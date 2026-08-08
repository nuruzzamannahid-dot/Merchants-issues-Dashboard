# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-07-26 - [Custom Interactive Element Keyboard Accessibility & Focus-Visible Styling]
**Learning:** Interactive CSS elements designed with custom shape properties (like circular avatars `#userAvatar` with `border-radius: 50%`) will receive standard rectangular keyboard focus outlines under blanket `:focus-visible` rules (like `border-radius: 6px`). This breaks visual consistency.
**Action:** Always add specific `:focus-visible` CSS rules for customized interactive controls (e.g., `.user-avatar:focus-visible { border-radius: 50% !important; }`) to maintain shape fidelity during keyboard navigation. Programmatic accessibility should be paired with proper `aria-expanded` and `aria-haspopup` attributes for custom dropdown triggers.
