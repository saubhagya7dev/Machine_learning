# NumPy Cheat Sheet — Quick Revision for AI/ML

> Organized basic → advanced. Sections marked **[ML]** are the ones you'll use constantly — every ML library (pandas, sklearn, PyTorch, TensorFlow) is built on NumPy arrays under the hood.

```python
import numpy as np
```

---

## 1. Creating Arrays
```python
np.array([1, 2, 3])
np.array([[1, 2], [3, 4]])  # 2D array (matrix)
np.zeros((3, 4))
np.ones((2, 3))
np.full((2, 2), 7)
np.eye(3)  # identity matrix
np.arange(0, 10, 2)  # like range(), but array
np.linspace(0, 1, 5)  # 5 evenly spaced values between 0 and 1
np.empty((2, 3))  # uninitialized (fast, garbage values)
```

## 2. Array Attributes & Inspection **[ML]**
```python
a.shape  # dimensions, e.g. (3, 4)
a.ndim  # number of dimensions
a.size  # total number of elements
a.dtype  # data type
a.itemsize  # bytes per element
a.nbytes  # total memory used
```

## 3. Data Types **[ML]**
```python
np.array([1, 2, 3], dtype=np.float32)
a.astype(np.int64)
a.astype("float32")  # common: cast to float32 for GPU-friendly ML models
```

## 4. Indexing & Slicing
```python
a[0]  # first element
a[-1]  # last element
a[1:4]  # slice
a[:, 0]  # first column (2D)
a[0, :]  # first row (2D)
a[1:3, 1:3]  # sub-matrix
a[::2]  # every other element
a[::-1]  # reverse
```

## 5. Boolean / Fancy Indexing **[ML]**
```python
a[a > 5]  # filter values > 5
a[(a > 2) & (a < 8)]  # combine conditions — use & | ~, not and/or
np.where(a > 5, 1, 0)  # conditional replace — very common for labeling/thresholds
a[[0, 2, 4]]  # select specific indices (fancy indexing)
np.nonzero(a > 5)  # indices where condition is true
```

## 6. Reshaping **[ML]**
```python
a.reshape(3, 4)
a.reshape(-1, 1)  # column vector — common before feeding into sklearn
a.reshape(-1)  # flatten to 1D
a.flatten()  # flatten, always returns a copy
a.ravel()  # flatten, returns a view when possible (faster)
a.T  # transpose
np.expand_dims(a, axis=0)  # add a dimension — common for batching in DL
np.squeeze(a)  # remove size-1 dimensions
```

## 7. Combining & Splitting Arrays
```python
np.concatenate([a, b], axis=0)
np.vstack([a, b])  # stack vertically (row-wise)
np.hstack([a, b])  # stack horizontally (column-wise)
np.stack([a, b], axis=0)  # stack along a new axis — common for building batches
np.split(a, 3)  # split into 3 equal parts
np.array_split(a, 3)  # split, allows unequal parts
```

## 8. Arithmetic & Vectorized Operations **[ML]**
```python
a + b, a - b, a * b, a / b  # element-wise
a**2
np.sqrt(a)
np.exp(a)
np.log(a)
np.abs(a)
np.round(a, 2)
```
**Rule of thumb:** vectorized NumPy ops >> Python loops. This is the entire reason NumPy exists for ML — orders of magnitude faster.

## 9. Broadcasting **[ML — core concept]**
```python
a + 5                    # scalar broadcast to every element
matrix + vector            # smaller array is "stretched" to match shape (no copy made)
# Rule: shapes are compatible if, from the right, dims are equal or one of them is 1.
(3,4) + (4,)   -> works
(3,4) + (3,1)  -> works
(3,4) + (3,)   -> fails
```
Broadcasting is why you can normalize a whole dataset (`(X - mean) / std`) in one line without loops.

## 10. Aggregation Functions **[ML]**
```python
a.sum()
a.mean()
a.std()
a.var()
a.min()
a.max()
a.argmin()
a.argmax()  # index of min/max — used to get predicted class
a.sum(axis=0)  # column-wise sum
a.sum(axis=1)  # row-wise sum
np.median(a)
np.percentile(a, 90)
np.cumsum(a)  # cumulative sum
```

## 11. Linear Algebra — the backbone of ML math **[ML]**
```python
np.dot(a, b)  # dot product
a @ b  # matrix multiplication (preferred syntax)
np.matmul(a, b)
a.T  # transpose
np.linalg.inv(a)  # matrix inverse
np.linalg.det(a)  # determinant
np.linalg.eig(a)  # eigenvalues & eigenvectors (used in PCA)
np.linalg.svd(a)  # singular value decomposition (used in PCA/recsys)
np.linalg.norm(a)  # vector/matrix norm (used in regularization, distances)
np.linalg.solve(A, b)  # solve Ax = b
```

