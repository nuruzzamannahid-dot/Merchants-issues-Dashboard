## 2026-08-06 - [Securing API Tokens and Escaping HTML in Telegram Reminders]
**Vulnerability:** Hardcoded Telegram bot API token and missing HTML escaping of user-supplied fields rendered in HTML-formatted Telegram messages.
**Learning:** Hardcoding credentials exposes sensitive API access keys. Additionally, formatting Telegram messages in HTML mode without escaping user inputs allows HTML injection and crashes the bot's parser when characters like `<` or `>` are encountered.
**Prevention:** Always load API tokens from environment variables, validating them only within the program's startup entry point. Use standard escape functions (like `html.escape`) on all external fields before embedding them into HTML-formatted message structures.
