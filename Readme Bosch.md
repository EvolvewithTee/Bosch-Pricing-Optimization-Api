Bosch Pricing Optimization Project



\## Overview

This project aims to optimize product pricing for Bosch by building a data‑driven model that accounts for demand elasticity, competitor pricing, and product features (as a proxy for customer preference). The model predicts units sold and identifies profit-maximizing prices for individual products, supporting strategic pricing decisions.



---



\## Dataset

\- \*\*Dataset used:\*\* Retail Price Optimization Data (adapted from Kaggle)

\- \*\*File name:\*\* `retail\_price.csv`

\- \*\*Key columns include:\*\*

&nbsp; - `product\_id` — Unique identifier for each product

&nbsp; - `unit\_price` — Price at time of sale

&nbsp; - `qty` — Quantity sold (demand)

&nbsp; - `comp\_1`, `comp\_2`, `comp\_3` — Competitor pricing references

&nbsp; - Temporal features such as `month\_year`, `month`, `year` — Allow seasonal analysis

&nbsp; - `product\_score` — Proxy for customer preference



---



\## Jupyter Notebook (`pricing\_optimization.ipynb`)

The notebook performs the following steps:

1\. \*\*Data loading, inspection, and cleaning\*\*

2\. \*\*Feature engineering\*\* — Price gaps vs competitors, seasonality, customer preference proxy

3\. \*\*Exploratory data analysis\*\* — Price vs demand, competitor price impact, seasonality

4\. \*\*Demand elasticity estimation\*\*

5\. \*\*Demand prediction model\*\* — Linear Regression (baseline) and Random Forest (planned upgrade)

6\. \*\*Price optimization\*\* — Find revenue-maximizing price per product

7\. \*\*Model export\*\* — `pricing\_model.pkl` and `scaler.pkl` for deployment



---



\## Model Export

\- \*\*Files:\*\*

&nbsp; - `pricing\_model.pkl` — Trained Linear Regression model

&nbsp; - `scaler.pkl` — StandardScaler for preprocessing

\- Used for predictions in the Flask API and AWS deployment



---



\## Flask API (`app.py`)

This Flask application serves the trained pricing model for real-time predictions.



\### Running Locally

1\. Ensure you have Python 3 and required packages installed:

```bash

pip install flask pandas scikit-learn joblib

```

2\. Run the API:

```bash

python app.py

```

3\. Send a POST request to `/predict` with JSON input:

```json

{

&nbsp;  "unit\_price": 45.0,

&nbsp;  "comp\_1": 50.0,

&nbsp;  "comp\_2": 48.0,

&nbsp;  "comp\_3": 47.0,

&nbsp;  "month": 6

}

```

Access locally at: `http://127.0.0.1:5000/predict`



---



\## AWS Deployment

The API can be deployed on an AWS EC2 instance for public access:

\- Launch EC2 instance (Amazon Linux 2 / Ubuntu), install Python 3 and dependencies.

\- Upload project folder including `app.py`, `pricing\_model.pkl`, and `scaler.pkl`.

\- Run the Flask API on port 5000.

\- Open port 5000 in EC2 security group.





---



\## Repository

GitHub Repository: https://github.com/EvolvewithTee/bosch-pricing-optimization



---



\## Submission Checklist

\- Dataset: `retail\_price.csv`

\- Jupyter Notebook: `pricing\_optimization.ipynb`

\- Exported Model: `pricing\_model\_.pkl` and `scaler\_.pkl`

\- PowerPoint Presentation 

\- README.md 

\- Flask API Template (`app.py`)

\- GitHub repository link

\- AWS deployment link 



---



\## References

\- Galarnyk, M. W. (2025, August 4). *Train test split: What it means and how to use it.*  https://builtin.com/data-science/train-test-split

\- Louppe, G. (2015). *Understanding random forests: From theory to practice \[PhD thesis].* https://doi.org/10.48550/arXiv.1407.7502

\- Pelletier, H. (2024, March 29). *Track your ML experiments. Towards Data Science.* https://towardsdatascience.com/track-your-ml-experiments

\- Zinkevich, M. (2024). *Rules of machine learning. Google Developers.* https://developers.google.com/machine-learning/guides/rules-of-ml

\- Palei, S. (2025, May 1). *Train-test-validation split in 2025.* https://www.analyticsvidhya.com/blog/2023/11/train-test-validation-split/



