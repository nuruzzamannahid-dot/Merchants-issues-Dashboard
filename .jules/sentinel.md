# Sentinel's Journal

## 2026-03-01 - Telegram Bot Token Hardcoded in Source File
**Vulnerability:** Hardcoding sensitive secrets (like the Telegram Bot API Token) in the source code (`carrybee_reminder_bot.py`) exposes credentials to unauthorized parties, especially when checked into source control.
**Learning:** Hardcoded credentials are a frequent source of data leaks. Storing them directly in python source code makes rotation difficult and increases exposure risk.
**Prevention:** Load sensitive secrets dynamically from environment variables at runtime, and validate that they are set on startup. Provide clear, secure error messaging when configuration is missing.
