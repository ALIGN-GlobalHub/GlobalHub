# ALIGN Global Hub Brand & Design Guidelines

## 1. Vision & Strategy
The ALIGN Global Hub is a structured intelligence platform for tracking, classifying, and comparing health products. The design should reflect professional-grade data analytics: clean, authoritative, and highly legible.

## 2. Visual Identity

### Color Palette
*   **Primary Blue (`--brand-primary`):** `#012169` - Used for the main navigation and major headers.
*   **Accent Blue (`--brand-accent`):** `#00539B` - Used for primary buttons, active links, and progress indicators.
*   **Success Green (`--success-color`):** `#228B22` - Used for positive status indicators and 'Add' actions.
*   **Error Red (`--error-color`):** `#DC143C` - Used for negative status indicators and 'Delete/Remove' actions.
*   **Highlight Yellow (`--highlight-color`):** `#FFD700` - Reserved for critical warnings or special focus areas.
*   **Neutral Grays:**
    *   Dark Text: `#2F2F2F`
    *   Card Border: `#BFBBBB`
    *   Background: `#F8F9FA` (light gray for contrast with white cards)

### Typography
*   **Body Text:** 'Inter', sans-serif. Line height `1.6`.
*   **Headers:** 'Inter Tight', sans-serif. Bold weight (`700`).

## 3. UI Components & CSS Structure

### Layout Containers
*   **Sticky Hero:** `.sticky-hero-container` - Remains fixed below the navbar.
*   **Cards:** `.card` - Standard container for all modules.
    *   Border: `1px solid var(--card-border)`
    *   Radius: `0.5rem`
    *   Shadow: `0 4px 12px rgba(0,0,0,0.05)`
    *   Spacing: `2.5rem` bottom margin for top-level cards; nested cards should use `mb-0` or standardized row spacing (`1.5rem` bottom margin).
    *   **Headers:** `.card-header` - Standardized `min-height: 4.5rem` with centered flex layout to accommodate wrapped text and maintain vertical alignment.
    *   **Nested Cards:** Should remove box-shadows and use a subtle background (`#fafbfc`) to distinguish from parent containers.

### Input Elements
*   **Visibility:** All inputs (`.form-control`, `.form-select`, `.selectize-input`) have a defined border and `0.375rem` radius.
*   **Interaction:** Focus states use `var(--brand-accent)` for the border and a soft blue glow for the box-shadow to provide clear feedback.

### Spacing & Alignment
*   Internal card padding is set to `1.75rem`.
*   Grid gutters (`g-3`, `g-4`) are used consistently across rows.
*   **Sentence Case:** All UI text (labels, buttons, headers) should follow Sentence Case (e.g., "Product comparison" instead of "Product Comparison").

## 4. Specialized Components
*   **Value Boxes:** Custom styled `.bslib-value-box` with absolute-positioned info icons.
*   **Floating Actions:** `.floating-reset-btn` and `.floating-filter-status` for global controls that remain accessible during scrolling.
*   **Comparison Heatmap:** Uses a structured table with conditional formatting (green for "Yes"/high values, red for "No"/low values).
