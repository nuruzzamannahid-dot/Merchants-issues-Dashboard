## 2026-08-16 - [Short-circuit Empty Searches and Memoize Geocode Lookups]
**Learning:** In interactive tables and map views, evaluating `.toLowerCase()` and substring matches across large datasets on empty search inputs creates unnecessary CPU work and heap string allocations. Similarly, scanning large keyword arrays (~120 elements) for repeating hub location names during map and list renders incurs redundant linear overhead.
**Action:** Always short-circuit search evaluation when the query string is empty (`!search || ...`) and use `Map` memoization for deterministic string geocoding/parsing helper functions.

## 2026-07-25 - [Optimize CSV Parsing using Standard Library csv.reader]
**Learning:** Hand-rolled character-by-character string parsers implemented in pure Python have massive performance overhead (taking O(N) in Python bytecode with lots of string object copying and conditionals) and can easily fail on edge cases like embedded commas or multiline quoted columns. Using standard library `csv.reader` (which is written in optimized C) is ~3x to 12x faster, and handles complex RFC 4180 parsing correctly.
**Action:** Always prefer standard library, C-implemented parsing modules (like `csv`, `json`, `xml.etree.ElementTree`) over hand-rolled parsing logic for processing structured data formats.
