# Probability 

Probability is used in Machine Learning to model **uncertainty, randomness, and likelihood of events**. It is especially important in classification, Bayesian methods, statistics, and generative models.

---

## 1. Basic Probability

Probability measures how likely an event is to occur.

[
P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total possible outcomes}}
]

Probability ranges from:

[
0 \leq P(A) \leq 1
]

* `0` → Impossible
* `1` → Certain
* `0.5` → 50% chance

---

## 2. Sample Space & Events

### Sample Space

The **sample space** contains all possible outcomes.

Example: Rolling a die

```text
S = {1, 2, 3, 4, 5, 6}
```

### Event

An event is a subset of the sample space.

Example:

```text
A = {2, 4, 6}
```

Event `A` represents getting an even number.

---

## 3. Complement of an Event

The complement of event `A` means that `A` does not occur.

[
P(A^c) = 1 - P(A)
]

Example:

If:

[
P(A)=0.7
]

Then:

[
P(A^c)=0.3
]

---

## 4. Addition Rule

For two events:


$$P(A \cup B)=P(A)+P(B)-P(A\cap B)$$


If events are mutually exclusive:

$$
P(A\cap B)=0
$$

Therefore:

$$
P(A\cup B)=P(A)+P(B)
$$

---

## 5. Conditional Probability

Conditional probability measures the probability of an event given that another event has already occurred.

[
P(A|B)=\frac{P(A\cap B)}{P(B)}
]

Read as:

> Probability of A given B.

### ML Application

Conditional probability is fundamental to:

* Classification
* Bayesian inference
* Naive Bayes
* Recommendation systems

---

## 6. Independence

Two events are independent if the occurrence of one does not affect the other.

$$
P(A\cap B)=P(A)P(B)
$$

For independent events:

$$
P(A|B)=P(A)
$$

---

## 7. Bayes' Theorem

Bayes' theorem updates the probability of an event using new evidence.

$$
(P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

$$
P(A\mid B)=\frac{P(B\mid A)\cdot P(A)}{P(B)}
$$

Where:

* (P(A)) → Prior probability
* (P(B|A)) → Likelihood
* (P(B)) → Evidence
* (P(A|B)) → Posterior probability

### ML Application

Bayes' theorem is used in:

* Naive Bayes
* Spam detection
* Medical classification
* Fraud detection
* Bayesian inference

---

## 8. Random Variables

A random variable assigns numerical values to outcomes.

### Discrete Random Variable

Has countable values.

Example:

```text
Number of heads = {0, 1, 2, ...}
```

### Continuous Random Variable

Can take any value within a range.

Example:

```text
Height = 172.5 cm
```

---

## 9. Probability Distributions

A probability distribution describes how probabilities are distributed among possible values.

### Common Distributions

| Distribution | Common Use              |
| ------------ | ----------------------- |
| Bernoulli    | Binary outcomes         |
| Binomial     | Number of successes     |
| Normal       | Continuous measurements |
| Poisson      | Count of events         |
| Uniform      | Equal probability       |

Example:

```python
import numpy as np

samples = np.random.normal(loc=0, scale=1, size=1000)
```

---

## 10. Expected Value

Expected value represents the **long-run average outcome**.

For a discrete random variable:

$$
E[X]=\sum xP(x)
$$

In Python:

```python
values = np.array([1, 2, 3])
probabilities = np.array([0.2, 0.5, 0.3])

expected_value = np.sum(values * probabilities)
```

---

## 11. Variance

Variance measures how far values are spread from the mean.

$$
Var(X)=E[(X-\mu)^2]
$$

where (\mu) is the mean.

```python
np.var(data)
```

Higher variance means greater spread.

---

## 12. Probability Density

For continuous variables, probability is represented using a **Probability Density Function (PDF)**.

The probability of an exact continuous value is effectively zero; probabilities are obtained over intervals.

---

## 13. Probability in Machine Learning

Probability appears throughout ML:

| Concept                   | ML Application         |
| ------------------------- | ---------------------- |
| Conditional Probability   | Classification         |
| Bayes' Theorem            | Naive Bayes            |
| Random Variables          | Data Modeling          |
| Probability Distributions | Generative Models      |
| Expected Value            | Decision Making        |
| Variance                  | Model/Data Analysis    |
| Independence              | Naive Bayes Assumption |

---

## Key Takeaway

Focus on understanding this progression:

```text
Probability Basics
       ↓
Events
       ↓
Conditional Probability
       ↓
Independence
       ↓
Bayes' Theorem
       ↓
Random Variables
       ↓
Probability Distributions
       ↓
Expected Value & Variance
       ↓
Bayesian ML / Classification / Generative Models
```

### Useful Python Libraries

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
```

NumPy can be used for basic numerical experiments, while SciPy provides many statistical probability distributions and functions.