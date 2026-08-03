# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-07-26 - [Keyboard Focus and Custom Interactive Element Navigation]
**Learning:** Found that custom interactive elements with tabindex or focus capability (such as the pull string lamp zone `#pullZone`, the `.theme-toggle` buttons, the `.login-eye-toggle`, and the `.user-avatar`) lacked clear `:focus-visible` indicators. This made keyboard navigation invisible and confusing for accessibility-focused users. Furthermore, using plain divs like `.user-avatar` as buttons without a `role="button"`, proper ARIA states (like `aria-expanded`), and keydown handlers prevented screen readers from interacting with them.
**Action:** Always styling custom interactive/focusable controls with `:focus-visible` outline rings to ensure prominent visual focus. When designing interactive custom elements, equip them with semantic roles, correct ARIA attributes (such as `aria-haspopup` and `aria-expanded`), and active event listeners for keyboard activation (e.g., Space and Enter keys).
