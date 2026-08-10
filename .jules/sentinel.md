## 2026-06-29 - Telegram Bot Token Leak Risk Prevention
**Vulnerability:** A hardcoded Telegram bot API token (`8851597317:[REDACTED]`) was exposed in both the source code of the reminder bot (`carrybee_reminder_bot.py`) and the setup documentation (`README.md`).
**Learning:** Hardcoding credentials in source code and tracking them in version control leaks control over communication channels to anybody with read access to the repository, presenting severe risks of spoofing, spamming, and API abuse.
**Prevention:** Always load secrets dynamically at runtime from environment variables or a secure vault, and add rigorous validation checks on startup to fail securely if configuration is missing, while ensuring testing contexts do not terminate prematurely.
