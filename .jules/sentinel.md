## 2026-07-29 - [Secure Telegram Bot Token configuration]
**Vulnerability:** Hardcoded API keys and Telegram Bot Token in application source files (`carrybee_reminder_bot.py`) and configuration files (`README.md`).
**Learning:** Hardcoding credentials exposes sensitive API access tokens to anyone with read access to the repository, which can lead to unauthorized control over the Telegram bot and information leakage.
**Prevention:** Always load sensitive API credentials dynamically from environment variables (e.g. `TELEGRAM_BOT_TOKEN`), and perform safe runtime checks to exit securely if required configuration keys are missing. Keep user configuration manuals free of raw secret keys.
