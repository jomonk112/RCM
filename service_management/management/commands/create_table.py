from django.core.management.base import BaseCommand

import boto3


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("creating table Coupons")
        try:
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.create_table(
            TableName='Coupons',
            KeySchema=[
                {
                    'AttributeName': 'coupon_code',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'denomination',
                    'KeyType': 'RANGE'
                },
            ],
            AttributeDefinitions=[
                
                {
                    'AttributeName': 'coupon_code',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'denomination',
                    'AttributeType': 'N'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
            )
            table.meta.client.get_waiter('table_exists').wait(TableName='users')
            print("table created")
        except Exception as e:
            print(str(e))
        