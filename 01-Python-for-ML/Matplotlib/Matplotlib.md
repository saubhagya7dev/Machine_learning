# Matplotlib Cheat Sheet — Quick Revision for AI/ML
*(Every term explained — not just code)*

```python
import matplotlib.pyplot as plt
import numpy as np
```

---

## 1. Core Concepts & Terminology (learn this first — it prevents 90% of confusion)

| Term | Meaning |
|---|---|
| **Figure** | The entire window/canvas. One Figure can hold multiple plots. Think of it as the whole page. |
| **Axes** | A single plot/chart *inside* a Figure (it has an x-axis, y-axis, title, etc.). Confusingly, this is **not** the same as "axis." A Figure can contain many Axes (i.e., a grid of subplots). |
| **Axis** | One of the number lines on a plot — the x-axis or y-axis specifically (singular for one line). |
| **pyplot (`plt`)** | The "stateful" quick-plotting interface — it remembers the "current" figure/axes so you can just call `plt.plot(...)`, `plt.title(...)` etc. without naming them. Great for quick, single plots. |
| **Object-Oriented (OO) interface** | Instead of relying on "current" figure/axes, you explicitly create and use `fig` and `ax` objects: `fig, ax = plt.subplots()`. Recommended for anything with multiple subplots or reusable code. |
| **Artist** | The umbrella term for anything drawn on a Figure — lines, text, ticks, patches, everything visible is technically an "Artist" object. |
| **Backend** | The engine that actually renders the plot (to a window, a PNG file, a Jupyter notebook cell, etc.) — usually you don't need to touch this. |

---

## 2. Basic Plot Types

#### `plt.plot(x, y)`
**What it does:** draws a line plot connecting (x, y) points — default plot type, used for continuous data like trends over time (e.g., loss curves).
```python
plt.plot(x, y)
```

#### `plt.scatter(x, y)`
**What it does:** draws individual (x, y) points without connecting lines — used to see the relationship/spread between two variables.
```python
plt.scatter(x, y)
```

#### `plt.bar(x, height)`
**What it does:** vertical bar chart — used for comparing categories (e.g., feature importances, class counts).
```python
plt.bar(categories, values)
plt.barh(categories, values)  # horizontal version
```

#### `plt.hist(data, bins)`
**What it does:** histogram — bins continuous data into intervals and shows frequency counts. Core tool for understanding a feature's **distribution** before modeling.
- `bins` — number of intervals to split the data range into (more bins = finer detail, more noise).
```python
plt.hist(data, bins=30)
```

#### `plt.boxplot(data)`
**What it does:** shows median, quartiles (25th/75th percentile), and outliers in one compact shape — used for spotting outliers and comparing spread across groups.
```python
plt.boxplot(data)
```

#### `plt.pie(values)`
**What it does:** pie chart — shows proportion of categories out of a whole. Rarely used in ML work beyond simple class-balance visuals.
```python
plt.pie(values, labels=labels)
```

---

## 3. Customizing a Plot (labels, title, legend)

| Function | Explanation |
|---|---|
| `plt.title('text')` | Sets the title shown above the plot. |
| `plt.xlabel('text')` / `plt.ylabel('text')` | Labels the x-axis / y-axis so readers know what the numbers represent. |
| `plt.legend()` | Displays a legend box mapping colors/lines to their `label=` names (set inside `plot()`/`scatter()` calls). |
| `plt.xlim(min, max)` / `plt.ylim(min, max)` | Manually sets the visible range of the x-axis / y-axis. |
| `plt.xticks([...])` / `plt.yticks([...])` | Manually sets which tick marks (numbers) appear on an axis, and can rename them. |
| `plt.grid(True)` | Adds background gridlines — makes it easier to read exact values. |

```python
plt.plot(epochs, loss, label="train loss")
plt.plot(epochs, val_loss, label="val loss")
plt.title("Training Progress")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()  # renders the plot (needed outside Jupyter; often optional inside notebooks)
```

---

## 4. Styling — Colors, Lines, Markers

| Parameter | Meaning |
|---|---|
| `color=` | Sets the color of the line/points (e.g., `'red'`, `'#1f77b4'`, or shorthand `'r'`). |
| `linestyle=` (or `ls=`) | Line pattern: `'-'` solid, `'--'` dashed, `':'` dotted, `'-.'` dash-dot. |
| `linewidth=` (or `lw=`) | Thickness of the line in points. |
| `marker=` | Symbol drawn at each data point: `'o'` circle, `'s'` square, `'^'` triangle, `'x'` cross. |
| `alpha=` | Transparency, from 0 (invisible) to 1 (fully opaque) — useful when points overlap heavily. |
| `cmap=` | **Colormap** — a gradient of colors used to represent numeric values (e.g., in `scatter()` with a `c=` array, or `imshow()`). Common ones: `'viridis'`, `'coolwarm'`, `'plasma'`. |

```python
plt.plot(x, y, color="blue", linestyle="--", linewidth=2, marker="o", alpha=0.7)
plt.scatter(
    x, y, c=labels, cmap="viridis"
)  # color points by class label — great for visualizing clusters
```

