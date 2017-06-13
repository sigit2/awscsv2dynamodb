#CSV import format
# AAPL, Apple
# AMD, AMD

# Format for DynamoDB
# {"id":{"s":"AAPL"},"description":{"s":"Apple"}}
# {"id":{"s":"AMD"},"description":{"s":"AMD"}}


import csv

filename = 'data.csv'
outputfilename = 'dynamodbimport'

with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        outputfile = open(outputfilename, 'w')

        for line in reader:
                print (line)
                outputfile.write("{\"id\":{\"s\":\"" + line[0] + "\"},\"description\":{\"s\":\""+ line[1] + "\"}}" +  "\n")
				
