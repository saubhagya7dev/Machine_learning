### **Artificial Intelligence (AI)**, **Machine Learning (ML)**, and **Deep Learning (DL)** are nested concepts. The easiest way to visualize their relationship is as a set of concentric circles: AI is the outermost umbrella, ML is a subset within AI, and DL is a deeper subset within ML.


## 1. Artificial Intelligence (AI)

AI is the broadest discipline aimed at creating machines or systems capable of mimicking human intelligence to perform complex tasks, make decisions, or solve problems.

* **Core Objective:** To simulate human cognitive functions (like learning, reasoning, and problem-solving).
* **Historical Approach (Symbolic AI):** Early AI heavily relied on **Expert Systems** or rule-based logic [03:15](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=195). Human experts programmed explicit "if-then" rules into software.
* **Limitation:** While highly functional for structured, closed problems like playing chess [03:36](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=216), symbolic AI fails when faced with "fuzzy logic" or highly variable real-world scenarios—such as recognizing a dog in a photo, where rigid rules cannot easily capture every visual variation [04:10](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=250).



## 2. Machine Learning (ML)

Machine Learning is a subset of AI that moves away from explicit rule-based programming. Instead, it uses statistical methods to enable computers to find underlying patterns and learn directly from data [05:09](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=309).

* **Core Shift:** Instead of manually writing the code or rules, you input **Data + Expected Outputs** into the system, and the algorithm mathematically deduces the rules or patterns itself [05:39](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=339).
* **How it Works:** If you want an ML model to identify a dog, you feed it thousands of diverse dog images. The system learns the mathematical patterns common among those photos [06:34](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=394).
* **Limitation (Feature Engineering):** Traditional ML requires human engineers to explicitly define and extract features from the data before feeding it to the algorithm [10:33](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=633). For instance, to classify images, a human might have to pre-define visual metrics like ear shapes, snout length, or textures to help the model learn [10:44](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=644).



## 3. Deep Learning (DL)

Deep Learning is a specialized subfield of Machine Learning that is structurally inspired by the interconnected layout of biological neurons in the human brain, though it fundamentally functions as a dense mathematical stack [09:33](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=573).

* **Core Mechanics:** DL relies on **Artificial Neural Networks (ANNs)** with many layers (hence the term "Deep") [09:53](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=593).
* **The Key Breakthrough (Automatic Feature Extraction):** Unlike traditional ML, Deep Learning completely eliminates the need for manual feature engineering [11:14](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=674). You feed raw data (like an image) directly into the neural network, and successive layers automatically detect lower-level features (like edges and curves) and combine them into higher-level features (like eyes, nose, or a full face) [12:14](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=734).
* **Data Dependency:** Deep Learning models thrive on massive datasets. While traditional ML models tend to hit a performance plateau even if you feed them more data, DL performance continuously scales upward as data volume expands [13:33](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=813).

<br>
<br>

## Quick Comparison Summary

| Attribute | Artificial Intelligence (AI) | Machine Learning (ML) | Deep Learning (DL) |
| --- | --- | --- | --- |
| **Scope** | Entire universe of making machines intelligent. | Subset of AI focused on learning from data. | Subset of ML utilizing deep neural networks. |
| **Human Intervention** | High (in early symbolic AI) to define every logic path. | Medium; requires humans to extract data features. | Low; extracts data features automatically. |
| **Data Requirement** | Can function on minimal data (rule-based). | Performs well on small-to-medium datasets. | Requires massive amounts of data to excel. |
| **Ideal For** | Broad system logic, strategy games, general automation. | Structured tabular data, banking, insurance analytics [15:04](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=904). | Complex unstructured data (Computer Vision, NLP). |


<br>
<br>


# Types of Machine Learning 

## There are 4 Types of Machine Learning

Based on how much external human supervision the system receives during training, ML is split into four paths:

* **1. Supervised Learning (Labeled Data):** The model is trained on a dataset containing both inputs and correct output answers.
    * **Regression:** Predicts a continuous numerical value (e.g., house prices).
    * **Classification:** Predicts a categorical group or discrete class (e.g., "Spam" vs. "Not Spam").


* **2. Unsupervised Learning (Unlabeled Data):** The dataset contains only inputs with no pre-defined answers. The model mines for hidden structures:
    * **Clustering:** Groups similar data points together (e.g., customer segments).
    * **Dimensionality Reduction:** Compresses many data columns down into fewer, key dimensions.
    * **Anomaly Detection:** Flags rare data deviations (e.g., credit card fraud).
    * **Association Learning:** uncovers item co-occurrences (e.g., supermarket product placement).


* **3. Semi-Supervised Learning (Mixed Data):** Combines a small amount of expensive labeled data with a massive pile of unlabeled data.
    * *Example:* **Google Photos** groups visually similar faces automatically (unsupervised) and labels the entire group once you provide a single name (supervised).


* **4. Reinforcement Learning (Trial & Error):** No initial training data is provided. An autonomous **Agent** interacts with an **Environment** and learns to optimize its choices by collecting **Rewards** for correct moves and **Penalties** for mistakes. Used in robotics and systems like AlphaGo.

![alt text](The-main-types-of-machine-learning-Main-approaches-include-classification-and-regression.webp)

<br>
<br>

# Offline Learning VS Online Learning

## Batch Learning (Offline Learning)
### 1. Definitions

* **Production Environment:** The real-world server where your final code runs and interacts with actual customers `[00:01:22]`.
* **Batch Learning (Offline Learning):** A conventional approach where a machine learning model is trained using the entire dataset all at once, rather than in continuous, incremental steps `[00:02:17]`.

---

### 2. Workflow & Core Concept

* **Offline Training:** Because training on a massive dataset is computationally heavy and slow, it is done offline by engineers on local machines or dedicated servers `[00:03:09]`.
* **Static Model:** Once uploaded to the production server, the model becomes fixed. It uses what it has already learned to make predictions but cannot learn from new, incoming data on its own `[00:04:40]`.
* **Periodic Updates:** To prevent the model from becoming obsolete (e.g., a movie recommendation engine missing newly released films), developers must periodically combine old data with new data and retrain a brand-new model from scratch (e.g., every 24 hours, weekly, or monthly) `[00:05:58]`.

---

### 3. Main Disadvantages

* **Hardware & Scaling Bottlenecks:** As data grows exponentially over time, retraining a model on the *entire* dataset at once can eventually overwhelm system memory and crash your hardware `[00:07:45]`.
* **Connectivity Issues:** It fails in environments with limited or no internet access (e.g., remote locations, tracking satellites), where you cannot easily push frequent server updates `[00:08:23]`.
* **Slow Adaptation to Trends:** Because updates rely on a set schedule, the system cannot react to sudden real-time events or viral shifts instantly. By the time the next batch update runs, the trend may already be irrelevant `[00:09:39]`.

![alt text](1_DmOcKlevCbcNd4n4JBYtzQ.png)