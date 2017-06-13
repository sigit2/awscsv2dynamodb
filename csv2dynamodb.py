#CSV import format
#  AAPL, Apple
#  AMD, AMD


# Format for DynamoDB
# {"id":{"s":"AAPL"},"description":{"s":"Apple"}}
# {"id":{"s":"AMD"},"description":{"s":"AMD"}}


# TODO - make even more generic by reading header line in from CSV and looping through each column.


import csv

filename = 'data.csv'
outputfilename = 'dynamodbimport'

def formatStr(name, type, value):
        return "\"" + name + "\":{\"" + type + "\":\"" + value + "\"}"


with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        outputfile = open(outputfilename, 'w')

        for line in reader:
                outputfile.write("{" + formatStr("id", "s", line[0]) + "," + formatStr("description","s", line[1]) +"}" +  "\n")
