import boto3

def lambda_handler(event, context):
    ec2_resource = boto3.resource('ec2')
    
#use a for loop to iterate through all the EIP addresses. Utilize an if condition to release inactive Elastic IPs that are not associated with an EC2 instance.  
    for elastic_ip in ec2_resource.vpc_addresses.all():
        if elastic_ip.instance_id is None:
            print(f"\nNo association for elastic IP: {elastic_ip}. Releasing...\n")
            elastic_ip.release()
    
    
    
    return {
        'statusCode': 200,
        'body': 'Processed elastic IPs'
    }
