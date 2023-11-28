The purpose of this project was to utilize EventBridge scheduler to trigger a lambda function at daily intervals. This lambda function would then create a snapshot of our target VolumeID every day at 2 AM. 

Prequisites:
1. A lambda function created in Python
2. An EC2 instance with a volume we can create a snapshot for
3. EC2 IAM permissions for our lambda function so it can perform the snapshot.

Architecture:

![2023-11-28 18_08_49-Window](https://github.com/jklemens90/Python/assets/95970840/ab100298-a669-4b08-8dc4-6c56879e3ae1)
