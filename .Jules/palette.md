# Palette's Journal - Critical UX/A11y Learnings

## 2026-07-25 - [Form Accessibility in Issue Tracker Dashboard]
**Learning:** Found that the "Raise New Issue" form has form label elements that are visually descriptive but lack programmatic connection (the `for` attribute) to their target form inputs, dropdown, and textareas. This degrades the user experience for assistive technology users (like screen reader users) and prevents clicking on labels to focus fields.
**Action:** Always associate `<label>` elements with their target inputs using the `for` attribute referencing the exact `id` of the target elements. Also ensure icon-only interactive controls (such as the dark/light theme toggles and modal close buttons) are fully equipped with `aria-label` attributes for clear context.

## 2026-08-09 - [Keyboard Focus and Screen Reader Support on Profile/User Menus]
**Learning:** Learned that using plain `div` elements for custom dropdown menus and profile toggles breaks the default keyboard focus flow. Interactive profile indicators should have standard keyboard trigger listeners and ARIA button attributes, while their dropdown items are best styled as native HTML `<button>` elements to maintain keyboard-accessible actions.
**Action:** Configure custom avatars or toggle buttons with `tabindex="0"`, `role="button"`, and explicit keydown handlers. Replace plain clickable divs inside dropdown menus with native focusable `<button>` elements to optimize screen reader and keyboard-only interaction.
