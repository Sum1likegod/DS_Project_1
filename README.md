# Customer Support Data Optimizer

## 📌 Project Overview
This project is a Python-based data processing tool designed to automate the cleaning and analysis of customer support logs. Developed as a bridge between my experience in **Process Execution at Cognizant** and **IT Development**, this script transforms messy, raw interaction data into actionable insights.

## 🛠️ Key Technical Features
- **Data Normalization:** Automatically handles inconsistent string formatting (case sensitivity and trailing whitespaces).
- **Missing Data Imputation:** Uses `Pandas` to identify `NaN` values and fill them with calculated means to maintain dataset integrity.
- **Automated Categorization:** Implements logic to group tickets by department.
- **Data Visualization:** Generates frequency distribution charts using `Matplotlib`.

## 🚀 How It Works
The script follows an **ETL (Extract, Transform, Load)** workflow:
1. **Extract:** Loads raw data from an excel file, CSV or Python Dictionary.
2. **Transform:** Standardizes text and fixes missing numerical values.
3. **Load:** Outputs a cleaned DataFrame and saves a visualization of the results.

## 📊 Sample Output
| Employee | Score | Department | Issue |
| :--- | :--- | :--- | :--- |
| Amit | 8.0 | Tech | login error |
| Suresh | 10.0 | Tech | payment failed |
| Priya | 7.0 | Tech | slow website |

## 💻 Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy, Matplotlib, Pathlib