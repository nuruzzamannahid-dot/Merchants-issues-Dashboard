## 2026-03-01 - Telegram API Token Hardcoding in Reminder Bot
**Vulnerability:** A hardcoded Telegram Bot API token (`BOT_TOKEN`) was present directly in the configuration section of the `carrybee_reminder_bot.py` script.
**Learning:** Hardcoding API tokens and other secrets in source files poses a severe security risk of secrets exposure when the code is committed to version control systems (VCS).
**Prevention:** Always externalize API keys, access credentials, and other secrets using environment variables (such as loading with `os.environ.get`), key management services, or configuration secret injection pipelines, using hardcoded fallback values only for local debug modes with non-production limits if absolutely necessary.
