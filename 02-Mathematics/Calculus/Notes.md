# Calculus for Machine Learning

Calculus helps Machine Learning models **understand how variables change and optimize model parameters**. It is especially important for gradient descent, neural networks, and optimization.

---

## 1. Functions

A function maps an input to an output.

$$
y = f(x)
$$

Example:

$$
f(x)=x^2+2x+1
$$

```python
def f(x):
    return x**2 + 2 * x + 1
```

In ML, functions are used to represent **models and loss functions**.

---

## 2. Limits

A limit describes the value a function approaches as the input approaches a particular value.

$$
\lim_{x\rightarrow a} f(x)
$$

Limits are the foundation of derivatives and continuous functions.

---

## 3. Derivatives

A derivative measures the **rate of change** of a function.

$$
f'(x)=\frac{dy}{dx}
$$

For:

$$
f(x)=x^2
$$

The derivative is:

$$
f'(x)=2x
$$

### Python

```python
import sympy as sp

x = sp.symbols("x")

f = x**2
derivative = sp.diff(f, x)

print(derivative)
```

### ML Application

Derivatives tell us how changing a model parameter affects the output or loss.

---

## 4. Partial Derivatives

When a function has multiple variables, we can calculate the derivative with respect to one variable while keeping the others constant.

For:

$$
f(x,y)=x^2+y^2
$$

$$
\frac{\partial f}{\partial x}=2x
$$

$$
\frac{\partial f}{\partial y}=2y
$$

Partial derivatives are essential for **machine learning models with many parameters**.

---

## 5. Gradient

The gradient is a vector containing all partial derivatives.

For:

$$
f(x,y)=x^2+y^2
$$

$$
\nabla f =
\begin{bmatrix}
2x\
2y
\end{bmatrix}
$$

The gradient points in the direction of the **steepest increase**.

In ML, we usually move in the opposite direction to minimize the loss.

---

## 6. Chain Rule

The chain rule is used to differentiate **composite functions**.

If:

$$
y=f(g(x))
$$

then:

$$
\frac{dy}{dx}
=============

\frac{dy}{dg}
\frac{dg}{dx}
$$

### Why it matters in ML

The chain rule is the mathematical foundation of **backpropagation** in neural networks.

```text
Input
  ↓
Layer 1
  ↓
Layer 2
  ↓
Output
  ↓
Loss
  ↓
Backpropagation
  ↓
Gradients
```

---

## 7. Optimization

Optimization means finding the parameters that minimize or maximize a function.

In ML, we usually minimize a **loss/cost function**.

$$
\theta^* = \arg\min_\theta L(\theta)
$$

Where:

* (\theta) = model parameters
* (L(\theta)) = loss function

---

## 8. Gradient Descent

Gradient descent is an optimization algorithm used to minimize a loss function.

The basic update rule is:

$$
\theta_{new}
============
\theta_{old}

\alpha\nabla L(\theta)
$$

Where:

* (\theta) = parameter
* (\alpha) = learning rate
* (\nabla L(\theta)) = gradient of the loss

### Simple Implementation

```python
theta = 10
learning_rate = 0.1

for _ in range(100):
    gradient = 2 * theta
    theta -= learning_rate * gradient

print(theta)
```

The parameter moves toward the minimum of the function.

---

## 9. Learning Rate

The learning rate controls **how large each optimization step is**.

```text
Small Learning Rate
→ Slow Training

Large Learning Rate
→ May Overshoot Minimum

Good Learning Rate
→ Faster Stable Convergence
```

Choosing an appropriate learning rate is important when training ML models.

---

## 10. Local & Global Minima

### Local Minimum

A point that is lower than nearby points but may not be the lowest point overall.

### Global Minimum

The lowest point of the entire function.

```text
Loss
 ↑
 │       /\          /\
 │      /  \        /  \
 │_____/    \______/    \____
 │          ↑
 │      Minimum
 └──────────────────────────→ Parameter
```

Optimization algorithms attempt to find a good minimum of the loss function.

---

## 11. Second Derivative

The second derivative describes how the rate of change itself changes.

$$
f''(x)
$$

It can provide information about the **curvature** of a function.

For:

$$
f(x)=x^2
$$

$$
f'(x)=2x
$$

$$
f''(x)=2
$$

Second-order derivatives are used in advanced optimization methods.

---

## 12. Calculus in Machine Learning

| Concept             | ML Application           |
| ------------------- | ------------------------ |
| Functions           | Model & Loss Functions   |
| Limits              | Mathematical Foundations |
| Derivatives         | Parameter Updates        |
| Partial Derivatives | Multiple Parameters      |
| Gradient            | Optimization             |
| Chain Rule          | Backpropagation          |
| Optimization        | Model Training           |
| Gradient Descent    | Minimizing Loss          |
| Second Derivative   | Advanced Optimization    |

---

## Key Takeaway

Focus on this progression:

```text
Functions
   ↓
Limits
   ↓
Derivatives
   ↓
Partial Derivatives
   ↓
Gradients
   ↓
Chain Rule
   ↓
Optimization
   ↓
Gradient Descent
   ↓
Backpropagation
   ↓
Neural Network Training
```

### Useful Python Libraries

```python
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
```

* **NumPy** → Numerical calculations
* **SymPy** → Symbolic differentiation
* **Matplotlib** → Visualizing functions and optimization
