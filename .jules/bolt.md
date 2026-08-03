## 2026-07-25 - [Optimize CSV Parsing using Standard Library csv.reader]
**Learning:** Hand-rolled character-by-character string parsers implemented in pure Python have massive performance overhead (taking O(N) in Python bytecode with lots of string object copying and conditionals) and can easily fail on edge cases like embedded commas or multiline quoted columns. Using standard library `csv.reader` (which is written in optimized C) is ~3x to 12x faster, and handles complex RFC 4180 parsing correctly.
**Action:** Always prefer standard library, C-implemented parsing modules (like `csv`, `json`, `xml.etree.ElementTree`) over hand-rolled parsing logic for processing structured data formats.

## 2026-08-03 - [Optimize High-Frequency DOM Render Triggers and Single-Batch Writes]
**Learning:** Iterative DOM updates like `element.innerHTML += html` inside loops trigger frequent browser layout recalcs and UI repaints, degrading rendering performance from O(N) to O(N^2). Additionally, rebuilding complete filter dropdowns inside high-frequency event handlers (like keyup searching) causes massive CPU overhead and layout thrashing.
**Action:** Always gather HTML templates into arrays/maps to execute a single-batch `innerHTML` write, and hoist expensive filter option rebuilds out of search-trigger paths into the primary data-fetch callback.
