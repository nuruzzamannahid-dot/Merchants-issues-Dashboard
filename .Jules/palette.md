# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-08-04 - [Keyboard Focus and Interaction for Custom Div Elements]
**Learning:** Adding standard focus visual support to custom interactive div elements (such as `#userAvatar`) requires explicit CSS `:focus-visible` outline styles, plus semantic HTML additions like `tabindex="0"`, `role="button"`, `aria-label`, and dedicated keydown listener logic for handling 'Enter' and Space (' ').
**Action:** Ensure custom non-button components with interaction capability are given proper keyboard visibility, semantics, and activation listeners.
