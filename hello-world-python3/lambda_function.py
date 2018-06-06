# import json
import boto3

print('Loading function')
ec2_client = boto3.client('ec2', region_name='ap-northeast-1')


def lambda_handler(event, context):
    response = ec2_client.describe_instances()
    for ec2_group in response['Reservations']:
        for instance_info in ec2_group['Instances']:
            print(instance_info['InstanceId'])

    return True
