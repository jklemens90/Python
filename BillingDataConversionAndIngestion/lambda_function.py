# Required libraries
import boto3
import io
import csv
import logging

# Constants - database and credentials details, and currency conversion rates. Create a dictionary called currency_conversion_to_usd with different currencies and their conversion rates. 
currency_conversion_to_usd = {'USD': 1, 'CAD': 0.79, 'MXN': 0.05}  
database_name = 'rds_hol_db'
secret_store_arn = 'arn:aws:secretsmanager:us-east-1:046068811061:secret:rds-db-credentials/cluster-YXNROE3V7XZFV324IQYB2QDKGI/dctuser1/1700128081064-7icnD9'
db_cluster_arn = 'arn:aws:rds:us-east-1:046068811061:cluster:rds-hol-cluster'


# Boto3 clients for AWS services
s3_client = boto3.client('s3')
rds_client = boto3.client('rds-data')


# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Function to process each record/row from the CSV file. Include all our variables for each record. 
def process_record(record):
    id, company_name, country, city, product_line, item, bill_date, currency, bill_amount = record
    bill_amount = float(bill_amount)


    # Convert the bill amount to USD using conversion rates. This will access the dictionary and get the corresponding currency in the dictionary.
    usd_amount = 0
    rate = currency_conversion_to_usd.get(currency)
    if rate:
        usd_amount = bill_amount * rate
    else:
        # If no conversion rate is found for the currency, log an info message
        logger.info(f"No rate found for currency: {currency}.")
  
   # Prepare SQL statement with placeholders for inserting record into the billing_data table
    sql_statement = ("INSERT IGNORE INTO billing_data " 
                        "(id, company_name, country, city, product_line, "
                        "item, bill_date, currency, bill_amount, bill_amount_usd) "
                     "VALUES (:id, :company_name, :country, :city, :product_line, "
                             ":item, :bill_date, :currency, :bill_amount, :usd_amount)"
                    )
   
   # Prepare parameters for SQL statement
    sql_parameters = [
        {'name':'id', 'value':{'stringValue': id}},
        {'name':'company_name', 'value':{'stringValue': company_name}},
        {'name':'country', 'value':{'stringValue': country}},
        {'name':'city', 'value':{'stringValue': city}},
        {'name':'product_line', 'value':{'stringValue': product_line}},
        {'name':'item', 'value':{'stringValue': item}},
        {'name':'bill_date', 'value':{'stringValue': bill_date}},
        {'name':'currency', 'value':{'stringValue': currency}},
        {'name':'bill_amount', 'value':{'doubleValue': bill_amount}},
        {'name':'usd_amount', 'value':{'doubleValue': usd_amount}}
    ]
   
   
   # Execute the SQL statement and log the response
    response = execute_statement(sql_statement, sql_parameters)
    logger.info(f"SQL execution response: {response}")
   
# Function to execute SQL statement. Tries to execute the statements and calls the RDS client to get DB credentials. Utilizes exception block to log errors if we cant connection to MySQL instance.
def execute_statement(sql, sql_parameters):
    try:
        response = rds_client.execute_statement(
            secretArn=secret_store_arn,
            database=database_name,
            resourceArn=db_cluster_arn,
            sql=sql,
            parameters=sql_parameters
        )
    except Exception as e:
        logger.error("ERROR: Could not connect to Aurora Serverless MySQL instance.")
        return None

    return response

#This lambda function will be invoked by new records that are added. The object will be read from S3 and then be decoded. A csv reader will then process the CSV data.


def lambda_handler(event, context):
    try:
        # Get the bucket name and file name from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        s3_file = event['Records'][0]['s3']['object']['key']
        

        # Read the file from S3. We're getting the object by passing the bucket name and the S3 file. Then decode the data. 
        response = s3_client.get_object(Bucket=bucket_name, Key=s3_file)
        data = response['Body'].read().decode('utf-8')



        # Use csv reader to process the CSV data. Use "next" because we dont want to process the first line which is the header line of the record.
        csv_reader = csv.reader(io.StringIO(data))
        next(csv_reader)



        # Process each record in the CSV file. Use a for loop to iterate through each record. Print everytime a record is processed. 
        for record in csv_reader:
            process_record(record)
            
        logger.info("Lambda has finished execution.")
   
    except Exception as e:
        # If an unexpected error occurs, log an error message
        logger.error(f"ERROR: unexpected error: {e}")

   
   
   
   





   
