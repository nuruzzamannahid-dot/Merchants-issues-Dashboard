# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-08-01 - [Keyboard Focus Visibility and Semantic Dropdowns]
**Learning:** Custom interactive div-based controls (like `#userAvatar`) lack built-in focusability, screen-reader context, and keyboard activation support. Adding `:focus-visible` styling alongside standard button/dialog attributes (`role="button"`, `tabindex="0"`, `aria-*`) makes these custom widgets fully accessible without compromising visual aesthetic.
**Action:** Always verify that custom active elements can be navigated to via the keyboard and provide clear visual `:focus-visible` outlines matching the brand style.
