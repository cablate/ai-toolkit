# Claude Code StatusLine - Context & Cost Awareness
# Line 1: Model + Context bar + K values + context alert
# Line 2: 5h/7d plan usage

param()

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$jsonInput = ""
try {
    $inputStream = [System.IO.StreamReader]::new([System.Console]::OpenStandardInput())
    $jsonInput = $inputStream.ReadToEnd()
    $inputStream.Close()
}
catch {
    $jsonInput = '{"model":{"display_name":"Claude"}}'
}

try {
    $inputData = $jsonInput | ConvertFrom-Json

    $modelName = if ($inputData.model.display_name) { $inputData.model.display_name } else { "Claude" }
    $outputStyle = if ($inputData.output_style.name) { $inputData.output_style.name } else { "" }
    $transcriptPath = $inputData.transcript_path
    $contextWindowSize = $inputData.context_window.context_window_size

    # ============================================================
    # Plan usage: prefer inline rate_limits (2.1.80+), fallback to OAuth API
    # ============================================================
    $usageData = $null
    $usageSource = "none"  # "inline" or "api"

    if ($inputData.rate_limits) {
        # 2.1.80+: rate_limits provided directly in statusline JSON
        $usageData = $inputData.rate_limits
        $usageSource = "inline"
    }

    if (-not $usageData) {
        # Fallback: fetch from OAuth API with resilient cache
        $cachePath = Join-Path $env:TEMP "claude_usage_cache.json"
        $successTtlSeconds = 300
        $failureTtlSeconds = 15
        $rateLimitBaseSeconds = 60
        $rateLimitMaxSeconds = 300

        try {
            $now = Get-Date
            $useCache = $false
            $cacheObj = $null

            if (Test-Path $cachePath) {
                try { $cacheObj = Get-Content $cachePath -Raw | ConvertFrom-Json -ErrorAction Stop } catch { $cacheObj = $null }
            }

            if ($cacheObj -and $cacheObj.timestamp) {
                $cacheTime = [DateTimeOffset]::FromUnixTimeMilliseconds([long]$cacheObj.timestamp).LocalDateTime
                $cacheAge = ($now - $cacheTime).TotalSeconds

                $effectiveTtl = $successTtlSeconds
                if ($cacheObj.rateLimitedCount -and [int]$cacheObj.rateLimitedCount -gt 0) {
                    $backoffPower = [Math]::Min([int]$cacheObj.rateLimitedCount - 1, 3)
                    $effectiveTtl = [Math]::Min($rateLimitBaseSeconds * [Math]::Pow(2, $backoffPower), $rateLimitMaxSeconds)
                } elseif ($cacheObj.isFailure) {
                    $effectiveTtl = $failureTtlSeconds
                }

                if ($cacheAge -lt $effectiveTtl) {
                    $useCache = $true
                    if ($cacheObj.lastGoodData) { $usageData = $cacheObj.lastGoodData }
                    elseif (-not $cacheObj.isFailure) { $usageData = $cacheObj.data }
                }
            }

            if (-not $useCache) {
                $credPath = Join-Path $env:USERPROFILE ".claude\.credentials.json"
                if (Test-Path $credPath) {
                    $creds = Get-Content $credPath -Raw | ConvertFrom-Json
                    $token = $creds.claudeAiOauth.accessToken

                    $tokenValid = $true
                    if ($creds.claudeAiOauth.expiresAt) {
                        try {
                            $expiry = [DateTimeOffset]::FromUnixTimeMilliseconds([long]$creds.claudeAiOauth.expiresAt).LocalDateTime
                            if ($expiry -lt $now) { $tokenValid = $false }
                        } catch {}
                    }

                    if ($token -and $tokenValid) {
                        $headers = @{
                            "Authorization"  = "Bearer $token"
                            "Content-Type"   = "application/json"
                            "anthropic-beta" = "oauth-2025-04-20"
                        }
                        try {
                            $resp = Invoke-RestMethod -Uri "https://api.anthropic.com/api/oauth/usage" -Headers $headers -Method Get -TimeoutSec 3 -ErrorAction Stop
                            $cacheData = @{
                                data = $resp
                                timestamp = [DateTimeOffset]::new($now).ToUnixTimeMilliseconds()
                                rateLimitedCount = 0
                                isFailure = $false
                            } | ConvertTo-Json -Depth 5
                            Set-Content $cachePath -Value $cacheData -Force
                            $usageData = $resp
                        }
                        catch {
                            $statusCode = 0
                            if ($_.Exception.Response) { $statusCode = [int]$_.Exception.Response.StatusCode }

                            $prevGoodData = $null
                            if ($cacheObj) {
                                if ($cacheObj.lastGoodData) { $prevGoodData = $cacheObj.lastGoodData }
                                elseif ($cacheObj.data -and -not $cacheObj.isFailure) { $prevGoodData = $cacheObj.data }
                            }
                            $prevRlCount = if ($cacheObj.rateLimitedCount) { [int]$cacheObj.rateLimitedCount } else { 0 }

                            $failCache = @{
                                data = $null
                                timestamp = [DateTimeOffset]::new($now).ToUnixTimeMilliseconds()
                                rateLimitedCount = if ($statusCode -eq 429) { $prevRlCount + 1 } else { 0 }
                                isFailure = $true
                                lastGoodData = $prevGoodData
                            } | ConvertTo-Json -Depth 5
                            Set-Content $cachePath -Value $failCache -Force
                            $usageData = $prevGoodData
                        }
                    }
                }
            }
            if ($usageData) { $usageSource = "api" }
        } catch {
            $usageData = $null
        }
    }

    # ============================================================
    # ANSI color codes
    # ============================================================
    $orangeMedium = "$([char]27)[38;5;208m"
    $orangeBright = "$([char]27)[38;5;220m"
    $dimGray = "$([char]27)[2m"
    $green = "$([char]27)[38;5;34m"
    $yellow = "$([char]27)[38;5;226m"
    $red = "$([char]27)[38;5;196m"
    $bold = "$([char]27)[1m"
    $reset = "$([char]27)[0m"

    $orangeColor = $orangeMedium
    if ($modelName -like "*Haiku*") { $orangeColor = $orangeBright }

    # ============================================================
    # Context window calculation
    # ============================================================
    $usagePercentage = $null
    $totalTokens = 0

    if ($inputData.context_window.used_percentage -ne $null) {
        $usagePercentage = [Math]::Round([double]$inputData.context_window.used_percentage, 1)
    }

    $cumulativeInput = [long]$inputData.context_window.total_input_tokens
    $cumulativeOutput = [long]$inputData.context_window.total_output_tokens

    # Get cache tokens from transcript for accurate count
    $cacheTokens = 0
    $transcriptInputTokens = 0

    if ($transcriptPath -and (Test-Path $transcriptPath)) {
        try {
            $lastLines = Get-Content $transcriptPath -Tail 50
            [array]::Reverse($lastLines)
            foreach ($line in $lastLines) {
                if ($line -match '"usage"') {
                    try {
                        $lineData = $line | ConvertFrom-Json -ErrorAction SilentlyContinue
                        if ($lineData.message.usage) {
                            $usage = $lineData.message.usage
                            $cacheTokens = [long]$usage.cache_read_input_tokens + [long]$usage.cache_creation_input_tokens
                            $transcriptInputTokens = [long]$usage.input_tokens
                            break
                        }
                    } catch { }
                }
            }
        } catch { }
    }

    if ($cacheTokens -gt 0 -or $transcriptInputTokens -gt 0) {
        $totalTokens = $transcriptInputTokens + $cacheTokens
    } else {
        $totalTokens = $cumulativeInput + $cumulativeOutput
    }

    if ($usagePercentage -eq $null) {
        $usagePercentage = if ($contextWindowSize -gt 0) {
            [Math]::Round(($totalTokens / $contextWindowSize) * 100, 1)
        } else { 0 }
    }

    # ============================================================
    # Progress bar
    # ============================================================
    $barWidth = 20
    $filledWidth = [Math]::Min([Math]::Floor(($usagePercentage / 100) * $barWidth), $barWidth)
    $emptyWidth = $barWidth - $filledWidth

    $barColor = $green
    if ($usagePercentage -ge 80) { $barColor = $red }
    elseif ($usagePercentage -ge 60) { $barColor = $yellow }

    $progressBar = "${barColor}[" + ("=" * $filledWidth) + $dimGray + ("-" * $emptyWidth) + "${barColor}]${reset}"

    # Format token counts
    $totalTokensFormatted = if ($totalTokens -ge 1000000) { "{0:0.0}M" -f ($totalTokens / 1000000) }
        elseif ($totalTokens -ge 1000) { "{0:0.0}K" -f ($totalTokens / 1000) }
        else { "$totalTokens" }

    $contextWindowFormatted = if ($contextWindowSize -ge 1000000) { "{0:0.0}M" -f ($contextWindowSize / 1000000) }
        elseif ($contextWindowSize -ge 1000) { "{0:0.0}K" -f ($contextWindowSize / 1000) }
        else { "$contextWindowSize" }

    # ============================================================
    # Context alert (token-based thresholds)
    # ============================================================
    $contextAlert = ""
    $totalTokensK = $totalTokens / 1000

    if ($totalTokensK -ge 300) {
        $contextAlert = "${red}${bold} !! HANDOFF NOW !!${reset}"
    } elseif ($totalTokensK -ge 200) {
        $contextAlert = "${red}${bold} ! /handoff${reset}"
    } elseif ($totalTokensK -ge 150) {
        $contextAlert = "${yellow} /handoff soon${reset}"
    }

    # ============================================================
    # Build Line 1: Model + Context + Alert
    # ============================================================
    $separator = "${dimGray} | ${reset}"

    $line1 = "${orangeColor}${bold}${modelName}${reset}"

    if ($outputStyle -and $outputStyle -ne "default") {
        $line1 += "${separator}${dimGray}${outputStyle}${reset}"
    }

    $line1 += "${separator}${progressBar} ${barColor}${bold}${totalTokensFormatted}${reset}${dimGray}/${contextWindowFormatted}${reset} ${barColor}${usagePercentage}%${reset}"

    if ($contextAlert) {
        $line1 += $contextAlert
    }

    # ============================================================
    # Build Line 2: 5h / 7d plan usage
    # ============================================================
    $line2 = ""

    if ($usageData) {
        $isStale = $false
        if ($usageSource -eq "api" -and $cacheObj -and $cacheObj.rateLimitedCount -and [int]$cacheObj.rateLimitedCount -gt 0) { $isStale = $true }
        $staleMark = if ($isStale) { "${dimGray}~${reset}" } else { "" }

        function Format-ResetCountdown($resetsAt, $isUnixTimestamp) {
            try {
                if ($isUnixTimestamp) {
                    $resetTime = [DateTimeOffset]::FromUnixTimeSeconds([long]$resetsAt).UtcDateTime
                } else {
                    $resetTime = [DateTimeOffset]::Parse($resetsAt).UtcDateTime
                }
                $diff = $resetTime - [DateTime]::UtcNow
                if ($diff.TotalSeconds -le 0) { return $null }
                $d = [Math]::Floor($diff.TotalDays); $h = $diff.Hours; $m = $diff.Minutes
                if ($d -gt 0) { return "${d}d ${h}h" }
                elseif ($h -gt 0) { return "${h}h ${m}m" }
                else { return "${m}m" }
            } catch { return $null }
        }

        function Get-UsageColor($pct) {
            if ($pct -ge 90) { return $red }
            elseif ($pct -ge 70) { return $yellow }
            else { return $green }
        }

        # inline uses used_percentage, API uses utilization
        $isInline = ($usageSource -eq "inline")

        $line2Parts = @()

        if ($usageData.five_hour) {
            $pct5h = if ($isInline) { [Math]::Round([double]$usageData.five_hour.used_percentage, 1) }
                     else { [Math]::Round([double]$usageData.five_hour.utilization, 1) }
            $color5h = Get-UsageColor $pct5h
            $part5h = "${dimGray}5h: ${reset}${staleMark}${color5h}${pct5h}%${reset}"
            $reset5h = Format-ResetCountdown $usageData.five_hour.resets_at $isInline
            if ($reset5h) { $part5h += " ${dimGray}(${reset5h})${reset}" }
            $line2Parts += $part5h
        }

        if ($usageData.seven_day) {
            $pct7d = if ($isInline) { [Math]::Round([double]$usageData.seven_day.used_percentage, 1) }
                     else { [Math]::Round([double]$usageData.seven_day.utilization, 1) }
            $color7d = Get-UsageColor $pct7d
            $part7d = "${dimGray}7d: ${reset}${staleMark}${color7d}${pct7d}%${reset}"
            $reset7d = Format-ResetCountdown $usageData.seven_day.resets_at $isInline
            if ($reset7d) { $part7d += " ${dimGray}(${reset7d})${reset}" }
            $line2Parts += $part7d
        }

        if ($line2Parts.Count -gt 0) { $line2 = $line2Parts -join $separator }
    }

    # ============================================================
    # Line 3: Handoff warning (only when >= 150K)
    # ============================================================
    $line3 = ""
    if ($totalTokensK -ge 250) {
        $line3 = "${red}${bold}!! DO NOT close/resume -- use /handoff first, or waste 6%+ of 5h tokens !!${reset}"
    }

    # ============================================================
    # Output
    # ============================================================
    [System.Console]::WriteLine("${reset}${line1}")
    if ($line2 -and $line3) {
        [System.Console]::WriteLine("${reset}${line2}")
        [System.Console]::Write("${reset}${line3}")
    } elseif ($line2) {
        [System.Console]::Write("${reset}${line2}")
    } elseif ($line3) {
        [System.Console]::Write("${reset}${line3}")
    }
    [System.Console]::Out.Flush()
}
catch {
    $orangeColor = "$([char]27)[38;5;208m"
    $bold = "$([char]27)[1m"
    $reset = "$([char]27)[0m"
    [System.Console]::Write("${orangeColor}${bold}Claude${reset}")
    [System.Console]::Out.Flush()
}

exit 0
