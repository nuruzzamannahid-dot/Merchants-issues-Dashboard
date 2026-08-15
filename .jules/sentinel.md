## 2026-06-29 - Hardcoded Telegram Bot Token Removal
**Vulnerability:** Telegram Bot Token was hardcoded directly in `carrybee_reminder_bot.py` and documented in `README.md`.
**Learning:** Hardcoded credentials in source code or documentation present a severe risk of secret leakage to repository viewers or public source control.
**Prevention:** Always load sensitive API credentials dynamically from environment variables (e.g. `TELEGRAM_BOT_TOKEN`) and redact raw tokens in README/docs with placeholders. Perform validation checks inside `if __name__ == '__main__':` boundary to prevent premature script exits when imported.
