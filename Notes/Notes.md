### **Artificial Intelligence (AI)**, **Machine Learning (ML)**, and **Deep Learning (DL)** are nested concepts. The easiest way to visualize their relationship is as a set of concentric circles: AI is the outermost umbrella, ML is a subset within AI, and DL is a deeper subset within ML.

# **DAY 1**
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

# **DAY 2**

## Quick Comparison Summary

| Attribute | Artificial Intelligence (AI) | Machine Learning (ML) | Deep Learning (DL) |
| --- | --- | --- | --- |
| **Scope** | Entire universe of making machines intelligent. | Subset of AI focused on learning from data. | Subset of ML utilizing deep neural networks. |
| **Human Intervention** | High (in early symbolic AI) to define every logic path. | Medium; requires humans to extract data features. | Low; extracts data features automatically. |
| **Data Requirement** | Can function on minimal data (rule-based). | Performs well on small-to-medium datasets. | Requires massive amounts of data to excel. |
| **Ideal For** | Broad system logic, strategy games, general automation. | Structured tabular data, banking, insurance analytics [15:04](http://www.youtube.com/watch?v=1v3_AQ26jZ0&t=904). | Complex unstructured data (Computer Vision, NLP). |


<br>
<br>

# **DAY 3**

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

# **DAY 4**

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
<br>
<br>

# **DAY 5**

## Online learning

This lecture by [CampusX](http://www.youtube.com/watch?v=3oOipgCbLIk) covers the concept of **Online Machine Learning**, contrasting it with Batch (Offline) Learning, exploring its applications, implementation strategies, and associated risks.

Here is a summary of the key definitions and key points to remember from the lecture, with timestamps removed:

---

### 1. Definition

* **Online Machine Learning** is an incremental learning technique where a model is trained sequentially as data arrives, rather than all at once.
* Instead of retraining the whole model on the entire dataset (which is computationally expensive), the model updates its weights dynamically on the server or in production using small streams or chunks of data called **mini-batches**.

### 2. When to Use Online Learning

You should opt for Online Learning under the following scenarios:

* **Concept Drift:** When the nature of the problem or underlying data patterns change dynamically over time (e.g., changing consumer behavior on e-commerce platforms during a festive sale).
* **Cost Efficiency:** Retraining massive datasets using batch learning repeatedly is incredibly expensive. Online learning processes data in tiny chunks, reducing computation overhead.
* **Fast / Dynamic Solutions:** When the application demands real-time responsiveness to user interactions.
* **Out-of-Core Learning:** When you have a massive dataset (e.g., $50\text{ GB}$) that exceeds your system's memory capacity (e.g., $8\text{ GB}$ RAM). Online learning allows you to load and train on small chunks sequentially.

### 3. Real-World Examples

* **Smart Keyboards (e.g., SwiftKey):** Adapts and personalizes text predictions dynamically as you type.
* **Recommendation Feeds (e.g., YouTube):** If you click a specific video, your home feed updates with related content immediately upon returning to the home screen.
* **AI Assistants / Chatbots:** Continuous learning from live user queries to optimize conversational accuracy.

### 4. Implementation Tools & Code Logic

* **Scikit-Learn (`partial_fit`):** Standard batch algorithms use `.fit()`. However, Online Learning algorithms like `SGDRegressor` use the `.partial_fit()` method, which allows you to continually pass fresh data and update the existing model state incrementally without losing prior learning.
* **Dedicated Streaming Libraries:** Libraries like [River](https://github.com/online-ml/river) (a Python library explicitly built for streaming data) and **Vowpal Wabbit** are excellent industry choices for complex online learning tasks.

---

### 💡 Key Points to Remember

> ⚠️ **The Learning Rate ($\eta$) Dilemma**
> Setting the correct learning rate is the hardest part of online learning.
> * If it is **too fast**, the model suffers from catastrophic forgetting (it learns new data too fast and completely forgets old patterns).
> * If it is **too slow**, the model reacts poorly to live trend changes.
> 
> 

> 🛡️ **Security and Data Poisoning Risk**
> Because the model learns continuously from incoming server data, it is vulnerable to malicious data injections or server anomalies. If garbage or biased data is fed into the pipeline, the model's behavior will quickly decay.
> * *Fix:* You **must** build automated anomaly detection layers to screen live data, closely monitor performance, and have a rollback strategy to revert the model to a previous stable state if it misbehaves.
> 
> 

---

### Comparison Summary: Online vs. Offline (Batch) Learning

| Feature | Offline / Batch Learning | Online Learning |
| --- | --- | --- |
| **Data Processing** | Processes data all at once in a bulk dataset. | Processes data continuously and incrementally . |
| **System Complexity** | Lower complexity; trained offline and deployed to only make predictions. | Higher complexity; must continually learn, predict, and be monitored live. |
| **Best Suited For** | Static data where patterns don't change frequently (e.g., Cat vs. Dog classifier). | Volatile environments with fluctuating trends (e.g., Stock prediction, live recommendation systems). |

<br>
<br>

# **DAY 6**

# Instance-Based Vs Model-Based Learning
![alt text](1_esVJb_A1pD8FL4Ol4N7nCw@2x.jpg)
## Core Overview

The lecture focuses on how different Machine Learning (ML) algorithms learn from data. Just like humans learn either by **memorization (rote learning)** or **generalization (understanding the concept)**, machine learning models fall into two primary categories based on their learning approach: **Instance-Based Learning** and **Model-Based Learning**.



## 1. Instance-Based Learning

```
[ Training Data ] 
       │
       ▼  (Stored directly into memory without changes)
[ Database / Storage ] 
       │
       ├─◄─ [ New Query Instance ] (An unseen data point arrives)
       ▼
[ Similarity / Distance Measure ] (e.g., calculates closest neighbors)
       │
       ▼
[ Prediction / Output ] (Based on majority vote or average of neighbors)

```

### Brief Definition

Instance-Based Learning is an approach where the system learns the training examples by heart (memorization) and generalizes to new instances on-the-fly based on a similarity measure (e.g., distance). It is also famously referred to as **Lazy Learning** because the model does no real work during the training phase.

### Key Points :

* **No Explicit Training Phase:** The algorithm does not construct an abstract model or rule during training; it simply stores the raw training data as-is.
* **Similarity-Driven:** When a new query point is introduced, the algorithm calculates its similarity or distance (e.g., Euclidean distance) to all stored data points to predict the outcome.
* **Example Given:** **K-Nearest Neighbors (KNN)** is a classic example. If a new student's data is plotted, the algorithm looks at the closest neighbors to determine whether the student will get placed or not based on majority voting.

---

## 2. Model-Based Learning

### Phase 1: Training Phase

```
[ Training Data ] ──► [ Learning Algorithm ] ──► [ Optimized Parameters / Model Formula ]

```

### Phase 2: Prediction Phase

```
[ New Query Instance ] ──► [ Optimized Model Formula ] ──► [ Prediction / Output ]

``` 


### Brief Definition

Model-Based Learning is an approach where the system tries to extract an underlying pattern, rule, or concept from the training data to build a predictive mathematical function (or decision boundary).

### Key Points :

* **Builds a Decision Boundary:** Instead of keeping the data points, the algorithm optimizes a set of mathematical parameters to draw a permanent boundary separating classes.
* **Data-Independent Post Training:** Once the mathematical function (model) is built and saved, the training data can be completely deleted. Predictions depend entirely on the calculated formula.
* **Examples Given:** Linear Regression, Logistic Regression, and Decision Trees are primary examples where relationships are reduced to equations or structured rules.


## Key Differences Summary

The lecture concludes with a direct comparison between the two approaches across several critical performance metrics:

| Metric / Feature | Model-Based Learning | Instance-Based Learning |
| --- | --- | --- |
| **Primary Mechanism** | Extracts a generalized rule or formula. | Memorizes and holds onto individual instances. |
| **Data Dependency** | Training data can be discarded after the model is trained. | Training data **must** be kept indefinitely to make predictions. |
| **When Generalization Happens** | Before scoring; creates a global rule for all future incoming data. | Only at the moment of scoring; local rules adapt uniquely per query point. |
| **Storage Requirements** | **Low Storage:** Only saves a few parameters or equations. | **High Storage:** Needs memory proportional to the size of the entire dataset. |
| **Computation Speed** | Slow training phase, but extremely fast prediction phase. | No training phase (instant), but slower prediction phase due to distance calculations. |



### Key Structural Difference

* **Instance-Based:** $\text{New Data} \longrightarrow \text{All Training Data} \longrightarrow \text{Output}$
* **Model-Based:** $\text{New Data} \longrightarrow \text{Mathematical Formula} \longrightarrow \text{Output}$

<br>
<br>

# **DAY 7** 

# Challenges In Machine learning - 
![alt text](0_4fmJ7BUeXBTiz42U.png)

### 1. Data Collection

* **Definition:** The process of gathering raw data from various sources (e.g., APIs, databases, web scraping) to train machine learning models.
* **Keypoints:** While working on educational or small-scale hobby projects provides easily accessible datasets (like CSV files on Kaggle), collecting data for production-level industry applications is highly difficult.

### 2. Insufficient Data & Labeled Data

* **Definition:** The bottleneck where a model lacks enough overall training examples or struggles because the collected data lacks correct target tags/labels.
* **Keypoints:** Having massive amounts of data can sometimes make up for a weaker algorithm—a concept known as the *unreasonable effectiveness of data*. However, most real-world scenarios suffer from medium-to-low dataset sizes. Furthermore, manually labeling data (e.g., separating images of cats vs. dogs) is incredibly tedious and time-consuming.

### 3. Non-Representative Data

* **Definition:** A flaw occurring when the training data sample fails to accurately mirror the real-world distribution of the population the model is trying to make predictions on.
* **Keypoints:** If your training data only shows "half the story," your predictions will fail on new data. This manifests as **Sampling Noise** (unintentional variance from small samples) or **Sampling Bias** (systemic faults in sample selection, such as polling only cricket fans in India to see who will win the World Cup).

### 4. Poor Quality Data

* **Definition:** Datasets riddled with errors, outliers, noise, missing values, or inconsistent formatting.
* **Keypoints:** Machine learning is heavily dependent on data quality. In actual data science projects, practitioners spend nearly **60% to 80% of their total time** performing data cleaning and recycling raw, noisy data into clean formats.

### 5. Irrelevant Features (Garbage In, Garbage Out)

* **Definition:** Including variables or columns in a dataset that do not add any predictive value or relate to the target output.
* **Keypoints:** Feeding useless attributes (e.g., using a person's geographic location to predict their marathon running performance) actively degrades model performance. Engineers combat this through **Feature Engineering**—combining or transforming columns (example - like turning height and weight into BMI) to give the model better signals.

### 6. Overfitting

* **Definition:** A scenario where a machine learning model learns the training data too perfectly, essentially "memorizing" individual points rather than understanding the underlying patterns.
* **Keypoints:** Overfitted models yield exceptionally high accuracy on training sets but fail to generalize when exposed to unseen test data. The model treats noise as a core pattern, clinging too rigidly to specific data coordinates.

### 7. Underfitting

* **Definition:** The exact opposite of overfitting; occurs when a model is too simple to capture the structural trends inherent within the data.
* **Keypoints:** An underfitted model performs poorly on *both* the training data and new test data. Striking a balance between underfitting and overfitting is a primary objective when selecting model architectures.

![alt text](420046946.webp)

### 8. Software Integration

* **Definition:** The complex engineering task of taking an isolated machine learning model and embedding it natively into an existing production software environment.
* **Keypoints:** Models do not run in a vacuum; they must live inside apps, websites, or edge hardware. Compatibility issues across operating systems (Windows, Android, Linux) and popular development ecosystems make this highly challenging. Stable ML toolings for core backend frameworks like Java or Frontend JavaScript (e.g., TensorFlow.js) are still structurally maturing.

### 9. Offline Learning vs. Deployment

* **Definition:** The operational friction points of moving a model to a production server and managing updates.
* **Keypoints:** Many models rely on static offline learning (the model is trained once, deployed, and cannot adapt unless it is taken offline, retrained with new data, and redeployed). Deploying models through cloud services like AWS or Azure requires ongoing monitoring, which is still significantly less streamlined than traditional software deployment.

### 10. Cost Involved

* **Definition:** The financial overhead generated by computationally intensive model training, cloud compute infrastructure, and server data hosting.
* **Keypoints:** Running large-scale models at high user volumes scales cloud costs rapidly. Because of these hidden expenses, companies often limit what algorithms can be deployed. This intersection of managing deployment pipelines, costs, and infrastructure has given rise to the rapidly growing discipline of **MLOps (Machine Learning Operations)**.

<br>
<br>

# **DAY 8**

# Application of Machine Learning - 

The primary objective of this lecture is to shift the perspective from standard consumer-facing applications **(Business-to-Consumer or B2C**, like YouTube or Amazon recommendations) toward **Business-to-Business (B2B)** applications, showing how machine learning (ML) acts as a backbone for industry profitability, operations, and strategic decision-making.

## 1. Retail & E-Commerce

* **Demand Forecasting:** Predicting which products will trend before massive sales events so companies only stock high-demand items, saving millions in warehousing costs.
* **Customer Profiling:** Tracking purchasing behavior via customer phone numbers to build distinct lifestyle profiles (e.g., health-conscious) for highly targeted ad conversions.
* **Market Basket Analysis:** > **Definition:** Finding hidden co-relations between products based on what customers frequently buy together.
* **Keypoint:** This dictates physical shelf or digital layout optimization to trigger spontaneous cross-purchasing.




## 2. Banking and Finance

* **Credit Risk Assessment:** Running customer profiles through ML models to compare them against historical default data. If a high correlation to past defaulters is found, the system flags a risk and rejects the loan.
* **Expansion Strategy:** Analyzing demographic data to determine the most profitable locations to open new branches and launch localized financial products.


## 3. Transportation and Logistics

* **Dynamic / Surge Pricing:** > **Definition:** Adjusting the cost of a service in real-time based on immediate supply and demand metrics.
* **Keypoint:** When passenger demand outpaces available drivers, prices spike. This premium acts as a financial incentive to draw nearby drivers into high-demand areas.


* **Route Optimization:** Generating the most efficient multi-stop delivery routes to minimize fuel consumption and transit time.


## 4. Manufacturing Sector

* **Predictive Maintenance:** > **Definition:** Monitoring equipment metrics (like temperature and RPM) using IoT sensors to predict and fix machinery failures before they happen.
* **Keypoint:** Enables automated factories to repair critical robotic machinery during off-hours, entirely avoiding costly, unplanned production halts.



## 5. Consumer Internet & Sentiment Analysis

Platforms that harvest vast textual data leverage natural language processing to extract market intelligence.

* Sentiment Analysis:
    * **Definition** : The process of computationally identifying and categorizing opinions expressed in text to determine whether the user's attitude toward a specific topic is positive, negative, or neutral Opens in a new window.

    * **Real world example** : Public platforms like Twitter leverage sentiment tracking during major   global events (such as political elections or entertainment releases) By processing public sentiment, platforms can create a real-time repository of human intelligence that is highly valuable to stock brokers, hedge funds, and market researchers aiming to make predictive investments before official results drop.


<br>
<br>

# **DAY 9**

# Machine Learning Development Life Cycle - 

![alt text](machine_learning_lifecycle.webp)

# Machine Learning Lifecycle

## Step 1: Problem Definition
The first step is identifying and clearly defining the business problem. A well-framed problem provides the foundation for the entire lifecycle. Important things like project objectives, desired outcomes and the scope of the task are carefully designed during this stage.

* Collaborate with stakeholders to understand business goals
* Define project objectives, scope and success criteria
* Ensure clarity in desired outcomes

---

## Step 2: Data Collection
Data Collection phase involves systematic collection of datasets that can be used as raw data to train model. The quality and variety of data directly affect the model’s performance.

Here are some basic features of Data Collection:

* **Relevance:** Collect data should be relevant to the defined problem and include necessary features.
* **Quality:** Ensure data quality by considering factors like accuracy and ethical use.
* **Quantity:** Gather sufficient data volume to train a robust model.
* **Diversity:** Include diverse datasets to capture a broad range of scenarios and patterns.

---

## Step 3: Data Cleaning and Preprocessing
Raw data is often messy and unstructured and if we use this data directly to train then it can lead to poor accuracy. We need to do data cleaning and preprocessing which often involves:

* **Data Cleaning:** Address issues such as missing values, outliers and inconsistencies in the data.
* **Data Preprocessing:** Standardize formats, scale values and encode categorical variables for consistency.
* **Data Quality:** Ensure that the data is well-organized and prepared for meaningful analysis.

---

## Step 4: Exploratory Data Analysis (EDA)
To find patterns and characteristics hidden in the data Exploratory Data Analysis (EDA) is used to uncover insights and understand the dataset's structure. During EDA patterns, trends and insights are provided which may not be visible by naked eyes. This valuable insight can be used to make informed decision.

Here are the basic features of Exploratory Data Analysis:

* **Exploration:** Use statistical and visual tools to explore patterns in data.
* **Patterns and Trends:** Identify underlying patterns, trends and potential challenges within the dataset.
* **Insights:** Gain valuable insights for informed decisions making in later stages.
* **Decision Making:** Use EDA for feature engineering and model selection.

---

## Step 5: Feature Engineering and Selection
Feature engineering and selection is a transformative process that involve selecting only relevant features to enhance model efficiency and prediction while reducing complexity.

Here are the basic features of Feature Engineering and Selection:

* **Feature Engineering:** Create new features or transform existing ones to capture better patterns and relationships.
* **Feature Selection:** Identify subset of features that most significantly impact the model's performance.
* **Domain Expertise:** Use domain knowledge to engineer features that contribute meaningfully for prediction.
* **Optimization:** Balance set of features for accuracy while minimizing computational complexity.

---

## Step 6: Model Selection
For a good machine learning model, model selection is a very important part as we need to find model that aligns with our defined problem, nature of the data, complexity of problem and the desired outcomes.

Here are the basic features of Model Selection:

* **Complexity:** Consider the complexity of the problem and the nature of the data when choosing a model.
* **Decision Factors:** Evaluate factors like performance, interpretability and scalability when selecting a model.
* **Experimentation:** Experiment with different models to find the best fit for the problem.

---

## Step 7: Model Training
With the selected model the machine learning lifecycle moves to model training process. This process involves exposing model to historical data allowing it to learn patterns, relationships and dependencies within the dataset.

Here are the basic features of Model Training:

* **Iterative Process:** Train the model iteratively, adjusting parameters to minimize errors and enhance accuracy.
* **Optimization:** Fine-tune model to optimize its predictive capabilities.
* **Validation:** Rigorously train model to ensure accuracy to new unseen data.

---

## Step 8: Model Evaluation and Tuning
Model evaluation involves rigorous testing against validation or test datasets to test accuracy of model on new unseen data. It provides insights into model's strengths and weaknesses. If the model fails to acheive desired performance levels we may need to tune model again and adjust its hyperparameters to enhance predictive accuracy.

Here are the basic features of Model Evaluation and Tuning:

* **Evaluation Metrics:** Use metrics like accuracy, precision, recall and F1 score to evaluate model performance.
* **Strengths and Weaknesses:** Identify the strengths and weaknesses of the model through rigorous testing.
* **Iterative Improvement:** Initiate model tuning to adjust hyperparameters and enhance predictive accuracy.
* **Model Robustness:** Iterative tuning to achieve desired levels of model robustness and reliability.

---

## Step 9: Model Deployment
Now model is ready for deployment for real-world application. It involves integrating the predictive model with existing systems allowing business to use this for informed decision-making.

Here are the basic features of Model Deployment:

* Integrate with existing systems
* Enable decision-making using predictions
* Ensure deployment scalability and security
* Provide APIs or pipelines for production use

---

## Step 10: Model Monitoring and Maintenance
After Deployment models must be monitored to ensure they perform well over time. Regular tracking helps detect data drift, accuracy drops or changing patterns and retraining may be needed to keep the model reliable in real-world use.

Here are the basic features of Model Monitoring and Maintenance:

* Track model performance over time
* Detect data drift or concept drift
* Update and retrain the model when accuracy drops
* Maintain logs and alerts for real-time issues


<br>
<br>

# **DAY 10**


# Data Science and Machine learning JOB Roles -



## 📊 Updated Data Job Roles & Market Comparison (2026)

| Job Title | Analytical Skills | Business Acumen | Data Storytelling | Soft / Comm. Skills | Software Engg. / DSA | System Design / Cloud | **Average U.S. Base Salary (2026)** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Data Analyst** | High | Medium to High | **Very High** *(Crucial)* | Medium to High | Low | None | **$84,000 – $90,000** |
| **Data Engineer** | Medium | Low / Agnostic | None | Medium | **Very High** | **Very High** | **$137,000 – $185,000** |
| **Data Scientist** | **Very High** | High | High | High | Medium | Low to Medium | **$112,000 – $128,000** |
| **ML Engineer** | Medium to High | Medium | None | High | **Very High** | **Very High** | **$160,000 – $187,000** |

---

## 🔍 Key 2026 Market Context & Salary Factors

* **The ML/AI Premium:** [Machine Learning Engineers](https://www.kore1.com/ml-engineer-salary-guide/) command the highest baseline packages. Because companies are rushing to put AI systems into actual software production, the demand for people who understand LLMOps, model deployment, and distributed computing has outpaced the general talent supply. Total compensation (including equity and bonuses) for senior ML Engineers at top-tier companies regularly pushes past **$350,000**.
* **The Data Infrastructure Crux:** [Data Engineers](https://www.recruitingfromscratch.com/blog/data-engineer-salary-in-2026-real-data-from-200k-job-postings) continue to see incredibly stable, high compensation. Modern AI models are only as good as the data fed into them, meaning specialized "AI Data Engineers" who build real-time vector databases and low-latency streaming pipelines are highly valued.
* **Data Scientist Evolution:** The role of the generalist Data Scientist has split. Those working primarily on traditional statistical business modeling sit around the mid-$120k base mark. However, those specializing in deep learning, Computer Vision, or NLP frequently jump into the ML Engineer tier or higher.
* **Data Analyst Automation:** With modern AI tools drastically cutting down the manual time required to write SQL queries or clean data, [Data Analysts](https://builtin.com/salaries/us/data-analyst) are evaluated much more heavily on their **Business Intelligence (BI)** and **Data Storytelling** capabilities—translating data directly into revenue-generating strategies.

<br>
<br>

# **DAY 11**

# What are Tensors ?

* **Definition:** In its simplest form, a tensor is a **data structure** or a container used to store numbers. In computer science, it is synonymous with a multidimensional array ($N\text{-Dimensional Array}$).
* **Importance:** Leading machine learning libraries like Scikit-Learn, TensorFlow, and PyTorch rely on tensors as their most basic building block to store and process data. In fact, Google’s top deep learning library, *TensorFlow*, derives its name directly from this concept.
![alt text](64798tensor.jpg)
### **Types of Tensors and Practical Examples**

The number of dimensions a tensor has is referred to as its **Rank** or **Axis**. The video breaks down the types of tensors from 0D to 5D using real-world applications:

* **0D Tensor (Scalar):** A single number containing no axes (e.g., `7` or `45`). Checking its dimension in NumPy returns `0`.
* **1D Tensor (Vector):** An array or a single list of numbers with one axis.
    * *Machine Learning Example:* In a student dataset with columns like [CGPA, IQ, State], the input data for a **single student** forms a 1D tensor.


* **2D Tensor (Matrix):** A collection of vectors consisting of rows and columns (two axes).
    * *Machine Learning Example:* An **entire tabular dataset** where rows represent multiple individual records (e.g., data for 10,000 students) and columns represent features.


* **3D Tensor:** A collection of multiple 2D matrices layered together.
    * *Machine Learning Examples:* 
    1. **Natural Language Processing (NLP):** Text data converted into vectors where sentences form a matrix of word embeddings.
    2. **Time Series Data:** Stock market data tracked over a timeline (e.g., tracking stock highs and lows daily over a 10-year span).


* **4D Tensor:** A collection of multiple 3D tensors.
    * *Machine Learning Example:* **Image datasets**. A single color image is a 3D tensor consisting of rows, columns, and 3 color channels (RGB). A batch containing multiple color images forms a 4D tensor.


* **5D Tensor:** A collection of multiple 4D tensors.
    * *Machine Learning Example:* **Video data**. Videos are essentially sequences of image frames playing rapidly over time. When processing a batch of multiple videos (Videos × Frames × Height × Width × Channels), the data structure escalates into a 5D tensor.



---

### **Core Properties: Shape and Size**

* **Shape:** Dictates the exact number of elements available along each specific axis (e.g., a shape of `(2, 3)` means 2 rows and 3 columns).
* **Size:** The total count of individual numbers inside a tensor. This is calculated by multiplying all the dimensions of its shape together. For example, a tensor with a shape of `(4, 3, 2)` holds a total size of 24 items.

<br>
<br>

# **DAY 12**

### it was all about setting up Anaconda for data science and kaggle for datasets retrival

# **DAY 13**

### made an End to End machine learning project to get an overview of what an actual process looks like to build an ML model from Scratch to Deployment

# **DAY 14**

# Framing Business problem to ML Problem 

## How to Frame a Machine Learning Problem Effectively

This project guide outlines a systematic, 7-step framework for planning a Data Science project and converting a real-world business problem into a structured Machine Learning (ML) problem. 

To illustrate the workflow, a practical case study of **Netflix Churn Rate Optimization** is used throughout the steps.

---

## The Core Philosophy
To grow into a senior data scientist or leadership role, you cannot simply jump straight into writing code. Spending significant time upfront mapping out the problem architecture, planning data flows, and structuring the ML approach is the most critical skill for project su ccess.

---

## The 7-Step Problem Framing Framework

### 1. Business Problem to ML Problem (Mathematical Problem)
* **The Business Problem:** Netflix wants to increase its overall revenue.
* **The ML Formulation:** Instead of spending heavily on acquiring new users, the strategy shifts to retaining existing users who are about to leave (reducing the churn rate). The broad business objective is converted into a concrete mathematical target: reducing the churn rate from 4% to 3.75%.

### 2. Identifying the Type of Problem
* While it initially looks like a binary classification problem (Will the user leave? Yes/No), framing it as a **Regression problem** offers a better business solution. 
* By predicting a precise probability score (0 to 100%) of how likely a user is to leave, the business can offer dynamically customized discount rates depending on their exact likelihood of churning.

### 3. Reviewing Existing Solutions
* Before starting from scratch, always check if an existing baseline model or framework is already built within the organization. 
* Reviewing past work helps gather inspiration, understand previously considered factors, and avoids wasting time reinventing the wheel.

### 4. Identifying and Gathering Data
* To predict user churn, you must identify relevant, measurable features. Key user behavior indicators include:
  * Total watch time vs. browsing time.
  * Search failures (how often a user searches for a title but doesn't find it).
  * Completion rates (how frequently they stop a movie or show halfway through).
* This step requires close collaboration with **Data Engineers** to extract these metrics from production databases and set up a structured data warehouse.

### 5. Defining Success Metrics
* You must define clear mathematical metrics to evaluate the model's success. 
* This involves tracking the difference between your predicted churn probabilities and actual user churn over time. These metrics act as a "North Star" guiding the entire project team.

### 6. Online vs. Batch Learning
* **Online Learning:** The model continuously updates and learns on-the-go as live user data flows in. This is ideal for highly volatile data like streaming behavior.
* **Batch Learning (Fallback):** If continuous online training is technically too complex or resource-heavy, a viable alternative is to train the model offline in batches (e.g., once every week) and deploy the updated version regularly.

### 7. Validating Key Assumptions
* Before deploying a model globally, you must rigorously test your core assumptions:
  * Are the intended data features actually logged and available in the database?
  * Will a model trained on data from users in one region (e.g., the US) perform equally well for users in another region (e.g., India), or does it require localized adjustments?


<br>
<br>

# **DAY 15**

## Data Gathering processes - 
1. Csv Files 
2. Jason/SQL Files 
3. Fetch API 
4. WEB Scraping


## Working With CSV FILES 

### 1. Loading CSV Data (Local & Remote)

You can load a CSV file directly from your local machine, or download and parse it directly from a web server URL using the `requests` library.

* **Local:** Pass the relative or absolute file path.
* **URL:** Fetch the text content using an API request and stream it into Pandas.

```python
import pandas as pd
import requests
import io

# A. Loading locally [00:07:52]
df_local = pd.read_csv('aug_train.csv')

# B. Loading from a Server URL [00:08:33]
url = "https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day15%20-%20working%20with%20csv%20files/aug_train.csv"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
df_url = pd.read_csv(io.StringIO(response.text))

```

---

### 2. TSV FIELS - Handling Separators & Custom Column Names

By default, `pd.read_csv()` looks for commas. If your data is Tab-Separated (`.tsv`) or uses a different delimiter, use the `sep` parameter. If the file lacks a header row, pass custom column names using `names` to prevent the first row of data from becoming the header [10:34](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=634).

```python
# Reading a TSV file and manually providing column names [00:11:34]
column_names = ['serial_no', 'movie_name', 'release_year', 'rating', 'votes', 'genres']
df_tsv = pd.read_csv('movie_titles_metadata.tsv', sep='\t', names=column_names)

```

---

### 3. Setting Index and Handling Misaligned Headers

* **`index_col`:** Convert an existing data column (like an ID) into the row index [13:40](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=820).
* **`header`:** If a file contains blank rows or metadata at the top before the actual columns start, tell Pandas exactly which row to treat as the header [14:35](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=875).

```python
# Convert 'enrollee_id' column to index [00:14:10]
df_index = pd.read_csv('aug_train.csv', index_col='enrollee_id')

# Specify that row 1 (instead of 0) contains the actual column names [00:15:13]
df_header = pd.read_csv('test.csv', header=1)

```

---

### 4. Memory Optimization (Selecting Specific Columns & Rows)

When handling large datasets, loading every single column or millions of rows wastes RAM.

* **`usecols`:** Only loads specified columns into memory [15:53](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=953).
* **`nrows`:** Limits the total number of rows imported [19:55](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=1195).
* **`skiprows`:** Skips specific row numbers or takes a custom filtering function [17:58](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=1078).

```python
# Select only 3 specific columns [00:16:26]
df_cols = pd.read_csv('aug_train.csv', usecols=['enrollee_id', 'gender', 'education_level'])

# Limit import to the first 100 rows [00:20:02]
df_rows = pd.read_csv('aug_train.csv', nrows=100)

# Skip rows by index or custom rule [00:18:22]
df_skipped = pd.read_csv('aug_train.csv', skiprows=[0, 2]) # skips row 0 and 2

```

---

### 5. Fixing Encoding & Parsing Errors

* **`encoding`:** If your data contains emojis or non-standard characters, it will throw a `UnicodeDecodeError`. Overriding the default `utf-8` encoding with formats like `latin-1` usually resolves it [20:47](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=1247).
* **`on_bad_lines`:** If some rows contain malformed data (e.g., 9 commas instead of 8), Pandas will crash. Setting this parameter skips those broken lines entirely [22:55](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=1375).

```python
# Fix encoding issues with 'latin-1' [00:22:18]
df_encoded = pd.read_csv('zomato.csv', encoding='latin-1')

# Skip malformed/broken lines instead of crashing [00:24:05]
df_cleaned = pd.read_csv('books.csv', sep=';', encoding='latin-1', on_bad_lines='skip')

```

---

### 6. Managing Datatypes, Custom Conversions, & Dates

* **`dtype`:** Cast column data types during the import step to save memory (e.g., converting a float to an integer) [24:45](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=1485).
* **`parse_dates`:** Ensures date columns are read as real datetime objects instead of flat strings [26:41](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=1601).
* **`converters`:** Allows you to instantly apply a custom python function to transform a column's values on the fly [29:30](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=1770).

```python
# 1. Force a datatype conversion [00:26:03]
df_dtype = pd.read_csv('aug_train.csv', dtype={'target': int})

# 2. Automatically parse columns into datetime objects [00:27:44]
df_dates = pd.read_csv('IPL Matches 2008-2020.csv', parse_dates=['date'])

# 3. Transform column values on import using a converter function [00:31:06]
def short_team_name(name):
    if name == "Royal Challenge Bangalore":
        return "RCB"
    return name

df_converted = pd.read_csv('IPL Matches 2008-2020.csv', converters={'team1': short_team_name})

```

---

### 7. Custom Null Values & Chunking Massive Datasets

* **`na_values`:** If your dataset uses unique placeholders for missing values (like hyphens `-` or specific text strings) that Pandas doesn't recognize natively, pass them into a list to explicitly treat them as `NaN` values [31:39](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=1899).
* **`chunksize`:** For massive datasets that exceed your computer's RAM, you can load your CSV iteratively in blocks (chunks) using a loop [33:39](http://www.youtube.com/watch?v=a_XrmKlaGTs&t=2019).

## Summary 

Here is a ultra-brief summary of the most common CSV techniques in Pandas, mapping the code directly to how it works:

### 1. Basic Ingestion

* **Code:** `df = pd.read_csv('file.csv')`
* **Working:** Loads a standard comma-separated file into a DataFrame.

### 2. Custom Delimiter

* **Code:** `df = pd.read_csv('file.tsv', sep='\t')`
* **Working:** Handles non-comma files (like tab `\t` or semicolon `;` separated data).

### 3. Column Selection (Memory Saving)

* **Code:** `df = pd.read_csv('file.csv', usecols=['Age', 'Salary'])`
* **Working:** Only loads specified columns into RAM, ignoring the rest.

### 4. Row Limitation (Quick Testing)

* **Code:** `df = pd.read_csv('file.csv', nrows=100)`
* **Working:** Restricts the import to the first $N$ rows ($N=100$ here) to quickly inspect large datasets.

### 5. Fixing Special Characters

* **Code:** `df = pd.read_csv('file.csv', encoding='latin-1')`
* **Working:** Prevents crashes (`UnicodeDecodeError`) when files contain emojis or non-standard characters.

### 6. Correcting Datatypes

* **Code:** `df = pd.read_csv('file.csv', dtype={'ID': int})`
* **Working:** Forces Pandas to interpret a specific column as a chosen datatype on import.

### 7. Native Date Parsing

* **Code:** `df = pd.read_csv('file.csv', parse_dates=['Date_Column'])`
* **Working:** Automatically converts flat text/strings into true Python datetime objects.

### 8. Processing Massive Files (Chunking)

* **Code:** ```python
for chunk in 
`pd.read_csv('huge.csv', chunksize=5000):`
process(chunk)


* **Working:** Breaks down files larger than your computer's RAM into manageable slices ($5000$ rows each) to loop through them sequentially.

<br>
<br>


# **DAY 16**


## Working with JSON/SQL files 

Here is a very brief summary of the core techniques used to process JSON and SQL data for machine learning workflows:

### 1. Handling JSON Files (Semi-Structured Data)

JSON is widely used for web APIs and nested data. The main challenge in ML is that it isn’t flat like a spreadsheet.

* **Direct Parsing:** Using Pandas (`pd.read_json()`) to instantly convert simple, flat JSON arrays into DataFrames.
* **Flattening / Normalization:** Real-world JSON often contains nested dictionaries or lists. Techniques like `pd.json_normalize()` are used to unpack these hierarchies into a flat tabular format (rows and columns) that ML algorithms can read.
* **Chunking:** For massive JSON files that cause memory errors, the data is streamed or read in batches using the `chunksize` parameter.

### 2. Handling SQL Files (Structured Relational Data)

Relational databases store structured, enterprise-level data. The goal is to safely query and extract exactly what you need.

* **Database Connectors:** Establishing a secure bridge between Python and the database engine using dedicated libraries (e.g., `mysql-connector-python`, `psycopg2` for PostgreSQL, or `sqlite3`).
* **In-Memory Querying:** Using Pandas (`pd.read_sql_query()`) to execute standard SQL commands directly inside Python. This allows you to filter (`WHERE`), aggregate (`GROUP BY`), or join tables *before* bringing the data into memory.
* **Batch Processing:** Like JSON, if a SQL table contains millions of rows, data scientists pull data sequentially in chunks or use specialized big-data frameworks (like PySpark) to prevent system crashes.
<br>
<br>

# **DAY 17**


To implement this workflow, you need the standard built-in `requests` library to manage HTTP handshakes and `pandas` for structural data wrangling.

### Step 1: Fetching and Structuring a Single Page of Data

Before scaling up with a loop, test your setup by pulling the first batch (Page 1) of top-rated movies [09:25](http://www.youtube.com/watch?v=roTZJaxjnJc&t=565):

```python
import pandas as pd
import requests

# Set your target API endpoint and append your personal TMDb API key
# Replace 'YOUR_API_KEY_HERE' with your real API credential from TMDb
api_key = "YOUR_API_KEY_HERE"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1"

# Step A: Perform an HTTP GET request to pull the data
response = requests.get(url)

# Step B: Parse the incoming text directly into JSON/Python Dictionary format
data_json = response.json()

# Step C: Isolate the nested list under 'results' and wrap it into a DataFrame
df_page1 = pd.DataFrame(data_json["results"])[
    [
        "id",
        "title",
        "release_date",
        "overview",
        "popularity",
        "vote_average",
        "vote_count",
    ]
]

# Quick check on the structural shape of your targeted DataFrame
print(df_page1.head())

```

---

### Step 2: Full Scaled Automation (Looping Over All Pages)

Once the single-page logic runs successfully, implement a robust loop that walks across all 428 structural data pages from the TMDb server [11:34](http://www.youtube.com/watch?v=roTZJaxjnJc&t=694), [17:13](http://www.youtube.com/watch?v=roTZJaxjnJc&t=1033). This compiles a unified master dataframe comprising over 8,500 movies [19:38](http://www.youtube.com/watch?v=roTZJaxjnJc&t=1178):

```python
import pandas as pd
import requests

api_key = "YOUR_API_KEY_HERE"

# Initialize an empty master DataFrame to house your incoming datasets
master_df = pd.DataFrame()

# TMDb features 428 total pages of top-rated items.
# We loop from 1 to 428 (remember python range boundaries exclude the end number).
for page_num in range(1, 429):
    # Dynamically inject the page number directly into your request string
    paginated_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page={page_num}"

    try:
        response = requests.get(paginated_url)

        # Confirm HTTP response status is optimal (200 means success)
        if response.status_code == 200:
            page_json = response.json()

            # Create a temporary dataframe focusing strictly on the current page records
            temp_df = pd.DataFrame(page_json["results"])[
                [
                    "id",
                    "title",
                    "release_date",
                    "overview",
                    "popularity",
                    "vote_average",
                    "vote_count",
                ]
            ]

            # Append the current page to your master sheet.
            # ignore_index=True dynamically sequences indices continuously (e.g., 1-8500+)
            master_df = pd.concat([master_df, temp_df], ignore_index=True)
        else:
            print(
                f"Skipping page {page_num}: Received Status Code {response.status_code}"
            )

    except Exception as e:
        print(f"An error occurred on page {page_num}: {e}")
        continue

# Check your ultimate matrix structural shape
print(f"Extraction Completed. Total dataset dimensions: {master_df.shape}")

# Export your freshly baked dataset seamlessly into a raw CSV document
master_df.to_csv("movies_dataset.csv", index=False)
print("Dataset successfully saved as movies_dataset.csv!")
```

# **DAY 18**

## It's really tough to Web scrape Data and present it as a data-frame 

### instead use AI-Powered & Modern Web Data Collection Tools to do this job - 

#### 1. [Firecrawl](https://www.firecrawl.dev?utm_source=chatgpt.com)
#### 2. [Jina AI Reader](https://jina.ai/reader?utm_source=chatgpt.com)
#### 3. [Apify](https://apify.com?utm_source=chatgpt.com)
#### 4. [Bright Data](https://brightdata.com?utm_source=chatgpt.com)
#### 5. [Browserbase](https://www.browserbase.com?utm_source=chatgpt.com)
#### 6. [Crawl4AI](https://github.com/unclecode/crawl4ai?utm_source=chatgpt.com)
#### 7. [LangChain Web Loaders](https://python.langchain.com?utm_source=chatgpt.com)

<br>
<br>

# **DAY 19** 

## UnderStanding  your Data 

### 1. How big is the data?

Understanding the shape (number of rows and columns) lets you know the scale of the data you are handling.

```python
df.shape
```

### 2. How does the data look like?

Previewing rows gives you a feel for the data format. While `df.head()` gives the top rows, using `df.sample()` is a better strategy to avoid any layout bias present at the beginning or end of the file.

```python
# To view the first 5 rows
df.head()

# To view 5 random rows (recommended to avoid layout bias)
df.sample(5)

```

### 3. What is the data type of each column?

Checking data types helps identify numerical, categorical, or text (`object`) columns. It also helps with optimization, such as downcasting continuous columns stored unnecessarily as floats into integers to save memory.

```python
df.info()
```

### 4. Are there any missing values?

Missing values can break machine learning models. This code tells you exactly how many missing values exist per column so you can plan whether to drop or impute them.

```python
df.isnull().sum()
```

### 5. How does the data look mathematically?

This provides a high-level statistical overview of all numerical features, helping you instantly spot distributions, standard deviations, and any mathematical anomalies.

```python
df.describe()

# Tip from comments: Use include="all" to see categorical stats as well
df.describe(include="all")
```

### 6. Are there duplicate values?

Duplicate entries introduce bias and reduce accuracy during model training. Checking for them lets you drop repetitive rows early on.

```python
df.duplicated().sum()
```

### 7. How is the correlation between the columns?

Correlation reveals how features relate to each other and the target variable (on a scale from -1 to 1). Features with little to no correlation can often be dropped to streamline the model.

```python
# Note: In newer pandas versions, pass numeric_only=True to avoid errors with string data
df.corr(numeric_only=True)

# To check correlation specifically with a target variable (e.g., 'Survived')
df.corr(numeric_only=True)['Survived']
```

<br>
<br>

# **DAY 20** 


## EDA using Univariate Analysis

This lecture covers the fundamentals of **Exploratory Data Analysis (EDA)** focusing on **Univariate Analysis**, which means analyzing a single variable (column) at a time to uncover trends, distributions, and shapes without looking at relationships between different variables.

Data is primarily divided into two main types:

* **Categorical Data:** Represents groups or categories (e.g., Survival status, Passenger Class, Gender, Embarked Station).
* **Numerical Data:** Continuous or discrete numbers (e.g., Age, Fare).

---


### 1. Analyzing Categorical Data

The instructor demonstrates two main ways to visualize categorical features using the `Seaborn` and `Matplotlib` libraries 

* **Countplot / Bar Chart:** Tells you the exact frequency of each category (e.g., showing that class 3 had the highest passenger count and more people died than survived)
* **Pie Chart:** Useful when you want to look at the relative distribution in terms of percentages (e.g., ~61% of passengers died, and ~65% of the passengers were male)

### 2. Analyzing Numerical Data

Numerical data is continuous, so instead of counting exact matches, we study its distribution and mathematical summary.

* **Histogram / Distplot:** Divides the range of continuous values into intervals ("bins") to map the data's shape. The curve overlaid by `distplot` is the **Probability Density Function (PDF)**, which displays the likelihood of data points falling across the range and helps determine if data is symmetrical or skewed.
* **Distribution Plots (Distplot / KDE):** Incorporates *Kernel Density Estimation (KDE)* to generate a continuous curve, turning frequency counts into a Probability Density Function (PDF). This also reveals data **skewness** (whether the data peaks centrally or leans left/right)
* **Box Plot:** Provides a **Five-Number Summary** (Minimum, 25th percentile $Q_1$, Median, 75th percentile $Q_3$, and Maximum). It is exceptionally useful for detecting potential **outliers** in your dataset.
* **Descriptive Statistics:** Functions like `.mean()`, `.median()`, `.min()`, `.max()`, and `.skew()` to mathematically understand the central tendency and asymmetry.

<BR>
<BR>


# **DAY 21**
## EDA using Bivariate and Multivariate Analysis.

### Key Visualization Techniques & Tools Covered

### 1. Numerical to Numerical Variables

* **Scatter Plot:** Used to analyze the relationship between two numerical columns. Using the `tips` dataset, the instructor plots `total_bill` vs `tip` to showcase a clear linear relationship.
* **Multivariate Expansion:** Demonstrates how to upgrade a bivariate scatter plot into multivariate analysis using additional parameters in Seaborn.
* `hue`: Adds a categorical dimension (e.g., color-coding by Gender).
* `style`: Encodes another category using markers (e.g., differentiating Smoker vs Non-smoker with dots and crosses).
* `size`: Introduces a numerical scale through marker size (e.g., party Size).



### 2. Numerical to Categorical Variables

* **Bar Plot:** Ideal for examining an average numerical metric across categories. For example, visualizing the average passenger age or ticket fare (`fare`) across different passenger classes (`Pclass`) in the `titanic` dataset.
* **Box Plot:** Used to visualize the five-number summary and identify outliers across categories (e.g., comparing the age distribution of males vs females, layered with survival status using `hue`).
* **Distplot / KDE Plot:** Shows how the probability density function (PDF) changes for different categories. By overlaying the age distributions of those who survived versus those who died, the instructor highlights clear data stories—such as children having a higher probability of survival.

### 3. Categorical to Categorical Variables

* **Cross-tabulation & Heatmaps:** Utilizing `pd.crosstab()` to create contingency tables (e.g., the number of people who survived/died per passenger class) and passing them into Seaborn's `heatmap` to visually isolate high-density clusters instantly.
* **Pandas GroupBy (Aggregations):** Grouping data to calculate precise survival percentages across categories (e.g., sex, embarkation ports) and visualizing them using bar charts.
* **Cluster Map:** Generates a heatmap alongside tree-like diagrams called dendrograms to automatically capture and group structurally similar hierarchical relationships in categorical data.

### 4. Special Multi-Variable & Time Plots

* **Pair Plot:** Automatically detects all numerical columns in a dataset (like `iris`) and creates a matrix of scatter plots for every combination, alongside histograms for self-correlations. It is highly effective for getting a quick bird's-eye view of multi-dimensional data.
* **Line Plot:** A specialized variation of a scatter plot used specifically when the x-axis contains time-series or sequential tracking tracking information (e.g., plotting yearly passenger growth using the `flights` dataset).

<br>
<br>

# **DAY 22**

## **Pandas Profiling** (now updated and maintained as `ydata-profiling`), a highly efficient tool designed to automate exploratory data analysis (EDA).

### Key Takeaways from the Video

* **Automation of EDA:** While manual analysis involves checking shape, variables, and plotting custom graphs, Pandas Profiling automates most of these heavy-lifting tasks with just a few lines of code.
* **Implementation Steps:** 1. Install the library via pip.
2. Import `ProfileReport` from the library.
3. Initialize it using your DataFrame and export the results to an interactive HTML file.
* **The Generated Report Sections:** The resulting HTML report simplifies dataset evaluation by dividing the data into five main components.
* **Overview:** Summarizes basic dataset statistics including row/column counts, missing cell percentages, duplicate values, and dataset memory footprint.
* **Variables:** Performs automated univariate analysis. It plots categorical charts or numerical histograms and details value distributions, minimums, maximums, and extreme values/outliers.
* **Interactions:** Handles bivariate and multivariate analysis by generating scatter plots to compare relationships between pairs of variables.
* **Correlations:** Offers a quick matrix visualization (like Pearson correlation) to show linear dependencies between features.
* **Missing Values & Samples:** Displays visualization maps (counts, matrix, dendrograms) pinpointing exact distributions of missing data, followed by previewing first and last sample rows.



The instructor notes that running this profile report is an excellent first step whenever starting any brand-new data science project.

<br>
<br>

# **DAY 23**

# introduction to **Feature Engineering**, 
## which is the process of using domain knowledge to extract or transform features from raw data to improve the performance of machine learning algorithms.

## Feature engineering into four core pillars:

### 1. Feature Transformation
This involves converting an existing feature into a form that is better suited for a machine learning model. Key techniques include:

* **Missing Value Imputation:** Handling missing data points by either removing them or filling them in using methods like mean, median, or mode.
* **Handling Categorical Values:** Converting string or categorical variables into numerical values (e.g., using One-Hot Encoding) so that frameworks like scikit-learn can process them .
* **Outlier Detection:** Identifying and removing extreme values that can disproportionately skew the training behavior of algorithms like linear regression .
* **Feature Scaling:** Bringing numerical features with different scales (e.g., age vs. salary) into a uniform range to prevent distance-based models from being dominated by a single variable.

### 2. Feature Construction
This is the manual creation of completely new features from existing data, heavily relying on your intuition, domain knowledge, and experience. For example, in the Titanic dataset, combining the separate features `SibSp` (siblings/spouses) and `Parch` (parents/children) into a single unified feature called `Family_Size` .

### 3. Feature Selection 

This process targets identifying and keeping only the most important features while filtering out redundant or irrelevant ones . Using datasets like MNIST as an example, selecting only the central pixels where digits are drawn significantly improves model speed and efficiency by reducing input dimensions 

### 4. Feature Extraction

Unlike feature construction, feature extraction programmatically projects or transforms high-dimensional data into a completely new, lower-dimensional set of features  This is often used for highly dimensional datasets using specialized algorithms like Principal Component Analysis (PCA) or Linear Discriminant Analysis (LDA) 


<br>
<br>

# **DAY 24**

## Feature Scaling & Standardization?

* **Feature Scaling:** This is a technique used to bring independent features of a dataset into a fixed or similar range. It is typically the final step of feature engineering, performed just before feeding data into a machine learning model.
* **Why we need it:** Algorithms that rely on distances (like K-Nearest Neighbors) or optimization techniques (like Gradient Descent in Logistic Regression and Neural Networks) perform poorly if one feature has a vastly larger scale than another (e.g., Age vs. Salary). The larger scale feature will mathematically dominate the model's logic.
* **Standardization (Z-score Normalization):** This transforms the data so that it ends up centered around a **Mean ($\mu$) of 0** and a **Standard Deviation ($\sigma$) of 1**.
* **Important Caveats:**
* **Distribution Shape:** Standardization changes the *scale* of the data, but it does **not** alter the underlying shape of the distribution.
* **Outliers:** It does **not** handle or minimize the relative impact of outliers. Outliers will remain outliers after being scaled.
* **When to use:** Use it for KNN, PCA, Logistic Regression, Linear Regression, and Deep Learning. You do **not** need it for tree-based models like Decision Trees, Random Forests, or Gradient Boosting.



---

## 2. Mathematical Formula

To standardize a specific value $x_i$ in a feature column, you subtract the mean ($\bar{x}$ or $\mu$) of that column and divide it by its standard deviation ($\sigma$):

$$x_i' = \frac{x_i - \mu}{\sigma}$$

Where:

* $x_i'$ = The newly scaled, standardized value.
* $x_i$ = The original raw value.
* $\mu$ = The mean of the feature column.
* $\sigma$ = The standard deviation of the feature column.

---

## 3. Scikit-Learn Code Implementation

Always perform your **Train-Test Split before scaling** to prevent data leakage. You `fit` the scaler only on the training data, but you `transform` both the training and testing sets.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Assume 'df' is your DataFrame with features and target
# Let's say columns are ['Age', 'EstimatedSalary'] and target is 'Purchased'
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# 2. Train-Test Split (Crucial step before scaling)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Initialize the StandardScaler
scaler = StandardScaler()

# 4. Fit the scaler on the training data (learns the mean and standard deviation)
scaler.fit(X_train)

# 5. Transform both the training and test datasets
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Note: StandardScaler returns NumPy arrays. 
# Optional: Convert back to DataFrame to preserve column names for visualization
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

# Verify the scaling effect: Mean should be ~0 and Standard Deviation should be ~1
print("Scaled Mean:\n", X_train_scaled.mean().round(2))
print("\Scaled Std Dev:\n", X_train_scaled.std().round(2))
```

<br>
<br>


# **DAY 25**

## Normalization 
Normalization is a critical data preparation technique used in machine learning to change the values of numeric columns to a common scale without distorting differences in ranges or losing information. It is primarily used to eliminate the impact of units and magnitudes, allowing algorithms to perform better.

### When to Use What:

* **Standardization** generally yields better results for most machine learning problems and is used by default.
* **MinMax Scaling** is highly recommended when you know the definitive minimum and maximum bounds of your data beforehand (e.g., Image Processing where pixel values range strictly between **0** and **255**).
* **Robust Scaling** should be preferred if your dataset contains a large number of outliers.
* **MaxAbs Scaling** is ideal for sparse datasets containing a high amount of zeros.

---

## 🧮 Mathematical Formulas

### 1. MinMax Scaling (Normalization)

Scales the data strictly between a range of **0** and **1**.


$$X' = \frac{X - X_{min}}{X_{max} - X_{min}}$$

### 2. Mean Normalization

Centers the data around the mean, scaling it typically between **-1** and **1**.


$$X' = \frac{X - X_{mean}}{X_{max} - X_{min}}$$


*(Note: Scikit-Learn does not have a built-in class for Mean Normalization, so it must be coded manually)*

### 3. MaxAbs Scaling

Scales data by dividing by the maximum absolute value. Ideal for preserving sparsity.


$$X' = \frac{X}{|X_{max}|}$$

### 4. Robust Scaling

Uses the median and Interquartile Range ($IQR$), making it robust to outliers.
$$X' = \frac{X - X_{median}}{IQR} = \frac{X - X_{median}}{Q_3 (75th\%) - Q_1 (25th\%)} $$
---

## 💻 Code Implementation

Here is how you can implement **MinMax Scaling**, **MaxAbs Scaling**, and **Robust Scaling** using Python's `scikit-learn` library:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, RobustScaler

# 1. Load your dataset
# df = pd.read_csv('your_data.csv')
# X = df[['feature1', 'feature2']]
# y = df['target']

# 2. Always split into training and testing sets first!
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# =====================================================================
# APPROACH A: MinMax Scaling (Most Common)
# =====================================================================
min_max_scaler = MinMaxScaler()

# Fit only on training data, but transform both train and test sets
X_train_minmax = min_max_scaler.fit_transform(X_train)
X_test_minmax = min_max_scaler.transform(X_test)

# =====================================================================
# APPROACH B: MaxAbs Scaling (For Sparse Data)
# =====================================================================
max_abs_scaler = MaxAbsScaler()
X_train_maxabs = max_abs_scaler.fit_transform(X_train)
X_test_maxabs = max_abs_scaler.transform(X_test)

# =====================================================================
# APPROACH C: Robust Scaling (For Outlier-Heavy Data)
# =====================================================================
robust_scaler = RobustScaler()
X_train_robust = robust_scaler.fit_transform(X_train)
X_test_robust = robust_scaler.transform(X_test)

# Note: Scikit-learn outputs NumPy arrays. Convert back to DataFrame if needed:
# X_train_scaled_df = pd.DataFrame(X_train_minmax, columns=X_train.columns)

```

# **DAY 26**

### Feature Engineering Framework

Encoding categorical data is a critical sub-type of **Feature Transformation** within the larger machine learning pipeline of Feature Engineering. Since machine learning algorithms explicitly require numbers rather than strings, data scientists must encode text categories into a numerical format.

---

### Classification of Categorical Data

Categorical data is split into two primary types:

* **Nominal Data:** Categories have no inherent order or relationship to one another (e.g., States, Engineering Branches, or Gender). This is typically encoded using **One-Hot Encoding**.
* **Ordinal Data:** Categories have a strict, sequential order or relative relationship (e.g., School grades, Customer Reviews like *Poor < Average < Good*, or Education levels like *High School < Undergrad < Postgrad*). This is handled using **Ordinal Encoding**.

---

### Ordinal Encoding vs. Label Encoding

A critical insight shared in the video is distinguishing when to use specific Scikit-Learn tools, avoiding a common mistake made by many practitioners:

| Encoding Type | Application Target | Description |
| --- | --- | --- |
| **Ordinal Encoder** | **Input Features ($X$)** | Used when the independent/input variables contain ordinal categories. You must manually pass the intended order format to the `categories` hyperparameter so Scikit-Learn knows the rank. |
| **Label Encoder** | **Output Target ($y$)** | Specifically designed by Scikit-Learn to encode target labels for classification problems. It automatically maps the classes to numbers (between $0$ and $\text{classes}-1$) and should **never** be used on input features ($X$). |

---

### Implementation Workflow

The practical coding walkthrough follows these steps:

1. **Train-Test Split:** Always separate your data into training and testing sets before doing feature transformations to prevent data leakage.
2. **Ordinal Encoding ($X$):** The `OrdinalEncoder` class is instantiated with a list of ordered categories matching the rank hierarchy (e.g., mapping `['Poor', 'Average', 'Good']` to sequential integers). It is then applied using `.fit()` on the training set and `.transform()` on both training and test sets.
3. **Label Encoding ($y$):** The `LabelEncoder` is instantiated without parameters (as target class ranking is determined internally or randomly) to transform the target prediction column (e.g., turning a `Purchased` status of `Yes`/`No` into `1`/`0`).


<br>
<br>


# **DAY 27**

## **"One Hot Encoding | Handling Categorical Data |**

### 1. The Need for One Hot Encoding (OHE)

* Machine learning algorithms generally require numerical input and cannot process categorical data in text/string format directly.
* Categorical data is split into two types: **Ordinal** (variables with an intrinsic order, like grades or sizes) and **Nominal** (variables with no inherent order, like colors, gender, or states).
* While Ordinal Encoding works for ordered data, using it on nominal data (e.g., assigning Yellow=0, Blue=1, Red=2) misleads the ML model into thinking one category is mathematically "greater" than another.
* **One Hot Encoding** solves this by creating a new binary column (containing only 0 or 1) for every unique category present in the feature.

### 2. Dummy Variable Trap & Multi-collinearity

* The newly created binary columns are called **Dummy Variables**.
* If a feature has $N$ distinct categories and you keep all $N$ columns, it introduces a mathematical dependency because the sum of all these columns will always equal 1. This issue is called **Multi-collinearity**.
* Multi-collinearity negatively impacts linear models like Linear and Logistic Regression. To fix this, you must drop one column, keeping only **$N-1$ columns**. If all remaining $N-1$ columns are 0, the model inherently understands that the dropped category is the active one.

### 3. Handling Features with Too Many Categories (High Cardinality)

* If a nominal column has too many unique categories (e.g., a "Car Brand" column with 32 different brands), OHE will create 32 new columns. This vastly increases the dataset's dimensionality and slows down model training.
* The solution is to identify the most frequently occurring categories (the top threshold) and bundle all the remaining rare categories into a single new category named **"Other"** or **"Uncommon"**. This keeps the number of columns manageable.

### 4. Practical Implementation in Python

The video demonstrates implementation using a car dataset through two different tools:

* **Pandas (`pd.get_dummies`)**: Good for quick Exploratory Data Analysis (EDA). You can pass `drop_first=True` to automatically handle the dummy variable trap. However, it shouldn't be used in production ML pipelines because it doesn't remember the exact order and structure of columns across different runs.
* **Scikit-Learn (`OneHotEncoder`)**: The ideal approach for machine learning projects. By setting parameters like `drop='first'` and `sparse=False`, you can seamlessly integrate it into production-ready pipelines.

The instructor concludes by noting that manually managing and aligning these encoded numpy arrays with the rest of the numerical data can be tedious, which is why the next lecture will introduce **Column Transformers** to do this efficiently in a single line of code.

<br>
<br>

# **DAY 28**

## **ColumnTransformer**

## Executive Summary: "Aam Zindagi" vs. "Mentos Zindagi"

When dealing with complex tabular data in machine learning, different columns often require distinct preprocessing treatments.

* **Numerical columns** might need missing value imputation (`SimpleImputer`) or feature scaling.
* **Ordinal categorical columns** require hierarchical mapping (`OrdinalEncoder`).
* **Nominal categorical columns** require disjoint mapping (`OneHotEncoder`).

### The Old Painful Way ("Aam Zindagi")

Without a unified framework, you have to chunk out columns individually, apply separate functions, extract `numpy` arrays, and continuously stitch them back together using functions like `np.concatenate`. This becomes highly prone to tracking errors, breaks easily, and creates a nightmare to duplicate onto your validation/test sets without leaking data.

### The ColumnTransformer Solution ("Mentos Zindagi")

Scikit-Learn provides `ColumnTransformer` to neatly package all heterogeneous preprocessing tasks into a single object. It processes specified column bundles concurrently and compiles them instantly into a unified, numeric representation ready for model ingestion.

---

## Core Code Implementation

Here is how you can implement `ColumnTransformer` explicitly matching the walkthrough.

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer

# 1. Assuming 'df' is loaded containing columns: 'age', 'gender', 'fever', 'cough', 'city', 'has_covid'
# Splitting into features (X) and target label (y)
X = df.drop(columns=['has_covid'])
y = df['has_covid']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Define the ColumnTransformer framework
# Note: In modern scikit-learn versions, use 'sparse_output=False' instead of 'sparse=False'
transformer = ColumnTransformer(
    transformers=[
        ('tnf1', SimpleImputer(), ['fever']),                                             # Mean imputation for numerical tracking
        ('tnf2', OrdinalEncoder(categories=[['mild', 'strong']]), ['cough']),             # Sequential structural encoding
        ('tnf3', OneHotEncoder(sparse_output=False, drop='first'), ['gender', 'city'])    # Flat structural categorical encoding
    ], 
    remainder='passthrough' # Crucial step to retain unmentioned columns like 'age' intact
)

# 3. Fit and Transform on training data
X_train_transformed = transformer.fit_transform(X_train)

# 4. Purely transform your test partition (To strictly prevent data leakage)
X_test_transformed = transformer.transform(X_test)

print("Preprocessed Training Shape:", X_train_transformed.shape)

```

### Critical Implementation Takeaways:

* **`remainder='passthrough'`**: This argument ensures that columns requiring absolutely no transformations (such as `age` in this specific video) are kept in the final array instead of being dropped by default.
* **Modernizing Syntax**: Note that newer versions of Scikit-Learn have replaced the `sparse` parameter with `sparse_output=False` inside the `OneHotEncoder` setup to reliably yield dense matrix instances.

# **DAY 29**

## **Machine Learning PIPELINES**

## 📌 Video Summary

The video explains **Scikit-Learn Pipelines**, demonstrating how they chain together multiple data preprocessing and modeling steps so that the output of each step serves as the input to the next.
The instructor showcases two workflows on the Titanic dataset:

1. **Without Pipelines:** Preprocessing steps like missing value imputation (`SimpleImputer`) and categorical encoding (`OneHotEncoder`) are done manually, While training is straightforward, executing this on new test data for a production deployment requires copying and tracking all individual preprocessing steps in the exact sequence, creating highly fragile code 
2. **With Pipelines:** All steps—Imputation, Encoding, Feature Scaling, Feature Selection, and Model Training—are unified into a single Scikit-Learn `Pipeline` object. When exporting the model via `pickle`, only the unified pipeline object needs to be saved. New production inputs can be processed and predicted with a single `.predict()` call, without changing any client-side code 

---

## 🛠️ Code Implementation

## Approach 1: **Without Pipelines** (The Hard Way)

### 1. **Aam Zindagi** -  Training & Exporting 

```python
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load and drop unnecessary columns
df = pd.read_csv('titanic.csv')
df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    df.drop(columns=['Survived']), df['Survived'], test_size=0.2, random_state=42
)

# Imputation
si_age = SimpleImputer()
si_embarked = SimpleImputer(strategy='most_frequent')

X_train_age = si_age.fit_transform(X_train[['Age']])
X_train_embarked = si_embarked.fit_transform(X_train[['Embarked']])

X_test_age = si_age.transform(X_test[['Age']])
X_test_embarked = si_embarked.transform(X_test[['Embarked']])

# One Hot Encoding
ohe_sex = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
ohe_embarked = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

X_train_sex = ohe_sex.fit_transform(X_train[['Sex']])
X_train_embarked = ohe_embarked.fit_transform(X_train_embarked)

X_test_sex = ohe_sex.transform(X_test[['Sex']])
X_test_embarked = ohe_embarked.transform(X_test_embarked)

# Concatenate remaining features back together
X_train_rem = X_train.drop(columns=['Sex', 'Age', 'Embarked']).values
X_test_rem = X_test.drop(columns=['Sex', 'Age', 'Embarked']).values

X_train_transformed = np.concatenate([X_train_rem, X_train_age, X_train_sex, X_train_embarked], axis=1)
X_test_transformed = np.concatenate([X_test_rem, X_test_age, X_test_sex, X_test_embarked], axis=1)

# Model Training
clf = DecisionTreeClassifier()
clf.fit(X_train_transformed, y_train)

# Export individual components
pickle.dump(clf, open('clf.pkl', 'wb'))
pickle.dump(ohe_sex, open('ohe_sex.pkl', 'wb'))
pickle.dump(ohe_embarked, open('ohe_embarked.pkl', 'wb'))

```

### 2. Production Prediction (Without Pipeline)

```python
import numpy as np
import pickle

# Load transformers and model individually
clf = pickle.load(open('clf.pkl', 'rb'))
ohe_sex = pickle.load(open('ohe_sex.pkl', 'rb'))
ohe_embarked = pickle.load(open('ohe_embarked.pkl', 'rb'))

# New input: [Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]
test_input = np.array([2, 'male', 31.0, 0, 0, 10.5, 'S'], dtype=object).reshape(1, -1)

# Manually recreate tracking step-by-step preprocessing transformations
test_input_sex = ohe_sex.transform(test_input[:, 1].reshape(-1, 1))
test_input_embarked = ohe_embarked.transform(test_input[:, 6].reshape(-1, 1))
test_input_age = test_input[:, 2].reshape(-1, 1)
test_input_rem = test_input[:, [0, 3, 4, 5]]

test_input_transformed = np.concatenate([test_input_rem, test_input_age, test_input_sex, test_input_embarked], axis=1)

# Predict
print(clf.predict(test_input_transformed))

```

---

## Approach 2: **With Pipelines** (The Efficient Way)

### 1. Building and Training the Pipeline

```python
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline

# Load Dataset
df = pd.read_csv('titanic.csv')
df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True)

X_train, X_test, y_train, y_test = train_test_split(
    df.drop(columns=['Survived']), df['Survived'], test_size=0.2, random_state=42
)

# Step 1: Imputation (Using indices instead of names to avoid array conversion errors)
trf1 = ColumnTransformer([
    ('impute_age', SimpleImputer(), [2]),
    ('impute_embarked', SimpleImputer(strategy='most_frequent'), [6])
], remainder='passthrough')

# Step 2: One Hot Encoding
trf2 = ColumnTransformer([
    ('ohe_sex_embarked', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), [1, 6])
], remainder='passthrough')

# Step 3: Scaling
trf3 = ColumnTransformer([
    ('scale', MinMaxScaler(), slice(0, 10))
])

# Step 4: Feature Selection
trf4 = SelectKBest(score_func=chi2, k=8)

# Step 5: Model
trf5 = DecisionTreeClassifier()

# Chain them all into a Pipeline
pipe = Pipeline([
    ('trf1', trf1),
    ('trf2', trf2),
    ('trf3', trf3),
    ('trf4', trf4),
    ('trf5', trf5)
])

# Single fit command triggers data flow sequentially
pipe.fit(X_train, y_train)

# Export the entire pipeline structure cleanly
pickle.dump(pipe, open('pipe.pkl', 'wb'))

```

### 2. Production Prediction (With Pipeline)

```python
import numpy as np
import pickle

# Load the single pipeline file
pipe = pickle.load(open('pipe.pkl', 'rb'))

# New raw data array input matching original feature dataframe format
test_input2 = np.array([2, 'male', 31.0, 0, 0, 10.5, 'S'], dtype=object).reshape(1, -1)

# One command automatically executes all transformation layers and outputs predictions
print(pipe.predict(test_input2))

```

<br>
<br>

# **DAY 30**

## **Mathematical Transformer**

## What & Why?

**Mathematical Transformation** is a feature engineering technique where you apply a mathematical function to data columns to change their underlying distribution.

* **The Ultimate Goal:** To convert a skewed distribution into a **Normal (Gaussian) Distribution** (or close to it).
* **Why do it?** Linear machine learning models like *Linear Regression* and *Logistic Regression* assume data is normally distributed; forcing the data into normality significantly improves their accuracy and stability. Tree-based algorithms like *Decision Trees* or *Random Forests* do not care about distribution and won't see much change.
* **How to Check Normality?** Use a **Q-Q Plot (Quantile-Quantile Plot)** 
The closer your data points align to a 45-degree diagonal line, the closer the data is to being normally distributed 
---

## 🧮 Formulas & When to Use Them

Here are the 4 primary transformations handled by Scikit-Learn's `FunctionTransformer`:

### 1. Log Transform

$$y = \log(x) \quad \text{or} \quad y = \log(x + 1)$$

* **When to use:** **Right-skewed (positively skewed) data**
* **Why:** It squashes large outliers and brings extreme values closer on a compressed scale. `log1p` ($x+1$) is safer because standard $\log(0)$ is undefined.

### 2. Reciprocal Transform

$$y = \frac{1}{x}$$

* **When to use:** When small values should become larger and huge values should become smaller.
* *Note:* Ensure $x \neq 0$ to avoid division-by-zero errors.

### 3. Square Transform

$$y = x^2$$

* **When to use:** **Left-skewed (negatively skewed) data** 

### 4. Square Root Transform

$$y = \sqrt{x}$$

* **When to use:** Moderately right-skewed data; milder than a log transform.

---

## 💻 Python Code Implementation

This snippet uses `scikit-learn`'s `FunctionTransformer` to apply a **Log Transform** to a skewed feature (like `Fare` in Titanic dataset) while keeping other features intact using a `ColumnTransformer`.

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

# 1. Dummy Setup (Simulating Age, Fare, and Survived)
data = {
    'Age': [22, 38, 26, 35, 35, 28, 54, 2, 27, 14],
    'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 51.86, 21.07, 11.13, 30.07],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
}
df = pd.DataFrame(data)

X = df[['Age', 'Fare']]
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Define your Mathematical Transformation via FunctionTransformer
# We use np.log1p (log(x+1)) to cleanly handle any 0 values safely.
log_transformer = FunctionTransformer(np.log1p)

# 3. Use ColumnTransformer to apply only to the skewed column ('Fare')
# 'passthrough' ensures 'Age' is not modified.
trf = ColumnTransformer([
    ('log_fare', log_transformer, ['Fare'])
], remainder='passthrough')

# 4. Transform the data
X_train_transformed = trf.fit_transform(X_train)
X_test_transformed = trf.transform(X_test)

# 5. Train your model
model = LogisticRegression()
model.fit(X_train_transformed, y_train)

print("Model trained successfully on transformed data!")

```

### Swapping Transformations:

If you want to try the other transformations discussed in the video, just replace `np.log1p` in the `FunctionTransformer` with:

* **Reciprocal:** `lambda x: 1 / (x + 0.0001)`
* **Square:** `lambda x: x2`
* **Square Root:** `np.sqrt`



<br>
<br>

# **DAY 31**

## **Power Transformers**
## 📌 Video Summary

**Power Transformers**, a family of parametric, monotonic mathematical transformations.

* **Objective:** These transformers are designed to stabilize variance and normalize data distributions, converting non-normal (skewed) data into a **Gaussian-like (Normal) distribution**.
* **Why it matters:** Many machine learning algorithms—such as Linear Regression, Logistic Regression, and Artificial Neural Networks (ANNs)—perform significantly better or inherently assume that the input numerical features follow a normal distribution.
* **Finding $\lambda$:** The transformation parameter $\lambda$ determines the power to which the data is raised. It is automatically optimized (typically between $-5$ and $5$) to minimize skewness using techniques like **Maximum Likelihood Estimation (MLE)** or Bayesian Statistics.

---

## 🧮 Mathematical Formulas

The two main types of power transformations supported by `PowerTransformer` are **Box-Cox** and **Yeo-Johnson**.

### 1. Box-Cox Transform

The Box-Cox transformation is a generalized approach where log and square-root transformations are special cases.

> ⚠️ **Strict Restriction:** It can **only** be applied to strictly positive data ($y > 0$). It does not support zero or negative values.

$$y^{(\lambda)} = \begin{cases} \frac{y^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0 \\ \ln(y) & \text{if } \lambda = 0 \end{cases}$$

### 2. Yeo-Johnson Transform

The Yeo-Johnson transformation is a modification of the Box-Cox method created to overcome its limitation.

> **Advantage:** It natively handles **zero and negative numbers** alongside positive values.

$$y^{(\lambda)} = \begin{cases} \frac{(y + 1)^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0, y \geq 0 \\ \ln(y + 1) & \text{if } \lambda = 0, y \geq 0 \\ -\frac{(-y + 1)^{2 - \lambda} - 1}{2 - \lambda} & \text{if } \lambda \neq 2, y < 0 \\ -\ln(-y + 1) & \text{if } \lambda = 2, y < 0 \end{cases}$$

---

## 💻 Python Implementation Code

In `scikit-learn`, both methods are packaged within the `PowerTransformer` class. By default, it also standardizes the output (scales data to a mean of 0 and variance of 1).

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PowerTransformer
from sklearn.metrics import r2_score

# 1. Split your data into Train and Test sets to prevent data leakage
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- METHOD A: Yeo-Johnson (Default) ---
# Works out of the box with zero and negative values
pt_yeo = PowerTransformer(method='yeo-johnson', standardize=True)

X_train_transformed = pt_yeo.fit_transform(X_train)
X_test_transformed = pt_yeo.transform(X_test)

# --- METHOD B: Box-Cox ---
# Note: If your data has zeros (like the Concrete dataset in the video), 
# you can apply a small shift constant before using Box-Cox
# X_train_positive = X_train + 0.00001 

pt_box = PowerTransformer(method='box-cox', standardize=True)
# X_train_transformed = pt_box.fit_transform(X_train_positive)

# 2. View the optimized optimal lambda values chosen for each column
print("Optimized Lambdas:", pt_yeo.lambdas_)

# 3. Fit a baseline model to check performance improvement
lr = LinearRegression()
lr.fit(X_train_transformed, y_train)
y_pred = lr.predict(X_test_transformed)

print("Transformed R2 Score:", r2_score(y_test, y_pred))

```

### 📈 Video Experiment Results:

In the tutorial's concrete strength dataset experiment:

* **Without Transformation:** The cross-validated $R^2$ score was low, sitting around **0.46**.
* **With Box-Cox/Yeo-Johnson:** The cross-validated $R^2$ score surged significantly to roughly **0.66**, proving how helpful normalization is for linear models!


<BR>
<BR>


# **DAY 32**

## **Binning (Discretization)** and **Binarization** 

## 1. Discretization / Binning

Discretization is the process of transforming continuous numerical variables into discrete, categorical features by creating a set of continuous intervals (bins). This helps in handling outliers better and transforming non-linear relationships into linear ones.

### A. Equal Width / Uniform Binning

The width of all bins is kept identical.

* **Formula:** 
$$\text{Width} = \frac{\text{Max Value} - \text{Min Value}}{\text{Number of Bins}}$$


* **Characteristics:** It handles outliers well but does not alter the underlying data spread significantly

### B. Equal Frequency / Quantile Binning

Each bin contains approximately the same number of observations (percentiles/quantiles).

* **Characteristics:** The interval widths vary, but the population density per bin remains uniform. This technique is highly effective at making the value distribution uniform.

### C. KMeans Binning

Uses the K-Means clustering algorithm to group values. Centroids are calculated iteratively based on the distance of data points to create optimal intervals.

* **Characteristics:** Best suited when data naturally clusters into separate pockets.

### D. Custom / Domain-Based Binning

Instead of an automated algorithm, you apply business logic or domain expertise to set manual intervals (e.g., splitting Age into `0-18` for minors, `18-60` for working adults, and `60+` for seniors). This must be done manually using `pandas` (e.g., `pd.cut()`) as `scikit-learn` doesn't provide it directly.

---

## 2. Binarization

Binarization is a special case of discretization where continuous features are converted into purely binary thresholds (`0` or `1`) based on a specified limit.

* **Example:** Mapping image pixels from color/grayscale ($0\text{ to }255$) to black and white ($0\text{ or }1$), or marking if a person is traveling alone based on family size ($0$ vs $>0$).

---

## 3. Python Code Implementation

You can implement these transformations seamlessly using `scikit-learn`'s `KBinsDiscretizer` and `Binarizer` classes.
```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer, Binarizer
from sklearn.compose import ColumnTransformer

# Dummy dataset containing Age, Fare, and Family Size
data = pd.DataFrame({
    'Age': [22, 38, 26, 35, 54, 2, 27, 14, 4],
    'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 21.07, 11.13, 30.07, 16.70],
    'Family': [1, 1, 0, 5, 0, 4, 0, 2, 1]
})

# ==========================================
# 1. DISCRETIZATION (BINNING) IMPLEMENTATION
# ==========================================

# Quantile Binning for Age, Uniform Binning for Fare
kbin_age = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')
kbin_fare = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')

# Applying transformations via ColumnTransformer
trf1 = ColumnTransformer([
    ('first', kbin_age, [0]),   # Apply to Age (Index 0)
    ('second', kbin_fare, [1])  # Apply to Fare (Index 1)
], remainder='passthrough')

data_binned = trf1.fit_transform(data)
print("Binned Data Matrix:\n", data_binned)


# ==========================================
# 2. BINARIZATION IMPLEMENTATION
# ==========================================

# Threshold = 0: Values <= 0 become 0, values > 0 become 1
binarizer = Binarizer(threshold=0.0, copy=False)

trf2 = ColumnTransformer([
    ('binarize_family', binarizer, [2]) # Apply to Family column (Index 2)
], remainder='passthrough')

data_binarized = trf2.fit_transform(data)
print("\nBinarized Data Matrix (Family modified to Binary):\n", data_binarized)

```

<br>
<br>