---

## 5. Subplots — Multiple Plots in One Figure **[ML]**

#### `plt.subplots(nrows, ncols)`
**What it does:** creates a Figure containing a grid of Axes (subplots) in one call — the recommended way to build multi-panel comparisons (e.g., loss curve + accuracy curve side by side).
- `nrows`, `ncols` — grid dimensions.
- `figsize=(width, height)` — size of the whole Figure in inches.
- Returns `fig` (the Figure object) and `ax` (either a single Axes, or an array of Axes if more than one subplot).

```python
fig, ax = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns
ax[0].plot(epochs, loss)
ax[0].set_title("Loss")
ax[1].plot(epochs, accuracy)
ax[1].set_title("Accuracy")
plt.tight_layout()  # auto-adjusts spacing so labels/titles don't overlap
```
Note the OO-style methods on `ax`: `ax.set_title()`, `ax.set_xlabel()`, `ax.set_ylim()` — same idea as the `plt.` versions but scoped to one specific subplot.

---

## 6. Saving Figures

#### `plt.savefig('filename.png')`
**What it does:** saves the current figure to disk as an image file.
- `dpi=` — resolution (dots per inch); higher = sharper, larger file (300 is common for reports).
- `bbox_inches='tight'` — trims excess whitespace around the figure.
```python
plt.savefig("loss_curve.png", dpi=300, bbox_inches="tight")
```

---

## 7. Advanced Techniques

#### `ax.twinx()`
**What it does:** creates a second y-axis sharing the same x-axis — used to plot two variables with different scales on one chart (e.g., loss and learning rate).
```python
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(epochs, loss, "b-")
ax2.plot(epochs, lr, "r--")
```

#### `plt.annotate(text, xy, xytext)`
**What it does:** adds a text label pointing at a specific data point, optionally with an arrow — useful for highlighting a best epoch or an anomaly.
```python
plt.annotate(
    "best epoch", xy=(20, 0.1), xytext=(25, 0.3), arrowprops=dict(arrowstyle="->")
)
```

#### `plt.fill_between(x, y1, y2)`
**What it does:** shades the area between two curves — commonly used to show a confidence interval or error band around a prediction line.
```python
plt.fill_between(x, y_lower, y_upper, alpha=0.3)
```

#### `plt.xscale('log')` / `plt.yscale('log')`
**What it does:** switches an axis to logarithmic scale — useful when values span several orders of magnitude (e.g., learning rate sweeps).

#### `plt.imshow(array, cmap=)`
**What it does:** displays a 2D array as an image using a colormap — used to view actual images, confusion matrices, or attention/weight matrices.
```python
plt.imshow(image_array, cmap="gray")
plt.colorbar()  # adds a color scale legend next to the plot
```

---

## 8. Matplotlib Patterns Specific to AI/ML **[ML — high value]**

```python
# Training/validation loss curve — the single most common ML plot
plt.plot(epochs, train_loss, label="train")
plt.plot(epochs, val_loss, label="validation")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.title("Loss Curve")

# Confusion matrix as a heatmap
plt.imshow(conf_matrix, cmap="Blues")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Feature importance bar chart
plt.barh(feature_names, importances)
plt.xlabel("Importance")

# Decision boundary (2D classifier visualization)
plt.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")  # colors the decision regions
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolors="k")

# ROC curve
plt.plot(fpr, tpr, label=f"AUC = {auc_score:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")  # random-guess baseline
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
```

---

## Quick-Glance: Most-Used Functions in AI/ML Work

| Function | Purpose |
|---|---|
| `plt.plot()` | Line plots — loss/accuracy curves |
| `plt.scatter()` | Relationship between two variables, colored by class |
| `plt.hist()` | Feature distribution before modeling |
| `plt.boxplot()` | Outlier detection |
| `plt.subplots()` | Multi-panel comparison figures |
| `plt.imshow()` | Confusion matrices, images, weight matrices |
| `plt.legend()`, `.title()`, `.xlabel()/.ylabel()` | Make plots interpretable — never skip these |
| `plt.savefig()` | Export plots for reports/papers |
| `plt.fill_between()` | Confidence intervals / error bands |
| `plt.contourf()` | Decision boundary visualization |

## Golden Rules
- **Figure vs Axes** — remember: Figure = whole canvas, Axes = one individual chart. This single distinction is the source of most beginner confusion.
- **Prefer the OO interface (`fig, ax = plt.subplots()`)** once you're doing more than one quick plot — it's more predictable and scales to subplots cleanly.
- **Always label your axes and add a legend** — an unlabeled plot is close to useless for anyone else (including future you).
- **`plt.show()`** flushes and displays the plot; forgetting it outside notebooks means nothing appears.
- Matplotlib is **low-level and highly customizable but verbose** — for statistical plots on DataFrames, Seaborn (built on top of Matplotlib) is usually faster to write. Use Matplotlib directly when you need fine control (custom subplots, annotations, ML-specific visuals like ROC curves or decision boundaries).