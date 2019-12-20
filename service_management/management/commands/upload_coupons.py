from django.core.management.base import BaseCommand

import boto3

from service_management.models import Coupons


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Uploading Coupons")
        try:
            
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table('Coupons')
            coupons = Coupons.objects.all()
            
            for item in coupons:
                
                table.put_item(
                Item={'id':str(item.id),'brnad_name':item.brand.brand_name,
                    'brand_id':str(item.brand.id),
                    'coupon_code': item.coupon_code,
                    'amount':item.currency_code +" "+str(item.denomination),
                    'denomination':item.denomination
                }
                )
                
                print("inserted: "+item.coupon_code)
        except Exception as e:
            print(str(e))