# Sentinel Security Journal

## 2026-07-25 - Hardcoded Telegram Bot API Token
**Vulnerability:** A highly critical Telegram Bot API Token was hardcoded as a global constant `BOT_TOKEN` in `carrybee_reminder_bot.py` and exposed in documentation/print statements.
**Learning:** Developing API-reliant automation scripts often leads to hardcoding secrets for ease of development and quick local testing, but this results in credentials leaking into Git repositories and public source files.
**Prevention:** Always load secrets strictly from external configurations like environment variables or a local `.env` file that is gitignored. Ensure that any default token placeholders or console output logs mask the API keys or dynamically load them rather than embedding strings.
