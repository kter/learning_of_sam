# import json
import boto3
import os
import json

print('Loading function')
ec2_client = boto3.client('ec2', region_name='ap-northeast-1')


def lambda_handler(event, context):
    if os.getenv("AWS_SAM_LOCAL"):
        backup_exclude_list = boto3.resource(
            'dynamodb',
            endpoint_url="http://docker.for.mac.host.internal:8000/"
        ).Table("backup_exclude_list")
    else:
        backup_exclude_list = boto3.resource('dynamodb').Table(os.getenv('TABLE_NAME'))
    resp = backup_exclude_list.scan()

    # print json.dumps({item['instanceid']: int(item['votes']) for item in resp['Items']})
    print(resp['Items'])

    response = ec2_client.describe_instances()
    for ec2_group in response['Reservations']:
        for instance_info in ec2_group['Instances']:
            print(instance_info['InstanceId'])

    return True