## 12. Random Module — data generation, initialization, shuffling **[ML]**
```python
np.random.seed(42)  # reproducibility — always set this
np.random.rand(3, 3)  # uniform [0,1)
np.random.randn(3, 3)  # standard normal — common for weight init
np.random.randint(0, 10, size=(3, 3))
np.random.choice([1, 2, 3], size=5, replace=True)  # random sampling
np.random.shuffle(a)  # in-place shuffle (e.g. shuffling dataset)
np.random.permutation(a)  # returns shuffled copy

# modern recommended API:
rng = np.random.default_rng(42)
rng.normal(size=(3, 3))
```

## 13. Sorting & Searching
```python
np.sort(a)
np.argsort(a)  # indices that would sort the array
np.searchsorted(a, 5)  # binary search — find insertion point
np.unique(a)  # unique values
np.unique(a, return_counts=True)  # unique values + frequency
```

## 14. Comparison & Set Operations
```python
np.array_equal(a, b)
np.isin(a, [1, 2, 3])
np.intersect1d(a, b)
np.union1d(a, b)
np.setdiff1d(a, b)
```

## 15. Common ML-Specific Patterns **[ML — high value]**
```python
# Normalization / standardization
X_norm = (X - X.mean(axis=0)) / X.std(axis=0)

# Min-max scaling
X_scaled = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

# One-hot encoding via identity matrix
one_hot = np.eye(num_classes)[labels]

# Predicted class from probability scores
preds = np.argmax(probs, axis=1)

# Train/test split (manual, quick version)
idx = np.random.permutation(len(X))
split = int(0.8 * len(X))
X_train, X_test = X[idx[:split]], X[idx[split:]]

# Distance calculations (e.g. for KNN)
dist = np.linalg.norm(a - b)  # Euclidean distance
cosine_sim = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

## 16. Handling NaN / Missing Values
```python
np.isnan(a)
np.nan_to_num(a)  # replace NaN with 0 (and inf with large numbers)
np.nanmean(a)  # mean ignoring NaN
np.nansum(a)
```

## 17. Views vs Copies — Memory Behavior **[ML — performance]**
```python
b = a.view()  # same data, different object (changes affect both)
b = a.copy()  # independent copy (safe, but uses more memory)
a[1:3]  # slicing returns a VIEW, not a copy — be careful mutating it
```

## 18. Performance & Memory Optimization **[ML — large datasets]**
```python
a.astype(np.float32)  # use float32 instead of float64 to halve memory (GPU-friendly)
a.nbytes  # check memory footprint
np.vectorize(func)  # convenience wrapper, still python-level speed (not a real speedup)
# For real speed on huge arrays: prefer built-in vectorized ufuncs over np.vectorize or loops
```

---

## Quick-Glance: Most-Used Functions in AI/ML Work

| Function | Purpose |
|---|---|
| `np.array()`, `.reshape()` | Build & shape input data |
| `.shape`, `.dtype`, `.ndim` | Sanity-check array structure |
| `a @ b` / `np.dot()` | Matrix multiplication — core of neural nets |
| Broadcasting (`X - mean`) | Vectorized normalization, no loops |
| `np.mean/std/sum(axis=...)` | Compute per-feature statistics |
| `np.random.seed()` / `default_rng()` | Reproducible experiments |
| `np.argmax/argmin` | Convert probabilities → predicted class |
| `np.linalg.*` | PCA, distances, solving linear systems |
| `np.where()` | Conditional labeling/thresholding |
| `np.unique(return_counts=True)` | Class distribution / label counts |
| `np.concatenate/stack/vstack/hstack` | Build batches, combine datasets |
| `astype(np.float32)` | Memory/GPU optimization |
| `np.nan_to_num`, `np.isnan` | Handle missing/invalid values |

## Golden Rules
- **Vectorize everything.** If you're writing a `for` loop over an array, there's almost always a NumPy function for it.
- **Understand broadcasting** — it's the single most powerful (and most confusing at first) NumPy concept, and it underlies almost every ML preprocessing line.
- **`a @ b` for matrix multiply, `a * b` for element-wise** — mixing these up is one of the most common ML bugs.
- **Set a random seed** (`np.random.seed()` or `default_rng()`) whenever reproducibility matters.
- **Watch for views vs copies** when slicing — accidental mutation is a classic silent bug.
- **Use `float32`** over `float64` for large datasets/deep learning — it's the default expected dtype for GPUs.
- `axis=0` = down the columns (per-feature), `axis=1` = across the rows (per-sample) — mixing these up silently breaks aggregations.