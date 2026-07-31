# Sentinel's Journal - Critical Security Learnings

## 2026-07-26 - [Telegram HTML Parser Vulnerability and Injection]
**Vulnerability:** User-supplied dynamic fields (such as merchant names, consignment IDs, tags, and details) were rendered directly into formatted HTML strings sent via the Telegram Bot API. If any of these fields contained HTML special characters (such as `<` or `>`), the Telegram parser would crash, causing failure to deliver critical reminders, or enabling HTML/XSS injection on Telegram clients.
**Learning:** Telegram API’s HTML `parse_mode` is highly sensitive to unbalanced HTML tags and entities. Failing to escape user-controlled spreadsheet data before interpolation leads to crashes and potential security risks.
**Prevention:** Always use `html.escape` to escape any dynamic user-supplied string fields before interpolating them into HTML messages intended for Telegram.
