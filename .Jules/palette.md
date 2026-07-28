# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-07-28 - [Interactive Containers and Dropdowns Accessibility in Layout]
**Learning:** Found that custom avatar containers and dropdown list items constructed from `<div>` elements are completely invisible to assistive technology and keyboard navigation unless explicitly structured with tabindex, aria-expanded, role="button", and keydown listeners, or replaced with semantic HTML `<button>` tags.
**Action:** Always convert interactive list/dropdown elements into semantic `<button>` tags with reset styles, or fully construct keyboard-accessible ARIA roles on `<div>` containers.
