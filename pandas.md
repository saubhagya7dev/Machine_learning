# Pandas Cheat Sheet — Quick Revision for AI/ML

> Organized basic → advanced. Sections marked **[ML]** are the ones you'll use constantly in real AI/ML preprocessing/EDA work.

```python
import pandas as pd
import numpy as np
```

---

## 1. Creating Data
```python
pd.Series([1, 2, 3], index=["a", "b", "c"])
pd.DataFrame({"a": [1, 2], "b": [3, 4]})
pd.DataFrame(np.random.randn(5, 3), columns=["x", "y", "z"])
```

## 2. Reading & Writing Data (I/O) **[ML]**
```python
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")
df = pd.read_json("file.json")
df = pd.read_parquet(
    "file.parquet"
)  # fast columnar format, common for large ML datasets
df = pd.read_sql(query, conn)

df.to_csv("out.csv", index=False)
df.to_parquet("out.parquet")
```

## 3. First Look at Data — EDA basics **[ML]**
```python
df.head()
df.tail()
df.shape
df.info()
df.describe()  # summary stats — always run this first
df.dtypes
df.columns
df.sample(5)
df["col"].value_counts()  # frequency of categories
df.nunique()
df.isnull().sum()  # missing values per column
```

## 4. Selection & Indexing
```python
df["col"]  # single column -> Series
df[["col1", "col2"]]  # multiple columns -> DataFrame
df.loc[row_label, col_label]  # label-based
df.iloc[row_pos, col_pos]  # position-based
df.at[row, "col"]  # fast single scalar (label)
df.iat[0, 0]  # fast single scalar (position)
```

## 5. Filtering / Boolean Indexing **[ML]**
```python
df[df["col"] > 5]
df[(df["a"] > 5) & (df["b"] < 10)]  # use & | ~, not and/or
df[df["col"].isin(["x", "y"])]
df[~df["col"].isin(["x"])]  # negate
df[df["col"].between(1, 10)]
df.query("age > 30 and salary < 50000")  # readable, often faster on big data
```

## 6. Handling Missing Data **[ML — critical]**
```python
df.isnull().sum()
df.dropna()  # drop rows with any NaN
df.dropna(axis=1)  # drop columns with NaN
df.fillna(0)
df.fillna(df.mean(numeric_only=True))  # mean imputation
df["col"].fillna(df["col"].median(), inplace=True)
df.fillna(method="ffill")  # forward fill — good for time series
df.interpolate()
```

## 7. Cleaning & Dtypes
```python
df.duplicated().sum()
df.drop_duplicates()
df.astype({"col": "int32"})  # convert / downcast dtype
df.rename(columns={"old": "new"})
df.drop(columns=["col"])
df.replace({"yes": 1, "no": 0})
df["col"] = df["col"].str.strip()
```

## 8. Applying Functions / Transformations **[ML]**
```python
df["col"].apply(func)
df.apply(func, axis=1)  # row-wise, slower — use only when needed
df["col"].map({"a": 1, "b": 2})  # element-wise mapping (Series)
df["new"] = df["a"] + df["b"]  # vectorized — ALWAYS prefer this over apply/loop
np.where(df["a"] > 0, "pos", "neg")
```
**Rule of thumb:** vectorized ops > `.apply()` > Python loops, for speed on large datasets.

## 9. GroupBy & Aggregation — feature engineering workhorse **[ML]**
```python
df.groupby("cat")["value"].mean()
df.groupby("cat").agg({"value": ["mean", "sum", "count"]})
df.groupby(["cat1", "cat2"]).size()
df.groupby("cat")["value"].transform("mean")  # broadcast group stat back to each row
df.groupby("cat").filter(lambda x: len(x) > 5)
df.pivot_table(values="sales", index="region", columns="month", aggfunc="sum")
```

## 10. Merging / Joining / Concatenating **[ML]**
```python
pd.merge(df1, df2, on="id", how="inner")  # how: inner/left/right/outer
pd.merge(df1, df2, left_on="a", right_on="b")
df1.join(df2, how="left")  # index-based join
pd.concat([df1, df2], axis=0)  # stack rows
pd.concat([df1, df2], axis=1)  # stack columns
```

