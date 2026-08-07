# Sentinel's Journal - Critical Security Learnings

## 2026-07-25 - [Hardcoded Telegram Bot Token Credential Leak]
**Vulnerability:** A raw, valid sensitive Telegram Bot API Token was exposed in the README.md and carrybee_reminder_bot.py configuration.
**Learning:** Hardcoding credentials inside source code, configuration files, or documentation can easily result in credential theft, unauthorized API access, and security breaches. In logistics notification scenarios, exposing the bot token lets attackers intercept operational message queues, send unauthorized messages, or manipulate internal communications.
**Prevention:** Always load secrets dynamically from externalized sources such as environment variables (`os.environ`). Redact all documentation and configuration file occurrences of real tokens with placeholder values (such as `REDACTED_TELEGRAM_BOT_TOKEN`) to prevent leaking secrets in version control.
