# 23 個 Bash Validator 分類

來源：`src/tools/BashTool/bashSecurity.ts`（2592 行）

## Misparsing Validators（Parser Differential 防禦）

| CheckID | 名稱 | 防禦的攻擊 |
|---------|------|-----------|
| BP001 | Process Substitution | `<(cmd)` 被 shell-quote 誤解為重導向 |
| BP002 | Brace Expansion | `{a,b}` 展開繞過命令過濾 |
| BP003 | ANSI-C Quoting | `$'\x72\x6d'` 解碼為 `rm` |
| BP004 | Command Substitution in Quotes | `"$(dangerous)"` 在引號內展開 |
| BP005 | Heredoc Injection | `<<EOF` 可注入任意命令 |
| BP006 | Arithmetic Expansion | `$((expr))` 可包含副作用 |
| BP007 | Array Syntax | `arr=(cmd)` 被誤解 |
| BP008 | Glob Injection | `*` 展開到意外的檔案名（含特殊字元） |

## Non-misparsing Validators（直接危險命令）

| CheckID | 名稱 | 防禦的風險 |
|---------|------|-----------|
| NP001 | Dangerous Commands | `rm -rf /`, `mkfs`, `dd if=/dev/zero` |
| NP002 | Network Exfiltration | `curl -d @/etc/passwd`, `nc -l` |
| NP003 | Privilege Escalation | `sudo`, `su`, `chmod 777` |
| NP004 | Disk Operations | `fdisk`, `mount`, `umount` |
| NP005 | System Modification | `systemctl`, `service`, `crontab -e` |
| NP006 | Package Managers with Install | `pip install`, `npm install -g` |
| NP007 | Compiler/Linker Abuse | 編譯帶 `-Wl,-rpath` 等注入 |

## Structural Validators

| CheckID | 名稱 | 防禦的風險 |
|---------|------|-----------|
| ST001 | Pipe to Shell | `curl ... \| bash` |
| ST002 | Background Processes | `&` fork bomb |
| ST003 | Multiple Statements | `;` 或 `&&` 串接危險命令 |
| ST004 | Alias/Function Definition | 定義覆蓋安全命令 |
| ST005 | History Manipulation | `history -c`, `HISTFILE=` |
| ST006 | Signal Trapping | `trap` 攔截安全機制 |
