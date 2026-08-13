## 2026-06-29 - [Fix Hardcoded Telegram Bot Token]
**Vulnerability:** The Telegram Bot API token was hardcoded inside the `carrybee_reminder_bot.py` configuration and exposed in the `README.md`.
**Learning:** Storing secrets directly in git-managed files makes them easily readable by anyone with repository access.
**Prevention:** Always load API tokens, credentials, and secrets dynamically from environment variables on startup. Validate the environment on script load and terminate gracefully if essential configuration is missing.
