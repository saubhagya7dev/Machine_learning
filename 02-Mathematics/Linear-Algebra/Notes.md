# Linear Algebra for Machine Learning

Linear Algebra is the mathematical foundation behind many Machine Learning and Deep Learning algorithms. It provides the tools to represent and manipulate data efficiently.

---

## 1. Scalars

A **scalar** is a single numerical value.

```python
x = 5
```

Examples:

* Learning rate
* Temperature
* Age

---

## 2. Vectors

A **vector** is an ordered collection of numbers.

$$
v = [v_1, v_2, ..., v_n]
$$

Example:

```python
import numpy as np

v = np.array([2, 4, 6])
```

### Common Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b
a - b
2 * a
```

### Dot Product

$$
a \cdot b = \sum_{i=1}^{n} a_i b_i
$$

```python
np.dot(a, b)
```

The dot product is heavily used in **linear models and neural networks**.

---

## 3. Matrices

A **matrix** is a rectangular arrangement of numbers.

$$
A =
\begin{bmatrix}
1 & 2 \
3 & 4
\end{bmatrix}
$$

```python
A = np.array([[1, 2], [3, 4]])
```

Matrices are commonly used to represent:

* Datasets
* Transformations
* Model parameters
* Neural network weights

---

## 4. Matrix Operations

### Addition

Matrices must have the same dimensions.

```python
A + B
```

### Matrix Multiplication

$$
C = AB
$$

```python
C = A @ B
```

Matrix multiplication is fundamental to **neural network computations**.

---

## 5. Transpose

The transpose swaps rows and columns.

$$
A^T
$$

```python
A.T
```

Example:

```text
A = [[1, 2],
     [3, 4]]

Aᵀ = [[1, 3],
       [2, 4]]
```

---

## 6. Identity Matrix

An identity matrix has `1`s on the main diagonal and `0`s elsewhere.

$$
I =
\begin{bmatrix}
1 & 0 \
0 & 1
\end{bmatrix}
$$

```python
np.eye(2)
```

It behaves like `1` in matrix multiplication:

$$
AI = IA = A
$$

---

## 7. Determinant

The determinant is a scalar value calculated from a square matrix.

For a 2×2 matrix:

$$
A =
\begin{bmatrix}
a & b \
c & d
\end{bmatrix}
$$

$$
\det(A) = ad - bc
$$

```python
np.linalg.det(A)
```

A determinant of `0` means the matrix is **singular** and does not have an inverse.

---

## 8. Inverse

The inverse of a matrix (A) is written as:

$$
A^{-1}
$$

such that:

$$
AA^{-1} = I
$$

```python
np.linalg.inv(A)
```

Only non-singular square matrices have an inverse.

---

## 9. Eigenvalues & Eigenvectors

For a matrix (A):

$$
Av = \lambda v
$$

Where:

* (A) = matrix
* (v) = eigenvector
* (\lambda) = eigenvalue

In Python:

```python
values, vectors = np.linalg.eig(A)
```

### ML Applications

Eigenvalues and eigenvectors are important in:

* PCA
* Dimensionality Reduction
* Spectral Clustering
* Covariance Analysis

---

## 10. Norm

A norm measures the **magnitude or length of a vector**.

For a vector:

$$
v = [v_1,v_2,...,v_n]
$$

The L2 norm is:

$$
||v||_2 = \sqrt{\sum v_i^2}
$$

```python
np.linalg.norm(v)
```

Norms are widely used in **regularization and optimization**.

---

## 11. Linear Transformations

A matrix can transform a vector.

$$
y = Ax
$$

This can represent operations such as:

* Rotation
* Scaling
* Reflection
* Projection

This concept becomes important in **computer vision and neural networks**.

---

## 12. Linear Algebra in Machine Learning

Linear Algebra appears throughout ML:

| Concept               | ML Application          |
| --------------------- | ----------------------- |
| Vectors               | Features                |
| Matrices              | Datasets & weights      |
| Dot Product           | Linear Regression       |
| Matrix Multiplication | Neural Networks         |
| Transpose             | Mathematical operations |
| Eigenvectors          | PCA                     |
| Norms                 | Regularization          |
| Vector Spaces         | Feature Representation  |

---

## Key Takeaway

The most important concepts to understand for Machine Learning are:

```text
Vectors
   ↓
Matrices
   ↓
Dot Product
   ↓
Matrix Multiplication
   ↓
Transpose
   ↓
Eigenvalues & Eigenvectors
   ↓
Norms
   ↓
Linear Transformations
   ↓
PCA / Optimization / Neural Networks
```
