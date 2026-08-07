# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-08-07 - [Keyboard Accessibility & Visible Focus States for Custom Controls]
**Learning:** Custom non-semantic interactive elements (such as `div` elements representing user avatars or complex pull-string lamp switches) lack default keyboard interactivity and visual focus feedback. This prevents keyboard-only and assistive technology users from fully using key app flows.
**Action:** Always equip custom interactive `div` elements with `tabindex="0"`, `role="button"`, and appropriate `aria-label` attributes, register `keydown` listeners to handle Space/Enter, and provide custom visual focus feedback using CSS `:focus-visible` to ensure visual feedback is clear and intuitive during keyboard-only navigation.
