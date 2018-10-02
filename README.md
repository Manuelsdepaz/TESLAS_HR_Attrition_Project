# TESLAS_Attrition_Project

This project describes using machine learning (ML) for the automated identification of employees with a higher risk of attrition. Also about how to incorporate the relative costs of prediction mistakes when determining the financial outcome of using ML.

The web application can be access through the following link:

https://s3.amazonaws.com/sagemaker-hremployeeattrition-0001/website/pages/EmployeeDatabase.html

## Background

TESLAS team was created in Guatemala and it includes 6 people 5 from DEX and 1 from RPA department. As you may already know employees play a key role in companies and for that reason it is important to know when employees will leave the company. Several factors contribute to employee’s turnover. reduction turns into loss of productivity and forces to incur in replacement costs.
We are proposing the creation of a tool powered by Machine Learning technologies to solve this problem.  The project was made with Amazon Web Services provided by the Hackathon Toolkit.  By anticipating attrition companies we are reduce the cost of employee turnover.


## AI & Machine Learning Models Steps

•	Gathering Data: Watson Analytics sample data for HR Employee Attrition and Performance (1,470 rows)
•	Data Analysis: Preview analysis of the data.
•	Data Preprocessing: Handle missing data, categorical data, split model into training and test set and feature scaling.
•	Spot-check algorithms:  Evaluate the classification, clustering and regression algorithms to be used. Define the optimum model based on the data available, problem and resources available.
•	Improve Results: Analyze and Interpret the results of each model Do statistical analysis to evaluate the performance of each model and choose the best model to resolve the problem
•	Build Back-end application to process results. Integrate tool with AWS SageMaker (Machine Learning service) and S3 (repository service) with Lambda function.
•	Build Front-end application for user. Build a serverless frontend for an AWS sage maker endpoint, this new app will accept new user data and produce an on-demanded prediction which will be returned to the user’s browser.
•	Define the optimum 

## Back-end application

### XGBOOST Sagemaker model 

SageMaker provides a powerful platform for building, training, and deploying machine learning models into a production environment on AWS. The data cleaun up and preprocessing was made using the Sagemaker instances (Jupyter notebooks) and Pandas libry.
  
### AWS LAMBDA & Chalice Microframework

We used the Chalice package to produce an API Gateway endpoint to trigger a Lambda function that call our SageMaker endpoint produce a predictions to the entire dataset.

## Back-end application

Finally, we created a static HTML form in Amazon S3 to serve as the user interface for our application. The end product is a web application that can accept new user data in CSV format and produce an on-demand prediction based on that data, which is returned to the user’s browser. 
