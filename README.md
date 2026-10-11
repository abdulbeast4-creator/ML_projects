# AutoML Desktop App

A desktop tool that trains and compares several scikit-learn classifiers on a CSV dataset without writing code.

<!-- TODO: add a screenshot: ![Score table](docs/screenshot.png) -->

## Features

- Upload a CSV and preview it in a table
- Choose the target (output) column; the rest become features
- Train 8 classifiers in one run: Logistic Regression, SVM, Random Forest, Decision Tree, K-Nearest Neighbors, Gaussian / Multinomial / Bernoulli Naive Bayes
- Compare models by test accuracy (70/30 split) and mean 5-fold cross-validation score
- Plot a learning curve for any trained model

## Tech stack

Python, PyQt5, scikit-learn, pandas, NumPy, matplotlib

## Run locally

```bash
git clone https://github.com/abdulbeast4-creator/ML_projects.git
cd ML_projects
pip install pyqt5 scikit-learn pandas numpy matplotlib
python main_window.py
```

## Project structure

| File | Purpose |
|---|---|
| `main_window.py` | App entry point and page navigation |
| `upload_your_data.py` | CSV upload, preview, target column selection |
| `class_and_reg_algos.py` | Classifier and regressor definitions |
| `train_your_model.py` | Train/test split, fitting, cross-validation |
| `display_scores_in_table.py` | Score comparison table |
| `display_learning_curve.py` | Learning curve plot |
| `MyApp.spec` | PyInstaller build spec |

## Planned

- Regression mode (regressors are defined but not wired into the UI yet)
- Data preprocessing (missing values, categorical encoding)

## Authors

Built jointly by [Abdul Rashid](https://github.com/abdulbeast4-creator) and [Santhosh](https://github.com/Santhosh-cobbler).
