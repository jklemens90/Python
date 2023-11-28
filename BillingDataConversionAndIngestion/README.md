The purpose of this project was to configure a lambda function that is triggered whenever a new billing CSV file is uploaded to an S3 bucket. The function will read the file, convert any billing amount not in USD into USD and then insert the record into an Aurrora Serverless database.

Beginning:
After writing the first part of the Lambda function, our Lambda function was able to read the data from the csv file in our S3 bucket.

![2023-11-28 05_18_33-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/fe003985-932f-4bda-8c4f-3436d6fb6374)

We were able to convert read the currency rates from the CSV file and then provide the conversion rate.

![2023-11-28 05_19_13-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/2a91a7a7-2a7e-4e0c-b6fa-2ca674586cd7)

Final steps:

Created an AuroraExecuteStatementPolicy so Lambda will execute the statement policy on our Aurora Serverless DB cluster

Created a LambdaSecretsManagerAccessPolicy which allows lambda to retrieve the DB Secrets ARN.

Created an S3 Put event trigger for the lambda function. The lambda function will be invoked every time a new CSV file is uploaded to S3

The newly uploaded csv file to s3 triggered the lambda function. The lambda function was then able to parse the data, finds data where the currency isnt in USD, and then normalizes the data from CAD/MXN to USD equivalent. Once that happens, SQL queries are setup and it inserts that newly transformed data into Aurora Serverless. 


![2023-11-28 05_11_47-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/d5240087-479b-4d8d-b69f-7b48c6fa91bd)
