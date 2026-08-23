# Statistics for Machine Learning

Statistics helps Machine Learning understand **data, patterns, relationships, uncertainty, and model performance**.

---

## 1. Population & Sample

**Population** → The complete set of data.

**Sample** → A smaller subset taken from the population.

Example:

```text
Population → All customers of a bank
Sample     → 10,000 selected customers
```

ML models usually work with **samples** to learn patterns about a larger population.

---

## 2. Mean

The mean is the average of the values.

$$
\bar{x}=\frac{\sum x_i}{n}
$$

```python id="z4s5yx"
import numpy as np

data = [10, 20, 30, 40, 50]

np.mean(data)
```

Mean is commonly used for **data analysis and preprocessing**.

---

## 3. Median

The median is the middle value when data is sorted.

```python id="6h5vzo"
np.median(data)
```

Median is less affected by **outliers** than the mean.

---

## 4. Mode

The mode is the most frequently occurring value.

Example:

```text id="y3v4sm"
Data = [1, 2, 2, 3, 4]

Mode = 2
```

```python id="a1hlk4"
from statistics import mode

mode(data)
```

---

## 5. Range

Range represents the difference between the maximum and minimum values.

$$
Range = Maximum - Minimum
$$

```python id="1k5h6j"
np.max(data) - np.min(data)
```

---

## 6. Variance

Variance measures how spread out the data is around the mean.

$$
\sigma^2 =
\frac{1}{N}
\sum_{i=1}^{N}(x_i-\mu)^2
$$

```python id="qk1x6x"
np.var(data)
```

Higher variance means greater spread.

---

## 7. Standard Deviation

Standard deviation is the square root of variance.

$$
\sigma=\sqrt{\sigma^2}
$$

```python id="xq7h4w"
np.std(data)
```

It is useful for understanding how far values typically lie from the mean.

---

## 8. Percentiles & Quartiles

A **percentile** indicates the value below which a certain percentage of observations fall.

Common quartiles:

```text id="5d5y7u"
Q1 → 25th percentile
Q2 → 50th percentile (Median)
Q3 → 75th percentile
```

```python id="wq8k0x"
np.percentile(data, 25)
np.percentile(data, 50)
np.percentile(data, 75)
```

Quartiles are useful for detecting **outliers**.

---

## 9. Interquartile Range (IQR)

$$
IQR=Q3-Q1
$$

A common outlier rule is:

$$
x < Q1-1.5(IQR)
$$

or

$$
x > Q3+1.5(IQR)
$$

---

## 10. Covariance

Covariance measures how two variables change together.

$$
Cov(X,Y)=
E[(X-\mu_X)(Y-\mu_Y)]
$$

```python id="wkw8sf"
np.cov(x, y)
```

* Positive → Variables tend to increase together.
* Negative → One tends to increase as the other decreases.
* Near zero → Little linear co-movement.

---

## 11. Correlation

Correlation measures the **strength and direction of a linear relationship**.

$$
-1 \leq r \leq 1
$$

```python id="d8qgqk"
np.corrcoef(x, y)
```

Interpretation:

```text id="u6e2b4k"
 1  → Strong positive relationship
 0  → No linear relationship
-1  → Strong negative relationship
```

### Important

**Correlation does not imply causation.**

---

## 12. Probability Distributions

A distribution describes how values are spread across possible outcomes.

Common distributions:

| Distribution | Example                     |
| ------------ | --------------------------- |
| Normal       | Heights, measurement errors |
| Bernoulli    | Yes/No outcome              |
| Binomial     | Number of successes         |
| Poisson      | Number of events            |
| Uniform      | Equal probability           |

Normal distribution:

$$
X\sim N(\mu,\sigma^2)
$$

---

## 13. Sampling

Sampling means selecting observations from a population.

Common sampling methods:

* Random Sampling
* Stratified Sampling
* Systematic Sampling

Good sampling helps reduce **sampling bias**.

---

## 14. Central Limit Theorem

The **Central Limit Theorem (CLT)** states that, under suitable conditions, the distribution of sample means approaches a normal distribution as the sample size becomes sufficiently large, even when the original population is not normally distributed.

CLT is important for:

* Statistical inference
* Confidence intervals
* Hypothesis testing

---

## 15. Confidence Interval

A confidence interval provides a range of plausible values for a population parameter.

General form:

$$
Estimate \pm Margin\ of\ Error
$$

For example:

```text id="0fms4k"
Sample Mean = 50
95% CI = [47, 53]
```

The interval represents uncertainty in the estimated parameter.

---

## 16. Hypothesis Testing

Hypothesis testing helps determine whether there is enough statistical evidence to support a claim.

### Hypotheses

**Null Hypothesis (H₀)**
Represents the default assumption.

**Alternative Hypothesis (H₁)**
Represents the claim being tested.

### Common Tests

* t-test
* z-test
* Chi-square test
* ANOVA

---

## 17. P-Value

The p-value measures how compatible the observed data is with the null hypothesis.

A commonly used threshold is:

$$
\alpha = 0.05
$$

If:

$$
p < 0.05
$$

the result is often considered **statistically significant** under that chosen threshold.

A p-value does **not** represent the probability that the null hypothesis is true.

---

## 18. Skewness

Skewness measures the asymmetry of a distribution.

```text id="7nq7cc"
Positive Skew → Tail extends to the right
Negative Skew → Tail extends to the left
Zero          → Approximately symmetric
```

Skewness can affect data preprocessing and model performance.

---

## 19. Feature Scaling

Statistics is important for transforming features to comparable scales.

### Standardization

$$
z=\frac{x-\mu}{\sigma}
$$

This transforms data to approximately:

$$
Mean=0,\quad Standard\ Deviation=1
$$

```python id="9s2v8b"
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 20. Statistics in Machine Learning

| Statistical Concept       | ML Application         |
| ------------------------- | ---------------------- |
| Mean / Median             | Data Analysis          |
| Variance / Std. Dev.      | Feature Analysis       |
| Percentiles               | Outlier Detection      |
| IQR                       | Outlier Handling       |
| Covariance                | Feature Relationships  |
| Correlation               | Feature Selection      |
| Probability Distributions | Data Modeling          |
| Sampling                  | Dataset Creation       |
| Confidence Intervals      | Uncertainty            |
| Hypothesis Testing        | Statistical Validation |
| Standardization           | Feature Scaling        |

---

## Key Takeaway

Focus on this progression:

```text id="y4b2v0"
Population & Sample
       ↓
Mean / Median / Mode
       ↓
Variance / Standard Deviation
       ↓
Percentiles / Quartiles / IQR
       ↓
Covariance / Correlation
       ↓
Distributions
       ↓
Sampling & CLT
       ↓
Confidence Intervals
       ↓
Hypothesis Testing
       ↓
Feature Scaling & ML
```

### Useful Python Libraries

```python id="w8tqpj"
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
```

* **NumPy** → Numerical/statistical calculations
* **Pandas** → Data analysis
* **SciPy** → Statistical tests and distributions
* **Matplotlib** → Statistical visualization
