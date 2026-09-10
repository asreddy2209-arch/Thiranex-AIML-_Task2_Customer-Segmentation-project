# 🧑‍💼 Customer Segmentation Using Machine Learning

A **Customer Segmentation** project that uses **Machine Learning and K-Means Clustering** to group customers based on their purchasing behavior and characteristics.

The project generates synthetic customer data, performs exploratory data analysis, determines suitable clusters using elbow and silhouette analysis, applies K-Means clustering, and creates meaningful customer segment names based on **spending, purchase frequency, and recency**.

The results can also be visualized using **Power BI**.

---

## 📌 Project Overview

Customer segmentation helps businesses understand different groups of customers and create targeted marketing strategies.

This project uses **K-Means Clustering** to segment customers into groups with similar characteristics.

The segmentation considers customer behavior such as:

* 💰 Spending
* 🛒 Purchase frequency
* ⏱️ Recency
* 💵 Income
* 👤 Demographic information
* 📍 Location

The final segments are interpreted using their measured characteristics rather than simply using K-Means cluster IDs.

---

## 🎯 Objectives

* Analyze customer purchasing behavior
* Perform exploratory data analysis
* Identify meaningful customer groups
* Determine an appropriate number of clusters
* Apply K-Means clustering
* Evaluate clustering using:

  * Elbow Method
  * Silhouette Score
* Create business-friendly customer segment names
* Export processed data for Power BI
* Generate customer segmentation insights

---

## 🧠 Machine Learning Approach

### K-Means Clustering

The project uses **K-Means**, an unsupervised machine learning algorithm.

The basic workflow is:

```text
Customer Data
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Preparation
      ↓
Elbow Method
      ↓
Silhouette Analysis
      ↓
K-Means Clustering
      ↓
Customer Segments
      ↓
Business Insights
      ↓
Power BI Dashboard
```

---

## 📊 Customer Segments

The segment names are assigned based on the actual characteristics of each cluster.

Instead of using generic names such as:

```text
Cluster 0
Cluster 1
Cluster 2
```

the project interprets clusters using:

* Spending level
* Purchase frequency
* Recency

This makes the results easier to understand from a business perspective.

---

## 📁 Project Structure

```text
Customer-Segmentation/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── customer_data.csv
│   │
│   └── processed/
│       ├── customers_segmented_powerbi.csv
│       ├── segment_summary_powerbi.csv
│       ├── elbow_results.csv
│       └── silhouette_results.csv
│
├── outputs/
│   ├── charts/
│   │   ├── ...
│   │
│   └── reports/
│       └── segment_insights.txt
│
└── src/
    ├── pipeline.py
    └── ...
```

> The exact generated files may vary depending on the pipeline configuration.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical computations
* **Scikit-learn** – Machine Learning and K-Means clustering
* **Matplotlib** – Data visualization
* **Seaborn** – Exploratory data visualization
* **Power BI** – Interactive business intelligence dashboard

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd <YOUR-REPOSITORY-NAME>
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Run the main pipeline from the project root:

```bash
python main.py
```

The `main.py` file loads the project pipeline from the `src` directory and executes it.

After execution, the processed datasets and segmentation analysis will be available in the appropriate `data/processed` and `outputs` directories.

---

## 📈 Exploratory Data Analysis

The project includes exploratory analysis to understand relationships between customer characteristics.

Example analysis areas include:

* Spending behavior
* Purchase frequency
* Recency
* Income
* Gender
* Location
* Relationships between numerical features

The generated scatter plots and other visualizations can be used to understand the structure of the customer data before clustering.

---

## 🔍 Selecting the Number of Clusters

Two techniques are used to evaluate the appropriate number of customer segments.

### Elbow Method

The elbow method evaluates the clustering inertia for different values of `K`.

```text
K = 2
K = 3
K = 4
K = 5
...
```

The point where the reduction in inertia begins to slow down can help identify a suitable number of clusters.

### Silhouette Analysis

The silhouette score measures how well each customer fits within its assigned cluster compared with other clusters.

A higher silhouette score generally indicates better-separated clusters.

The resulting elbow and silhouette tables are saved in the processed data directory.

---

## 📊 Power BI Dashboard

The project provides Power BI-ready datasets:

```text
data/processed/customers_segmented_powerbi.csv
data/processed/segment_summary_powerbi.csv
```

These files can be imported directly into Power BI.

### Recommended KPI Cards

Create cards for:

* 👥 Customer Count
* 💰 Average Spending
* 💵 Average Income
* 🛒 Average Purchase Frequency

### Recommended Visualizations

Build the following visuals:

* Segment Distribution
* Segment vs Total Spending
* Gender Distribution
* Location Distribution
* Customer Segmentation Scatter Plot

### Recommended Slicers

Add slicers for:

* Segment
* Gender
* Location

---

## 💡 Business Insights

Customer segments can be used to create targeted marketing strategies.

### High-Spending Customers

Target high-spending customers with:

* Loyalty rewards
* Retention benefits
* Premium offers
* Personalized recommendations

### Occasional / Lower-Spending Customers

Target occasional or lower-spending customers with:

* Reactivation campaigns
* Personalized discounts
* Promotional offers
* Engagement campaigns

The current calculated insights are available in:

```text
outputs/reports/segment_insights.txt
```

The project's existing documentation recommends retention-focused benefits for high-spending segments and tailored reactivation offers for lower-spending or occasional segments.

---

## 📦 Output Files

| Output                            | Description                                   |
| --------------------------------- | --------------------------------------------- |
| `customers_segmented_powerbi.csv` | Customer-level data with assigned segments    |
| `segment_summary_powerbi.csv`     | Summary statistics for each segment           |
| `elbow_results.csv`               | Results used for elbow analysis               |
| `silhouette_results.csv`          | Silhouette analysis results                   |
| `segment_insights.txt`            | Business insights generated from segmentation |

---

## 🔮 Future Improvements

Possible improvements include:

* Add a Streamlit interactive dashboard
* Add customer lifetime value analysis
* Add RFM-based segmentation
* Compare K-Means with DBSCAN and hierarchical clustering
* Add automated model evaluation
* Add customer churn prediction
* Add recommendation systems
* Deploy the dashboard online
* Connect the dashboard to a live database

---

## 📌 Key Takeaway

This project demonstrates how **Machine Learning can transform raw customer data into actionable business segments**.

By combining:

**Data Analysis → K-Means Clustering → Segment Interpretation → Power BI**

businesses can better understand their customers and develop more targeted marketing and retention strategies.

---


👩‍💻 GitHub Profile

Annreddy Saaketh Reddy

B.Tech Student  |Python & Data Analytics Enthusiast


📬 Connect With Me

GitHub
https://github.com/asreddy2209-arch

LinkedIn
https://www.linkedin.com/in/saaketh-reddy-annreddy-22434937b/

⭐ Support

If you find this project useful:

⭐ Give the repository a star 
🍴 Fork the repository 
📢 Share the project 
💬 Provide feedback

📜 License
This project is intended for educational and portfolio purposes.

                                     🙏 Thank You

⭐ **Module 1 — Introduction to AI & Python**
