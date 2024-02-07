import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd

#importing dataset
data_set=pd.read_csv('FIFA17_official_data.csv')

print("Before Cleaning:")
print(data_set.head())
#checking for missing values
data_set.dropna(subset=['age','Value'],inplace=True)
#removing duplicate rows
data_set.drop_duplicates(inplace=True)

data_set['Value']=data_set['Value'].clip(lower=0,upper=100000000)
data_set['Contract Valid Until']=data_set['Contract Valid Until'].astype(int)

print("\nAfter Cleaning:")
print(data_set.head())

#extracting independent and dependent variable
x=data_set[['age','performance_statistics']].values
y=data_set['market_value'].values

#Splitting the dataset into training and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.25,random_state=42)

#feature scaling
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

#Fitting Decision Tree classifier to the training set
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=100,random_state=42)
regressor.fit(x_train,y_train)

#Predicting the test set result
y_pred=regressor.predict(x_test)

#creating confusion matrix
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
mae=mean_absolute_error(y_test,y_pred)
rmse=np.sqrt(mean_squared_error(y_test,y_pred))
r_squared=r2_score(y_test,y_pred)
print("Mean Absolute Error:",mae)
print("Root Mean Squared Error:",rmse)
print("R-squared",r_squared)

mtp.figure(figsize=(8,6))
mtp.scatter(y_test,y_pred,color='blue',alpha=0.5)
mtp.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],'k--',lw=2)
mtp.xlabel('Actual Market Value')
mtp.ylabel('Predicated Market Value')
mtp.title('Actual vs Predicted Market Value')
mtp.grid(True)
mtp.show()
