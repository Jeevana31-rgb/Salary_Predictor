import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
data = pd.read_csv('Salary_Data.csv')
x=data[['YearsExperience']]
y=data.Salary
model=LinearRegression()
model.fit(x,y)
joblib.dump(model, 'salary_model.pkl')
print('Model Saved Successfully')