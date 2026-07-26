## 2026-07-25 - [Optimize CSV Parsing using Standard Library csv.reader]
**Learning:** Hand-rolled character-by-character string parsers implemented in pure Python have massive performance overhead (taking O(N) in Python bytecode with lots of string object copying and conditionals) and can easily fail on edge cases like embedded commas or multiline quoted columns. Using standard library `csv.reader` (which is written in optimized C) is ~3x to 12x faster, and handles complex RFC 4180 parsing correctly.
**Action:** Always prefer standard library, C-implemented parsing modules (like `csv`, `json`, `xml.etree.ElementTree`) over hand-rolled parsing logic for processing structured data formats.

## 2026-07-26 - [Optimize DOM Manipulation and Redundant Filter Rebuilds]
**Learning:** Modifying DOM elements like `innerHTML` inside loops (e.g., `element.innerHTML += row`) forces the browser to repeatedly re-parse HTML strings, perform expensive layout recalculations (reflows), and trigger style recalculations. Additionally, rebuilding drop-down lists (such as the tag filter) on every keypress during searching is unnecessary.
**Action:** Always accumulate HTML templates into strings/arrays and update the DOM in a single batch update. Extract static or fetch-dependent dropdown list builders out of frequent interactive rendering paths (like search/keyup events).
