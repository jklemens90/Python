The purpose of this project was to trigger a lambda everytime new billing data (.csv file) is uploaded (put request) to an S3 billing bucket. The lambda function will parse the CSV file contents, and if any discrepancies are found, then it will move the file to an "error" bucket.

Prequisites:
1. A lambda function written in Python to parse the data
2. S3 permissions for the lambda function
3. Two S3 buckets. A "billing" bucket and a "billing error bucket"
4. Setting up an S3 trigger for put requests.

Architecture:



![2023-11-28 18_02_16-Python+Programming+for+AWS+Slides pdf - Personal - Microsoft​ Edge](https://github.com/jklemens90/Python/assets/95970840/bc76226c-ed52-489b-ba8b-06ab1168de56)
