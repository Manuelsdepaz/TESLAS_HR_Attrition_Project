# TESLAS_Attrition_Project

This project describes using machine learning (ML) for the automated identification of employees with a higher risk of attrition. Also about how to incorporate the relative costs of prediction mistakes when determining the financial outcome of using ML.

The web application can be access through the following link:

https://s3.amazonaws.com/sagemaker-hremployeeattrition-0001/website/pages/EmployeeDatabase.html

## Background

TESLAS team was created in Guatemala and it includes 6 people 5 from DEX and 1 from RPA department. As you may already know employees play a key role in companies and for that reason it is important to know when employees will leave the company. Several factors contribute to employee’s turnover. reduction turns into loss of productivity and forces to incur in replacement costs.
We are proposing the creation of a tool powered by Machine Learning technologies to solve this problem.  The project was made with Amazon Web Services provided by the Hackathon Toolkit. 


## AI & Machine Learning Models Steps

* Gathering Data: [Watson Analytics sample data for HR Employee Attrition and Performance (1,470 rows)](https://github.com/Manuelsdepaz/TESLAS_HR_Attrition_Project/tree/test/HR%20Attrition%20Sample%20Data)
*	Data Analysis: Preview analysis of the data.
*	Data Preprocessing: Handle missing data, categorical data, split model into training and test set and feature scaling.
*	Spot-check algorithms:  Evaluate the classification, clustering and regression algorithms to be used. Define the optimum model based on the data available, problem and resources available.
*	Improve Results: Analyze and Interpret the results of each model Do statistical analysis to evaluate the performance of each model and choose the best model to resolve the problem
*	Build Back-end application to process results. Integrate tool with AWS SageMaker (Machine Learning service) and S3 (repository service) with Lambda function.
*	Build Front-end application for user. Build a serverless frontend for an AWS sage maker endpoint, this new app will accept new user data and produce an on-demanded prediction which will be returned to the user’s browser.
*	Define the cutoff that minimize the cost of attrition.

## [Back-end application](https://github.com/Manuelsdepaz/TESLAS_HR_Attrition_Project/tree/test/Back-End)

### [XGBOOST Sagemaker model](https://github.com/Manuelsdepaz/TESLAS_HR_Attrition_Project/tree/test/Back-End/Sage%20Maker%20Model)

We chose XGBOOST model because it handles a variety of data types, relationships, distributions and also  a  large number of hyperparameters that can be tuned for improved fits and accuracy. Boosting also allows us to reduce bias and has been successfully used in many machine learning competitions . 
SageMaker provides a powerful platform for building, training, and deploying machine learning models into a production environment on AWS. The data clean up and preprocessing, building, training was made using the Sagemaker instances (Jupyter notebooks) and Pandas libary. We set up a Sagemaker enpoint and transform it into a web application that accepts end-user input data.
  
### [AWS LAMBDA & Chalice Microframework](https://github.com/Manuelsdepaz/TESLAS_HR_Attrition_Project/tree/test/Back-End/AWS%20Lamda%20Function%20-%20Chalice%20Package)

We used the Chalice package to produce an API Gateway endpoint to trigger a Lambda function that call our SageMaker endpoint and produce  predictions to the entire dataset. The serverless capabilities of Amazon Simple Storage Service (S3), Amazon API Gateway, and AWS Lamda help us to deploy a  web application using a CSV file stored in a S3 bucket.

The preprocessing of the new input data is done through the Lamda function. Lambda function removed the unnecesary columns and convert the categorical into dummy variables. Lambda is also able to manipulate the columns and prepare the date before call the the Sagemaker endpoint. Finally the AWS Lamda function uploads the new CSV dataset to the S3 repository. To combine the AWS services we previusly created IAM roles and assigned the permission for each service.


## [Front-end application](https://github.com/Manuelsdepaz/TESLAS_HR_Attrition_Project/tree/test/Front-End)

Finally, we created a static HTML form in Amazon S3 to serve as the user interface for our application. The end product is a web application that can accept new user data in CSV format and produce an on-demand prediction based on that data, which is returned to the user’s browser.  The website loads the new CSV using Jquery datatable and Jquery csv. The user is able to filter the data, search by employe, sort and is also able to download the CSV.
