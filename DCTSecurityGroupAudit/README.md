The purpose of this project was to create a system to audit AWS security groups for potential security issues, such as rules that allow traffic from any IP address (0.0.0.0/0). I created automation that checked security groups automatically, compiled a report of the findings, and then sent the report via email to subscribers. 

When invoking the lambda function in the IDE, I was able to determine that the function runs correctly and was able to find security group rules that were exposed to the internet.

![2023-11-28 06_10_41-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/0ffa88f0-52e0-4c9c-bfa3-c6bf2b53b2fa)

I then uploaded the lambda function. I gave the lambda function EC2 and SNS permissions so it could execute on those services. I then created an eventbridge schedule and used the lambda function as the trigger. The eventbridge scheduler invoked the lambda function every day at 22:30. The function was invoked and it triggered an SNS topic that sent an email notifying me that one of the security group rules was open to the internet. It successfully works. 


![2023-11-28 06_12_48-Window](https://github.com/jklemens90/Python/assets/95970840/48f51c33-7ae9-4976-bf5c-3dc9b46b61c9)
