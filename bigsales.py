# -*- coding: utf-8 -*-
"""BigSales.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tFTwuU03Vn75ZUmdIRgcPXetzMu2ct5_
"""

import pandas as pd
import numpy as np

df=pd.read_csv('Big Sales Data.csv')
df.head()

df.info()

df.columns

df.describe()

import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(df)

plt.scatter(df['Item_Weight'],df['Item_Visibility'])

#df.Item_Fat_Content.value_counts()

# df.replace({'Item_Fat_Content':{'LF':0,'low fat':0,'Low Fat':0,'reg':1,'Regular':1}},inplace=True)
#df.head()

#df.Item_Fat_Content.value_counts()

#df.Item_Type.value_counts()

#df.replace({'Item_Type':{'Fruits and Vegetables':0,'Snack Foods':0,'Household':1,'Frozen Foods':0,'Dairy':0,'Baking Goods':0,'Canned':0,'Health and Hygiene':1,'Meat':0,'Soft Drinks':0,'Breads':0,'Hard Drinks':0,'Others':2,'Starchy Foods':0,'Breakfast':0,'Seafood':0}},inplace=True)

#df.Item_Type.value_counts()

from sklearn.preprocessing import OneHotEncoder
categorical_cols = df.select_dtypes('object').columns.tolist()
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoder.fit(df[categorical_cols])
encoded_cols = list(encoder.get_feature_names_out(categorical_cols))
df[encoded_cols] = encoder.transform(df[categorical_cols])

categorical_cols

df

df.info()

df.shape()

y=df['Item_Outlet_Sales']

y

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
x_std=df[['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']]
x_std=ss.fit_transform(x_std)
df[['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']]=pd.DataFrame(x_std,columns=['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year'])
df.head()

df.drop(columns=['Outlet_Size','Outlet_Location_Type','Outlet_Type'])

df.dropna(inplace=True)

x=df.drop(['Item_Identifier','Item_Outlet_Sales','Outlet_Identifier','Outlet_Size','Outlet_Location_Type','Outlet_Type'],axis=1)
y=df['Item_Outlet_Sales']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
x_train.shape,x_test.shape,y_train.shape,y_test.shape



from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor()
rfr.fit(x_train,y_train)

pred=rfr.predict(x_test)

pred

from sklearn.metrics import mean_absolute_error,mean_squared_error

mean_absolute_error(y_test,pred)

mean_squared_error(y_test,pred)

rfr.score(x_test,y_test)

import matplotlib.pyplot as plt
plt.scatter(y_test,pred)