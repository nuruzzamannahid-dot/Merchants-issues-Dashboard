# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-08-14 - [Password Visibility Toggle and Hidden Inputs in Compact Dark Login Forms]
**Learning:** Found that highly compact dark login card designs often omit standard text labels to maximize screen space, but this entirely breaks accessibility for screen-reader users unless visually hidden `sr-only` labels are provided. Additionally, password show/hide button controls require dynamic SVG icon swapping (e.g., standard eye to slashed eye) alongside programmatic `aria-label` updates, as visual and assistive feedback must remain in perfect sync.
**Action:** Always pair compact textless inputs with `sr-only` labels linked via `for`/`id` to maintain full accessibility. When creating password toggle buttons, ensure they are explicitly defined as `type="button"` to avoid accidental form submissions, and dynamically swap their SVG icons to represent current visibility state.