## 11. Reshaping Data
```python
df.pivot(index="date", columns="category", values="value")
df.melt(id_vars=["id"], value_vars=["a", "b"])  # wide -> long
df.stack()
df.unstack()
df.T
```

## 12. String Operations — text preprocessing **[ML]**
```python
df["col"].str.lower()
df["col"].str.contains("pattern")
df["col"].str.replace("a", "b")
df["col"].str.split(" ")
df["col"].str.strip()
df["col"].str.len()
df["col"].str.extract(r"(\d+)")  # regex extraction
```

## 13. DateTime Operations — time-series features **[ML]**
```python
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["weekday"] = df["date"].dt.dayofweek
df.set_index("date").resample("M").mean()  # downsample (monthly avg)
df["date"].diff()
```

## 14. Feature Engineering for ML **[ML — high value]**
```python
pd.get_dummies(df, columns=["category"])  # one-hot encoding
df["col"].factorize()  # simple label encoding
pd.cut(
    df["age"], bins=[0, 18, 35, 60, 100], labels=["teen", "young", "mid", "senior"]
)  # equal-width binning
pd.qcut(df["score"], q=4)  # quantile-based binning
(df["col"] - df["col"].mean()) / df["col"].std()  # manual standardization
df.corr()  # correlation matrix
df.corr(numeric_only=True)["target"].sort_values(ascending=False)  # corr with target
```

## 15. Sorting & Ranking
```python
df.sort_values("col", ascending=False)
df.sort_values(["a", "b"], ascending=[True, False])
df.rank()
df.nlargest(5, "col")
df.nsmallest(5, "col")
```

## 16. Sampling / Train-Test Style Split
```python
train = df.sample(frac=0.8, random_state=42)
test = df.drop(train.index)
```
(For real ML work, prefer `sklearn.model_selection.train_test_split` — this is just a quick pandas-only version.)

## 17. Performance & Memory Optimization **[ML — large datasets]**
```python
df.memory_usage(deep=True)
df["col"] = df["col"].astype("category")  # big memory savings on repeated strings
df.select_dtypes(include="number")
pd.eval("df.a + df.b")  # faster arithmetic on large df
df.query("a > 5")  # faster filtering than boolean mask on big data
```

## 18. Bridging to NumPy / ML Libraries **[ML]**
```python
df.to_numpy()  # preferred over df.values
X = df.drop("target", axis=1).to_numpy()
y = df["target"].to_numpy()
```

## 19. MultiIndex Basics
```python
df.set_index(["a", "b"])
df.xs("value", level="a")
df.reset_index()
```

---

## Quick-Glance: Most-Used Functions in AI/ML Work

| Function | Purpose |
|---|---|
| `read_csv/read_parquet` | Load dataset |
| `info()`, `describe()`, `isnull().sum()` | First-pass EDA |
| `value_counts()` | Check class balance / category frequency |
| `dropna()`, `fillna()` | Handle missing data |
| `astype()` | Fix/optimize dtypes |
| `groupby().agg()/.transform()` | Aggregate features per group |
| `merge()`, `concat()` | Combine datasets |
| `get_dummies()`, `factorize()` | Encode categorical variables |
| `cut()`, `qcut()` | Bin continuous variables |
| `corr()` | Feature relationships / selection |
| `apply()` vs vectorized ops | Custom transforms (vectorize when possible) |
| `to_datetime()` + `.dt` | Time-series feature extraction |
| `to_numpy()` | Hand data off to sklearn/torch/tf |
| `astype('category')` | Memory optimization on large data |

## Golden Rules
- **Vectorize, don't loop.** `.apply()` and Python `for` loops are last resorts.
- **Always check `isnull().sum()` and `dtypes` before modeling.**
- **Use `category` dtype** for low-cardinality string columns — huge memory win.
- **`.loc` for labels, `.iloc` for positions** — don't mix them up.
- **`corr()` before feature selection**, especially for quick baseline models.
- Chain operations when readable: `df.dropna().groupby('cat').mean().sort_values('val')`.