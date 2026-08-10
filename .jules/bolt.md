## 2026-07-25 - [Optimize CSV Parsing using Standard Library csv.reader]
**Learning:** Hand-rolled character-by-character string parsers implemented in pure Python have massive performance overhead (taking O(N) in Python bytecode with lots of string object copying and conditionals) and can easily fail on edge cases like embedded commas or multiline quoted columns. Using standard library `csv.reader` (which is written in optimized C) is ~3x to 12x faster, and handles complex RFC 4180 parsing correctly.
**Action:** Always prefer standard library, C-implemented parsing modules (like `csv`, `json`, `xml.etree.ElementTree`) over hand-rolled parsing logic for processing structured data formats.

## 2026-08-10 - [Batch DOM Updates and Pulled Out Filter Building]
**Learning:** Performing iterative `innerHTML +=` updates inside loops forces the browser to serialize, parse, and rebuild the DOM tree multiple times, leading to an O(N^2) rendering bottleneck and frequent UI repaints. Additionally, rebuilding options for dropdowns on high-frequency triggers (like `onkeyup` search inputs) causes unnecessary CPU cycles on every single keystroke.
**Action:** Always batch DOM manipulations by collecting HTML strings in arrays or map operations and executing a single `.innerHTML` assignment. Extract any static or periodic option-building tasks out of high-frequency UI render pathways.
