# import json
# TODO Add test
import boto3
import os

print('Loading function')


def lambda_handler(event, context):
    if os.getenv("AWS_SAM_LOCAL"):
        backup_exclude_list = boto3.resource(
            'dynamodb',
            endpoint_url="http://docker.for.mac.host.internal:8000/"
        ).Table("backup_exclude_list")
        sqs = boto3.resource('sqs',
                             endpoint_url='http://docker.for.mac.host.internal:9324',
                             region_name='elasticmq',
                             aws_secret_access_key='x',
                             aws_access_key_id='x',
                             use_ssl=False)
    else:
        backup_exclude_list = \
            boto3.resource('dynamodb').Table(os.getenv('TABLE_NAME'))
        sqs = boto3.resource('sqs',
                             region_name='ap-northeast-1',)
    resp = backup_exclude_list.scan()['Items']
    try:
        queue = sqs.get_queue_by_name(QueueName='createSnapshot')
    # AWS.SimpleQueueService.NonExistentQueueが返るが例外ではない？ためexceptに設定できない
    except:
        queue = sqs.create_queue(QueueName='createSnapshot')

    # print("instances")
    # TODO classified
    ec2_client = boto3.client('ec2', region_name='ap-northeast-1')
    response = ec2_client.describe_instances()
    instances = []
    for ec2_group in response['Reservations']:
        for instance in ec2_group['Instances']:
            # print(instance['InstanceId'])
            instances.append(instance['InstanceId'])

    print("exclude instances")
    for exclude in resp:
        # print(exclude['instanceid'])
        # excludes.append(exclude['instanceid'])
        try:
            instances.remove(exclude['instanceid'])
        except ValueError:
            print('Exclude instance non exist error ({0})'.format(exclude))
            pass

    print(instances)
    for instance in instances:
        response = queue.send_message(MessageBody=instance)

    return instances
