## 2026-07-25 - [Optimize CSV Parsing using Standard Library csv.reader]
**Learning:** Hand-rolled character-by-character string parsers implemented in pure Python have massive performance overhead (taking O(N) in Python bytecode with lots of string object copying and conditionals) and can easily fail on edge cases like embedded commas or multiline quoted columns. Using standard library `csv.reader` (which is written in optimized C) is ~3x to 12x faster, and handles complex RFC 4180 parsing correctly.
**Action:** Always prefer standard library, C-implemented parsing modules (like `csv`, `json`, `xml.etree.ElementTree`) over hand-rolled parsing logic for processing structured data formats.

## 2026-07-26 - [Memoize Performance Metrics Row Calculations]
**Learning:** In `index.html`, `buildPerformanceRows()` performs complex office-hours vs. non-office-hours date calculations (`officeMsInRange`) on every issue row. Triggering `buildPerformanceRows()` on every keystroke in search filters creates significant main-thread overhead ($O(N \times \text{days})$ operations). Caching the built rows in `performanceRowsCache` and invalidating on `fetchData()` reduces filter response latency while ensuring data consistency.
**Action:** Always memoize derived row/dataset structures when rendering filtered tables if row calculations involve multi-step math or string transformations.
