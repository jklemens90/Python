The goal of this small project was to automate the process of checking for unassociated Elastic IPs and releasing them. This automation would help with unnecessary costs due to unused Elastic IPs. 

I created the lambda function, invoked it in my IDE, and was able to find all elastic IPs in my account.


![2023-11-28 06_31_07-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/2f0bdb5a-15e5-449a-a0a6-0245d2b5c961)

The lambda function was then able to identify the unused Elastic IP and release it to save costs.


![2023-11-28 06_32_30-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/24804404-3f04-494d-aae6-e4f843492f28)

Lastly I created a Eventbridge trigger for the Lambda function so it could run on a daily schedule. This was done by adding EC2 access permissions to the lambda function so the function could execute on the EC2 instances. An Eventbridge trigger was then created to run on a schedule. 
