#CSV import format
#  AAPL, Apple
#  AMD, AMD

import boto3
import csv

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('stocks')

filename = 'data.csv'

with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for line in reader:
                print(line[0])
                print(line[1])
                table.put_item(Item={'id':line[0],'description':line[1]})
