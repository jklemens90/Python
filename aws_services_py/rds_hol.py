#we need to import boto3 and time module for our time based code
import boto3
import time

# Instantiate a boto3 client for RDS
rds = boto3.client('rds')


# User defined variables
username ='dctuser1'
password = '2Lxu1hRT'
db_subnet_group = 'vpc-hol'  
db_cluster_id = 'rds-hol-cluster'


# Check to see if the DB cluster exists before creating. Use exception to trigger the creation of DB cluster if not found. Call the API and pass in parameters.
try:
    response = rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
    print(f"The DB cluster named '{db_cluster_id}' already exists. Skipping creation.")
except rds.exceptions.DBClusterNotFoundFault:
    response = rds.create_db_cluster(
        Engine='aurora-mysql',
        EngineVersion='5.7.mysql_aurora.2.08.3',    
        DBClusterIdentifier=db_cluster_id, 
        MasterUsername=username,  
        MasterUserPassword=password,  
        DatabaseName='rds_hol_db',
        DBSubnetGroupName=db_subnet_group,  
        EngineMode='serverless',
        EnableHttpEndpoint=True,
        ScalingConfiguration={
            'MinCapacity': 1, # Minimum ACU
            'MaxCapacity': 8, # Maximum ACU
            'AutoPause': True,
            'SecondsUntilAutoPause': 3600  # Pause after 5 minutes of inactivity 
        }
    )
    print(f"The DB cluster named '{db_cluster_id}' has been created.")
    

    # Wait for the DB cluster to become available. Integrate wait whie loop. This calls teh describe_db_clusters API and then prints the current status of the DB cluster.
    while True:
        response = response = rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
        status = response['DBClusters'][0]['Status']
        print(f"The status of the cluster is '{status}'")
        if status =='available':
            break
        
        print("Waiting for the DB Cluster to become available...")
        time.sleep(40)    

 
   
   
# Modify the DB cluster. Update the scaling configuration for the cluster 
response = rds.modify_db_cluster(
        DBClusterIdentifier=db_cluster_id, 
        ScalingConfiguration={
            'MinCapacity': 1, # Minimum ACU 
            'MaxCapacity': 16, # Maximum ACU
            'SecondsUntilAutoPause': 600  # Pause after 10 minutes of inactivity 
        }
    )
    
print(f"Updated the scaling configuration for DB cluster '{db_cluster_id}'.")

  
  
  
# Delete the DB cluster. Utilized the response variable and then called the delete_db_cluster API. Skipped the snapshot prior to deletion.
response = rds.delete_db_cluster(
        DBClusterIdentifier=db_cluster_id, 
        SkipFinalSnapshot=True
    )
    
print(f"The '{db_cluster_id}' is being deleted.")       
   