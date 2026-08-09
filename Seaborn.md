# Seaborn Cheat Sheet — Quick Revision for AI/ML
*(Every term explained — not just code)*

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

---

## 1. Core Concepts & Terminology (learn this first)

| Term | Meaning |
|---|---|
| **Seaborn is built on Matplotlib** | It doesn't replace Matplotlib — it generates Matplotlib figures under the hood, but with statistical logic and nicer defaults baked in. You can still use `plt.title()`, `plt.show()`, etc. alongside it. |
| **Works directly with DataFrames** | Instead of passing raw x/y arrays, you typically pass `data=df` and refer to **column names** as strings — this is seaborn's biggest convenience over raw Matplotlib. |
| **`hue`** | A column used to **color-code** points/bars by category — lets you encode a third variable (e.g., class label) using color. This is seaborn's signature feature. |
| **`style`** | A column used to vary **marker/line style** by category (in addition to or instead of color). |
| **`size`** | A column used to vary the **size** of points/lines by a (usually numeric) variable. |
| **`palette`** | The set of colors used when mapping `hue` to colors (e.g., `'viridis'`, `'Set2'`, `'coolwarm'`). |
| **`kind`** | Used in figure-level functions to pick *which* plot type to draw (e.g., `kind='box'`, `kind='scatter'`). |
| **Estimator** | The aggregation function (default: mean) used to summarize multiple data points into one value — e.g., in `barplot`, the bar height is the *estimator* of `y` for each category. |
| **Confidence interval (`errorbar`/older `ci`)** | The shaded/whisker range shown around an estimate, indicating uncertainty — shown by default on `barplot`/`lineplot`. |
| **Figure-level vs Axes-level functions** | **Axes-level** functions (e.g. `scatterplot`, `boxplot`, `histplot`) draw onto a single Matplotlib `Axes` and can be placed into `plt.subplots()` grids manually. **Figure-level** functions (e.g. `relplot`, `catplot`, `displot`, `lmplot`) manage their *own* Figure and can automatically create a grid of subplots (facets) using `col=`/`row=`. You generally can't mix a figure-level function into an existing subplot grid. |
| **FacetGrid** | The mechanism figure-level functions use to create a **grid of subplots**, one per category of a `col=`/`row=` variable — e.g., a separate scatterplot per class label, all in one image. |

---

## 2. Distribution Plots — understanding a single variable's spread **[ML]**

#### `sns.histplot(data=df, x='col')`
**What it does:** histogram (like `plt.hist`, but DataFrame-aware and prettier) — shows how values of a feature are distributed.
- `bins=` — number of bins.
- `kde=True` — overlays a smoothed density curve on top of the bars.
- `hue='category'` — draws separate colored histograms per category, overlapping in one plot.
```python
sns.histplot(data=df, x="age", bins=20, kde=True, hue="target")
```

#### `sns.kdeplot(data=df, x='col')`
**What it does:** **Kernel Density Estimate** — a smoothed, continuous curve approximating the distribution (like a smoothed histogram, no bins needed).
```python
sns.kdeplot(
    data=df, x="age", hue="target", fill=True
)  # fill=True shades under the curve
```

#### `sns.displot(...)`
**What it does:** the **figure-level** version of `histplot`/`kdeplot` — same idea, but can create a grid via `col=`.
- `kind='hist'` or `kind='kde'` — chooses which distribution plot to draw.

#### `sns.rugplot(data=df, x='col')`
**What it does:** draws small tick marks on the axis for every individual observation — often layered under a histogram/kde to show exact data density. Rarely used alone.

---

## 3. Categorical Plots — comparing a numeric variable across groups **[ML]**

#### `sns.boxplot(data=df, x='category', y='value')`
**What it does:** shows median, quartiles (box edges), and outliers (dots beyond the "whiskers") for each category — the fastest way to compare spread/outliers across groups.
```python
sns.boxplot(data=df, x="class", y="age")
```

#### `sns.violinplot(data=df, x='category', y='value')`
**What it does:** combines a box plot with a KDE — the "violin" shape shows the full distribution density, not just quartiles, for each category. More informative than a boxplot, but denser to read.

#### `sns.barplot(data=df, x='category', y='value')`
**What it does:** shows the **mean** (or another `estimator=`) of `y` per category as a bar, with an error bar showing the confidence interval — this is *not* just counting rows (see `countplot` below), it's aggregating a numeric column.

#### `sns.countplot(data=df, x='category')`
**What it does:** counts and plots how many rows fall into each category — the visual version of `df['col'].value_counts()`. Very commonly used to check **class imbalance** in a target variable.
```python
sns.countplot(data=df, x="target")
```

#### `sns.stripplot(data=df, x='category', y='value')`
**What it does:** plots every individual point for each category with slight random horizontal jitter, so overlapping points are visible — good for seeing raw data alongside a box/violin plot.

#### `sns.swarmplot(data=df, x='category', y='value')`
**What it does:** like `stripplot`, but algorithmically arranges points so none overlap — clearer for smaller datasets, slow on very large ones.

---

## 4. Relational Plots — relationship between two numeric variables **[ML]**

#### `sns.scatterplot(data=df, x='col1', y='col2', hue='target')`
**What it does:** scatter plot, DataFrame-aware, with easy `hue`/`style`/`size` semantic mapping — the go-to plot for visually checking if two features separate by class.
```python
sns.scatterplot(data=df, x="feature1", y="feature2", hue="target", style="target")
```

