## 2026-07-25 - [Optimize CSV Parsing using Standard Library csv.reader]
**Learning:** Hand-rolled character-by-character string parsers implemented in pure Python have massive performance overhead (taking O(N) in Python bytecode with lots of string object copying and conditionals) and can easily fail on edge cases like embedded commas or multiline quoted columns. Using standard library `csv.reader` (which is written in optimized C) is ~3x to 12x faster, and handles complex RFC 4180 parsing correctly.
**Action:** Always prefer standard library, C-implemented parsing modules (like `csv`, `json`, `xml.etree.ElementTree`) over hand-rolled parsing logic for processing structured data formats.

## 2026-08-04 - [Batching DOM Updates and Decoupling Render Triggers in Issue Tracker]
**Learning:** Dynamic DOM additions (e.g., using `+=` inside loops) trigger browser layout recalculations and style reflows on every single iteration, leading to $O(N^2)$ rendering bottlenecks and UI lag. Decoupling expensive computational work (like parsing unique tags) from fast user input triggers (such as keyup search events) prevents unnecessary CPU-intensive calculations.
**Action:** Accumulate dynamic HTML templates into an array and perform a single batch write using `.innerHTML = array.join('')`. Cache and separate dropdown filter generation from standard table filtering and rendering loops.
