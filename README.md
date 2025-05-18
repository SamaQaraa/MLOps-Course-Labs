# 🏦 Bank Customer Churn Prediction

This project focuses on predicting customer churn in a banking environment using supervised machine learning. The pipeline includes preprocessing, model training, evaluation, and deployment with **MLflow** tracking.

## 🎯 Objective

To develop a robust classification system that identifies customers likely to leave the bank, helping stakeholders take proactive action.

---

## 🔍 Model Selection Rationale

After evaluating multiple models, two were selected based on performance and interpretability:

### ✅ Gradient Boosting (GBOOST) — **Production**

* 📈 **Top Performer**: Achieved highest F1-score with balanced precision and recall.
* 🧠 **Resilient**: Performed well on rebalanced data using SMOTE.
* 🔍 **Explainability**: Offers clear feature importance insights.
* 🔒 **Stable**: Delivered consistent results across validation splits.

### 🧪 Random Forest (RF) — **Staging**

* 🥈 **Strong Runner-Up**: Second-best across key metrics.
* 🌲 **Ensemble Diversity**: Adds value through bagging (vs boosting).
* 🔄 **Ready Backup**: Ideal fallback if production model degrades.
* 📊 **Interpretable**: Delivers human-readable feature importances.

⚠️ Other models such as **Logistic Regression** and **SVM** underperformed and were excluded from deployment.

---

## 🗂️ Project Structure

```
MLOPS-COURSE-LABS/
├── .gitignore                # Specifies files to ignore in version control
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── dataset/
│   └── Churn_Modelling.csv   # Raw dataset file
├── img/                      # Visualization directory
│   ├── confusion_matrix_GBOOST.png
│   ├── confusion_matrix_LR.png
│   ├── confusion_matrix_RF.png
│   └── confusion_matrix_SVC.png
├── src/
│   └── train.py              # Main training script
└── transformer.pkl           # Serialized preprocessing pipeline

```

---

## ⚙️ Key Features

* 🔄 **Preprocessing Pipeline**:

  * Categorical encoding (OneHotEncoder)
  * Feature scaling (StandardScaler)
  * Class balancing (SMOTE or similar)
* 🤖 **Trained Models**:

  * Logistic Regression
  * Support Vector Machine (SVM)
  * Random Forest
  * Gradient Boosting
* 📦 **MLflow Integration**:

  * Experiment logging
  * Model tracking/versioning
  * Artifact storage (metrics, plots, transformer)
* 🚀 **Model Promotion Strategy**:

  * **GBOOST** → Production
  * **Random Forest** → Staging

---

## 🧪 How to Run

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Train models**

   ```bash
   python src/train.py
   ```

3. **View MLflow dashboard**

   ```bash
   mlflow ui
   ```

---

## 📊 Evaluation Metrics

Metrics calculated on a balanced and preprocessed test set:

| Metric    | Meaning                                     |
| --------- | ------------------------------------------- |
| Accuracy  | Overall correct predictions                 |
| Precision | Correct churn predictions over total churns |
| Recall    | Actual churns correctly identified          |
| F1 Score  | Balance between precision and recall        |

Visual insights are provided via confusion matrix heatmaps per model.

---


