# 💡 Customer Churn Prediction API

This is a **FastAPI-based web service** that serves a trained **Gradient Boosting model** to predict customer churn. The model takes in customer data, applies preprocessing transformations, and returns a prediction indicating the likelihood of churn.

---

## 🚀 Features

* ✅ `/` – Home route to welcome users
* ✅ `/health` – Health check endpoint
* ✅ `/predict` – Accepts JSON input and returns a churn prediction

---

## 📦 Project Structure

```
.
├── main.py                  # FastAPI app with endpoints
├── test_main.py             # Unit tests for the API
├── models/
│   └── GBOOST_model.pkl     # Trained Gradient Boosting model
├── transformer.pkl          # Preprocessing pipeline (e.g., OneHotEncoder, Scaler, etc.)
├── requirements.txt         # Python dependencies
```

---

## 🧪 Sample Input

POST `/predict`

```json
{
  "CreditScore": 650,
  "Geography": "France",
  "Gender": "Female",
  "Age": 40,
  "Tenure": 5,
  "Balance": 50000.0,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 60000.0
}
```

### ✅ Sample Output

```json
{
  "prediction": 0
}
```

---

## 🛠️ How to Run

### 🔹 1. Clone the repository

```bash
git clone 
```

### 🔹 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 🔹 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 🔹 4. Run the API

```bash
uvicorn main:app --reload
```

API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔍 API Docs

Interactive API documentation is available at:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Running Tests

Make sure `pytest` is installed:

```bash
pip install pytest
```

Then run the tests:

```bash
pytest -s test_main.py
```

---

