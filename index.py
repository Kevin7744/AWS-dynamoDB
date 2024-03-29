from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime

demo_table = resource('dynamodb').Table('dynamo-db-demo')


def insert():
    print(f'demo_insert')
    
    response = demo_table.put_item(
        Item={
            'customer_id': 'cus-02',
            'order_id': 'ord-3',
            'status': 'pending',
            'created_date': datetime.now().isoformat()
        }
    )
    print(f'Insert response: {response}')
    
insert()
