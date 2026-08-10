# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-08-10 - [Keyboard Accessibility and Circular Focus Rings on Custom Interactive Components]
**Learning:** Custom interactive elements (such as `div` based user avatars and menu dropdown items) do not automatically inherit keyboard interactivity or semantic roles. Furthermore, global `:focus-visible` outline styles often impose standard rectangular border-radii (e.g. `6px`), which can visually distort circular widgets when they receive keyboard focus.
**Action:** When converting non-semantic `div` elements into interactive controls, always declare explicit focus styling (e.g., `.user-avatar:focus-visible { border-radius: 50% !important; }` for circular elements) alongside `tabindex="0"`, `role="button"`, `aria-label`, and keyboard event handlers.
