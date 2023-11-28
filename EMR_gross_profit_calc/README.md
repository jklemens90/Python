Architecture-

1. Glue crawlers parsed CSV data from the dct-billing-processed and dct-billing-data-lake S3 bucket. 

2. The glue crawlers then populated the data into the glue data catalog.
   
3. Within this Glue Data Catalog, they created three separate tables: billing, units sold, production costs. These tables were created automatically by the glue crawlers.
   
4. I then used the EMR Cluster to run the pyspark script. The cluster then processed the data within the glue data catalog.
   
5. To process the data, our EMR cluster used proper permissions from IAM and Lake Formation to access the data within the glue data catalog.
   
6. Once permissions were given I was then able to generate the gross profit report using the pysparks script. That report was then stored in the dct-billing-data-lake S3 bucket. 

![2023-11-28 05_36_15-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/b92d2ad0-b134-4418-b0bf-1f111d64c90b)

Steps:

1. Started a pyspark session.
2. Showed our tables.

   ![2023-11-28 05_38_20-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/95eae013-d84c-4127-9cdc-09b969378d9c)

![2023-11-28 05_39_06-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/a507a36c-2d82-4139-8530-56bd35c8229e)

![2023-11-28 05_39_29-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/0276b0f9-91b4-42cf-a442-0341c270faf6)

3. Then merged all the tables together with the following code:

   ![2023-11-28 05_40_13-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/ee34f8d6-3ac8-434d-96d4-2d4c4f7f540f)

![2023-11-28 05_41_04-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/46379d3e-989b-4919-b960-c3189ac6f637)

4. Wrote code that would calculate gross profit and add a gross profit column.

![2023-11-28 05_42_32-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/48ba88a4-d28c-430d-9e47-8fa6668cb31c)

5. We uploaded our Pyspark script to Step 1 for the EMR cluster. The Pyspark script was executed and it generated the gross profit report in our S3 bucket.

   ![2023-11-28 05_43_51-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/3530e2f6-322f-4e9d-9f08-5b9bef5cff2c)
   
![2023-11-28 05_44_22-Python Programming for AWS- Learn Python with AWS and Boto3 - Google Docs](https://github.com/jklemens90/Python/assets/95970840/b14465a9-4001-4637-acaf-c14e5dd9c95d)

