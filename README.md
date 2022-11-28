# Flight--Fare-Prediction:
Overview:
This is a Flask web app which predicts fare of Flight ticket.
About the Project:
The Airline Flight Fare Prediction is a Flask web application to predict airline flight fares across the Indian cities. The dataset for the project is taken from Kaggle, and it is a time-stamped dataset so, while building the model, extensive pre-processing was done on the dataset especially on the date-time columns to finally come up with a ML model which could effectively predict airline fares across various Indian Cities. The dataset had many features which had to pre-processed and transformed into new parameters for a cleaner and simple web application layout to predict the fares. The various independent features in the dataset were:

Airline: The name of the airline.

Date_of_Journey: The date of the journey

Source: The source from which the service begins.

Destination: The destination where the service ends.

Route: The route taken by the flight to reach the destination.

Dep_Time: The time when the journey starts from the source.

Arrival_Time: Time of arrival at the destination.

Duration: Total duration of the flight.

Total_Stops: Total stops between the source and destination.

Additional_Info: Additional information about the flight

Price: The price of the ticket

Algorithm used Random Forest

It is a supervised learning algorithm. The benefit of the random forest is, it very well may be utilized for both characterization and relapse issue which structure most of current machine learning framework. Random forest forms numerous decision trees, what’s more, adds them together to get an increasingly exact and stable expectation. Random Forest has nearly the equivalent parameters as a decision tree or a stowing classifier model. It is very simple to discover the significance of each element on the expectation when contrasted with others in this calculation. The regular component in these techniques is, for the kth tree, a random vector theta k is produced, autonomous of the past random vector’s theta 1, theta k-1 however with the equivalent distribution, while a tree is developed utilizing the preparation set and bringing about a classifier. x is an information vector. For a period, in stowing the random vector is created as the includes in N boxes where N is the number of models in the preparation set of information. In random split, choice includes various autonomous random whole numbers between 1 to K. The dimensionality and nature of theta rely upon its utilization in the development of a tree. After countless trees are created, they select the most famous class. These methodologies are called as random forests.

IMPLEMENTATION

We have followed following steps in our project to get to our ultimate goal of predicting flight fare:

Importing Necessary Libraries
Importing the python libraries such as pandas, matplotlib, seaborn, NumPy for reading and visualizing the dataset.

2. Reading our Dataset

We will read out dataset using pandas. As the dataset is in the excel form, we will use “pd.read_excel()”.

3. Dropping NAN Values

We will check if there are any Null values in our dataset, if we have, we will drop it using: “dropna(inplace=TRUE)”.

4. Exploratory Data Analysis

We will pre-process our dataset. We will extract day and month from the column “Date of Journey” as the model will understand numerical value, for this we will use “pd.to_datetime” for day and month column. “dt.day” and “dt.month” will extract day and month respectively from the given column.

Same process will be doing for the “dep_time” column, “Duration” column and “arrival_time” column and extract hours and min from it. After extracting day, month, hours and min, we will drop “Date of Journey”, “Duration”, “dep_time” & “arrival_time” column from our dataset.

5. Handling Categorical Data

As we know the model understands numerical value, so we will convert all the categorical data into numerical data. For this we will perform “OneHotEncoding” method to convert it to numerical data. We will make dummies using pandas and perform “OneHotEncoding” on the “Airline”, “Source” and “Destination” columns.

We will drop “AdditionalInfo” and “Route” columns as “Route” column contains same data as “Total_Stops” columns and “AdditionalInfo” column doesn’t have any additional info. “Total_Stops” column is ordinal type data so we will perform “LabelEncoder” and label each stop as 0,1,2,3,4. As the stop increases, the value also increases.

6. Test Data: Performing EDA and Feature Engineering

For the test data, we will perform same steps followed in step (2), (3), (4) and (5).

7. Feature Selection

In this process, we will find out the best feature which will contribute to our target variable.

X = “Independent Feature”

Y = “Dependent Feature” i.e., “Price” column.

We will separate all the independent features except price in the X variable and price in Y variable. For this, we will use loc & iloc method.

Now, we have used “ExtraTreesRegressor” to find more important features from the data. Use the selection variable and do fitting the X & Y features. After this we will print “feature_importance” and will get to know the important features.
We get to know that “Total_stops” is playing as the most important feature.

8. Applying Machine Learning Algorithms

We have implemented this project using Random Forest and XGBoost Regressor algorithm. The test results are mentioned below.

9. Pickling the File

Pickling the best model (Random Forest) to reuse it.
X. RESULTS
finally we get 0.79 accuracy for test data in random forest.
