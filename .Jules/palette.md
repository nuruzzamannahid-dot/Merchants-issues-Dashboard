# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-07-29 - [Friction-Free Empty Search States with Interactive Recovery]
**Learning:** Adding an explicit, keyboard-accessible "Clear Filters" button in an empty search/filter result state drastically reduces cognitive friction and interaction cost. Instead of forcing users to manually erase text queries and reset multiple dropdown selects one-by-one, a single recovery action restores the default dashboard state instantly. Additionally, when a UI element has an `aria-label`, its accessible name is strictly calculated from that attribute rather than inner text nodes, which must be kept in mind during both accessibility compliance and automated browser verification.
**Action:** Always provide an intuitive and accessible escape hatch (like a "Clear Filters" button) within empty search/filter results to allow quick recovery, and ensure it is fully compatible with screen reader accessible name calculations.
