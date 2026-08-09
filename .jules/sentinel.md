## 2026-06-29 - [Secure Secrets Handling in Telegram Reminder Bot]
**Vulnerability:** A hardcoded Telegram Bot Token API credential was committed in the configuration variables of `carrybee_reminder_bot.py` and exposed in `README.md`.
**Learning:** Credentials stored directly in codebase files risk exposure, checkout leaks, and unauthorized control of bot messaging actions. They must be loaded dynamically from secure runtime environments.
**Prevention:** Always load secrets, API keys, and tokens from environment variables at runtime, and check for their presence on startup, halting execution gracefully if missing.
