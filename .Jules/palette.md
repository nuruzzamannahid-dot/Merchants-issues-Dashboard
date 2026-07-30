# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-07-30 - [Keyboard Focus and Screen-Reader Accessibility]
**Learning:** Learned that custom keyboard-interactive elements (like `#pullZone` and `.theme-toggle` buttons) need custom `:focus-visible` ring/outline styles so that keyboard navigation remains fully clear and accessible, and that visually hidden labels (using Tailwind's `sr-only`) are critical to associate programmatically with standard inputs/selects lacking external visible labels.
**Action:** Always add tailored `:focus-visible` CSS rules to custom interactive components to present high-contrast focus rings for keyboard navigating users, and pair unlabelled inputs with `sr-only` labels.
