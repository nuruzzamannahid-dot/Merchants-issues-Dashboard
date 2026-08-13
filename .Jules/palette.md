# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-08-13 - [Screen Reader Accessible Control Descriptors via sr-only]
**Learning:** Identified that critical dashboard and login controls (e.g. search inputs and filter selectors) lacked associated `<label>` elements, rendering them inaccessible to screen readers. Furthermore, interactive controls that transition to icon-only buttons on mobile screen sizes (such as the Refresh and Export CSV buttons) lacked explicit ARIA labels when their text labels were visually hidden.
**Action:** Always configure hidden, screen-reader accessible label elements using the Tailwind CSS utility class `sr-only` to describe non-visually labelled inputs and selects, and equip dynamically collapsing responsive buttons with descriptive `aria-label` tags.
