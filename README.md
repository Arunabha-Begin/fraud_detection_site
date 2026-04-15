# Fraud Detection in Transactions

A machine learning-based web application that detects fraudulent transactions using trained models. This project aims to improve financial security by identifying suspicious activities with high accuracy and minimal false positives.

# Project Overview

With the rapid growth of online transactions, fraud detection has become a critical challenge. This project uses machine learning algorithms to analyze transaction data and classify them as *fraudulent* or *legitimate*.
The system is designed to:
* Automate fraud detection
* Reduce manual effort
* Improve detection accuracy
* Provide quick and reliable predictions

# Technologies Used

* Python
* Scikit-learn
* Pandas, NumPy
* HTML, CSS, JavaScript
* Flask (for backend deployment)

# Features

* Data preprocessing and feature engineering
* Machine learning model (Random Forest)
* Real-time fraud prediction
* User-friendly web interface
* High accuracy with optimized performance

## Model Details

* Algorithm: Random Forest Classifier
* Evaluation Metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * ROC-AUC

## Project Structure

```
project/
│── app.py
│── model.py
│── index.html
│── style.css
│── script.js
│── random_forest_model.pkl
│── scaler.pkl
│── imputer.pkl
│── requirements.txt
│── README.md
```

# How to Run Locally

1. Clone the repository:
```
git clone https://github.com/Arunabha-Begin/fraud_detection_site.git
```

2. Navigate to the project folder:
```
cd fraud_detection_site
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the application:
```
python app.py
```

5. Open in browser:
```
http://127.0.0.1:5000
```

# Deployment

The project can be deployed using:
* GitHub Pages (frontend only)
* Render

# Dataset

Dataset used: Credit Card Fraud Detection Dataset
(Source: Kaggle)
The dataset is not included in this repository due to size limitations.

# Future Scope

* Real-time streaming fraud detection
* Deep learning models (LSTM, Neural Networks)
* Integration with banking systems
* Advanced dashboard for analytics

# Author
***Arunabha Maiti***

## License

This project is for educational purposes only.
