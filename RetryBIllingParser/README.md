Part 2 of the BillingBucketParser project. 

The purpose of this project was to add an additional feature to the CSV billing validation project (BillingBucketParser). A feature was added to call a third party API in order to get real-time international tax data.  The idea was that if there was an error with the BillingBucketParser's function calling the "get_international_taxes" API, then this would publish to an SNS topic. An email would then be sent out to notify the issue.  A subscribed SQS queue would then trigger the "RetryBillingParser" function. This function would then re-attempt processing the csv files and data validation.



![2023-11-28 06_51_57-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/89197cba-d260-4f70-9326-ada41da7b2cd)

![2023-11-28 06_52_59-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/521f9174-3045-4278-b3be-9a4ae0b44da3)
