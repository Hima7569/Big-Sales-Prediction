Project Overview
This project analyzes a dataset of sales transactions to predict the Item_Outlet_Sales using a Random Forest Regressor. The dataset contains various features such as item characteristics and outlet information.

Dataset
Dataset File: "Big Sales Data.csv"
Features:
Item_Identifier: Unique identifier for the product.
Item_Weight: Weight of the product.
Item_Fat_Content: Categorical variable representing the fat content of the product.
Item_Visibility: The percentage of total display area of all products in a store allocated to this particular product.
Item_Type: Categorical variable representing the category of the product.
Item_MRP: Maximum Retail Price of the product.
Outlet_Identifier: Unique identifier for the outlet.
Outlet_Establishment_Year: The year in which the outlet was established.
Outlet_Size: Size of the outlet.
Outlet_Location_Type: Location type of the outlet.
Outlet_Type: Type of the outlet.
Item_Outlet_Sales: Sales of the product in the particular outlet.
Steps and Explanations
Import Libraries: Necessary libraries such as pandas, numpy, matplotlib, seaborn, and scikit-learn are imported.

Load Dataset: The dataset is loaded into a pandas DataFrame.

Initial Data Exploration:

Display the first few rows of the dataset to understand its structure.
Use info() to get a concise summary of the DataFrame.
List the columns and generate summary statistics using describe().
Visualizations:

Use seaborn's pairplot to visualize pairwise relationships in the dataset.
Create a scatter plot to explore the relationship between Item_Weight and Item_Visibility.
Data Preprocessing:

Categorical Data Handling:
Initially explore the categorical column Item_Fat_Content.
Replace values in Item_Fat_Content for consistency and recheck value counts.
Explore Item_Type and replace values for simplification (commented code).
Encode categorical columns using OneHotEncoder.
Standardization:
Standardize numerical columns Item_Weight, Item_Visibility, Item_MRP, and Outlet_Establishment_Year using StandardScaler.
Feature Selection:

Drop columns that are not needed or have been processed (Outlet_Size, Outlet_Location_Type, Outlet_Type).
Remove rows with missing values.
Defining Features and Target:

Define x (features) by dropping irrelevant columns.
Define y (target) as Item_Outlet_Sales.
Train-Test Split:

Split the data into training and testing sets with an 80-20 ratio using train_test_split.
Model Training:

Use RandomForestRegressor from scikit-learn to train the model on the training data.
Predictions:

Predict the Item_Outlet_Sales for the test set using the trained model.
Evaluation:

Calculate evaluation metrics such as Mean Absolute Error (MAE) and Mean Squared Error (MSE).
Print the R-squared score to assess model performance.
Visualize the predictions by plotting the true sales values against the predicted values using a scatter plot.
Conclusion
This project demonstrates a complete workflow for predicting sales using a regression model. It includes data exploration, preprocessing, model training, and evaluation, providing a comprehensive approach to handling sales data for predictive analytics.
