import json
import boto3

AMI = 'ami-0022f774911c1d690'
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'EC2Instance'
REGION = 'us-east-1'
 
 
ec2 = boto3.client('ec2', region_name=REGION)
def lambda_handler(event, context):
    
    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        MaxCount=1,
        MinCount=1
    )

    print ("New instance created:")
    instance_id = instance['Instances'][0]['InstanceId']
    print (instance_id)

    return print("ID of created Ec2Instance:", instance_id)