#### `sns.lineplot(data=df, x='col1', y='col2')`
**What it does:** line plot that, by default, also aggregates and shows a confidence interval if multiple `y` values exist per `x` — useful for plotting a metric over time/epochs across multiple runs.

#### `sns.relplot(...)`
**What it does:** the **figure-level** version of `scatterplot`/`lineplot` — set `kind='scatter'` or `kind='line'`, and use `col=`/`row=` to facet into subplots automatically.

---

## 5. Matrix Plots — visualizing 2D grids of values **[ML — very high value]**

#### `sns.heatmap(data)`
**What it does:** color-encodes a 2D matrix (usually a DataFrame or NumPy array) — the standard way to visualize a **correlation matrix** or a **confusion matrix**.
- `annot=True` — writes the actual numeric value inside each cell.
- `cmap=` — colormap, e.g., `'coolwarm'` for correlations (diverging: negative vs positive).
- `fmt='.2f'` — number formatting for the annotations.
```python
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
```

#### `sns.clustermap(data)`
**What it does:** like `heatmap`, but also runs hierarchical clustering on rows/columns and reorders them, adding dendrograms (tree diagrams) on the sides — used to spot groups of correlated features.

---

## 6. Pairwise & Multi-Plot Grids — full-dataset EDA in one shot **[ML — high value]**

#### `sns.pairplot(df, hue='target')`
**What it does:** builds a grid of scatterplots for **every pair of numeric columns**, with histograms/KDEs on the diagonal — the fastest way to get a full visual overview of how features relate to each other and to the target class.
```python
sns.pairplot(df, hue="target", diag_kind="kde")
```
⚠️ Can get slow/cluttered with many columns — often run on a subset of important features.

#### `sns.jointplot(data=df, x='col1', y='col2', kind='scatter')`
**What it does:** a scatter (or hex/kde) plot of two variables **plus** their individual histograms on the top and right margins — a "2-variable EDA in one image" plot.
- `kind=` — `'scatter'`, `'kde'`, `'hex'`, or `'reg'` (adds a regression line).

#### `sns.FacetGrid(df, col='category')`
**What it does:** the lower-level building block behind figure-level functions — manually creates a grid of subplots split by category, onto which you `.map()` any plotting function. Rarely needed directly since `relplot`/`catplot`/`displot` cover most use cases.

---

## 7. Styling & Themes

| Function | Explanation |
|---|---|
| `sns.set_style('darkgrid')` | Sets the overall visual theme. Options: `'darkgrid'`, `'whitegrid'`, `'dark'`, `'white'`, `'ticks'`. |
| `sns.set_palette('Set2')` | Sets the default color palette used for `hue` mapping across all plots. |
| `sns.set_context('notebook')` | Scales font/line sizes for the output medium. Options: `'paper'`, `'notebook'`, `'talk'`, `'poster'` (small to large). |
| `sns.despine()` | Removes the top/right border lines of a plot for a cleaner look. |

```python
sns.set_style("whitegrid")
sns.set_context("talk")
```

---

## 8. Seaborn Patterns Specific to AI/ML **[ML — high value]**

```python
# Correlation heatmap — feature selection / multicollinearity check
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")

# Class-separability check across all features at once
sns.pairplot(df, hue="target")

# Class imbalance check
sns.countplot(data=df, x="target")

# Outlier / spread comparison across classes
sns.boxplot(data=df, x="target", y="feature1")

# Distribution of a feature, split by class
sns.kdeplot(data=df, x="feature1", hue="target", fill=True)

# Confusion matrix (after computing it with sklearn)
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names,
)
```

---

## Quick-Glance: Most-Used Functions in AI/ML Work

| Function | Purpose |
|---|---|
| `sns.histplot()` / `sns.kdeplot()` | Feature distribution, optionally split by class via `hue` |
| `sns.boxplot()` / `sns.violinplot()` | Outlier detection & spread comparison across categories |
| `sns.countplot()` | Class imbalance check |
| `sns.scatterplot()` | Feature relationships, colored by class |
| `sns.heatmap()` | Correlation matrix, confusion matrix |
| `sns.pairplot()` | Full-dataset EDA — all feature pairs at once |
| `sns.jointplot()` | Two-variable relationship + individual distributions |
| `hue=`, `style=`, `size=` | Encode extra variables via color/shape/size |
| `sns.relplot()` / `sns.catplot()` / `sns.displot()` | Figure-level versions that support automatic faceting via `col=`/`row=` |

## Golden Rules
- **`hue` is seaborn's superpower** — almost any plot becomes far more useful for ML (spotting class separability) the moment you add `hue='target'`.
- **Know the difference between figure-level and axes-level functions** — figure-level functions (`relplot`, `catplot`, `displot`) return a `FacetGrid`/`Figure` object and can't be dropped into an existing `plt.subplots()` grid; axes-level functions (`scatterplot`, `boxplot`, `heatmap`) can, via `ax=`.
- **`sns.pairplot(df, hue='target')`** is often the single most useful line for first-look EDA on a small-to-medium dataset.
- Seaborn still runs on Matplotlib, so `plt.title()`, `plt.xlabel()`, `plt.savefig()`, and `plt.show()` all still work on seaborn plots.
- For heatmaps (correlation/confusion matrices), always add `annot=True` when the matrix is small enough to read — raw color alone is hard to interpret precisely.