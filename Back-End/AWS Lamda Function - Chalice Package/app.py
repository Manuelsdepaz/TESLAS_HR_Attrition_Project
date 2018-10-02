try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
# IMPORT LIBRARIES
from io import BytesIO
import csv
import io
# PANDA AND BOTO3 MUST BE INCLUIDED IN THE REQUIREMENTS TEXT FILE
import pandas as pd
import boto3
import numpy as np
from decimal import Decimal
import json
import sys, os, base64, datetime, hashlib, hmac 
from chalice import Chalice, Response
from chalice import NotFoundError, BadRequestError
import sys, os, base64, datetime, hashlib, hmac 

app = Chalice(app_name='XGBOOST-attrition-prediction')
# ASS THE AWS RESOURCES
try:
    from urlparse import urlparse, parse_qs
except ImportError:
    from urllib.parse import urlparse, parse_qs
    
client = boto3.client('sagemaker-runtime')
session = boto3.session.Session(region_name='us-east-1')
s3client = session.client('s3')

#GET API - CHALICE
@app.route('/predict')
def handle_data():
    # READ EMPLOYEE DATA BASE FROM S3 BUCKTE
    resedb = s3client.get_object(Bucket='sagemaker-hremployeeattrition-0001', Key='database/EmployeeDatabase.csv')
    dataset = pd.read_csv(io.BytesIO(resedb['Body'].read()), encoding='utf8')

    #DATA SET PREPROCESSING (DROP COLUMNS NOT NEEDED FOR THE MODEL)
    dataset.drop(['BusinessTravel', 'Attrition','EmployeeNumber','Atrition_Prediction_Value', 'Risk', 'EmployeeCount','StandardHours','Over18','JobRole'],axis = 1, inplace=True)
    #TRANSFORM CATEGORICAL COLUMNS INTO DUMMY VARIABLES FOR THE MODEL TO WORK PROPERLY
    cols_to_transform = ['Department', 'EducationField', 'Gender' , 'MaritalStatus' , 'OverTime']
    dataset = pd.get_dummies(dataset, columns = cols_to_transform )
    # RUN TRAINED MODEL FROM RUNNING SAGEMAKER ENDPOINT
    input_file = StringIO()
    dataset.to_csv(input_file, header=False, index=False)
    res = client.invoke_endpoint(
                    EndpointName='xgboost-2018-09-30-20-27-49-609',
                    Body=input_file.getvalue(),
                    ContentType='text/csv',
                    Accept='Accept'
                )
    # TRANSFORM PREDICTIONS INTO AN ARRAY, DATA FRAME
    predictions_array = np.fromstring(res ['Body'].read(), sep=',')
    dtattrition = pd.DataFrame(predictions_array)
    dtattrition.columns = ['Atrition_Prediction_Value']
    dtattrition = pd.DataFrame(dtattrition) 
    # DEFINE THE CUTOFF AND THE INTERPRETAION FOR THE RESULT OF THE MODEL
    def f(row):
        if Decimal(row[0]) > 0.21:
            val = "High"
        else:
            val = "Low"
        return val
    dtattrition['Risk']= dtattrition.apply(f, axis=1) 
    # APPLY SOME FORMATTING TO THE PREDICTIONS OUTPUT
    dtattrition['Atrition_Prediction_Value'] = (dtattrition['Atrition_Prediction_Value'].round(4))*100
    dtattrition['Atrition_Prediction_Value'] = dtattrition['Atrition_Prediction_Value'].astype(str)  + "%"
    dtattrition = pd.DataFrame(dtattrition)
    # READ ORINGINAL DATABASE AND LEFT JOIN WITH THE NEW PREDICTIONS OUTPUT
    resedb = s3client.get_object(Bucket='sagemaker-hremployeeattrition-0001', Key='database/EmployeeDatabase.csv')
    dataset = pd.read_csv(io.BytesIO(resedb['Body'].read()), encoding='utf8')
    # DROP OLD COLUMNS RESULT AND REPLACE IT WITH THE NEW PREDICTIONS
    dataset.drop(['Atrition_Prediction_Value', 'Risk'],axis = 1, inplace=True)
    dataset = pd.concat([dtattrition,dataset], axis=1)
    input_file2 = StringIO()
    dataset.to_csv(input_file2,header=True, index=False)
    # UPLOAD RESULTING MODEL IN AN S3 BUCKET REPLACING THE OLD EMPLOYEE DATABASE FILE 
    ress3 = s3client.put_object(
                ACL='public-read-write',
                Bucket='sagemaker-hremployeeattrition-0001',
                Key='database/EmployeeDatabase.csv',
                Body=input_file2.getvalue(),
                ContentType='text/csv'
            )
    return Response(body='XGBOOST model run sucessfully',status_code=200,headers={'Content-Type': 'text/plain'})