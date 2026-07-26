# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-07-26 - [Interactive Keyboard & Focus States for Custom Controls]
**Learning:** Found that custom non-interactive elements (like `div` based user avatars) used as trigger menus are invisible to keyboard-only and screen reader navigation, and lack native focus cues.
**Action:** Always assign `role="button"`, `tabindex="0"`, appropriate ARIA attributes (such as `aria-haspopup` and `aria-expanded`), and attach a keydown event listener to support Space and Enter triggers. Additionally, declare clear `:focus-visible` styles with a high-contrast focus ring (like custom gold outlines) to ensure focus tracking remains visually intuitive.
