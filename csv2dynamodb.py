#CSV import format
#  AAPL, Apple
#  AMD, AMD


# Format for DynamoDB
# {"id":{"s":"AAPL"},"description":{"s":"Apple"}}
# {"id":{"s":"AMD"},"description":{"s":"AMD"}}



import csv

filename = 'data.csv'
outputfilename = 'dynamodbimport'

def formatStr(name, vtype, value):
        return "\"" + name + "\":{\"" + vtype + "\":\"" + value + "\"}"


with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader)
        print(headers)

        outputfile = open(outputfilename, 'w')
        loop = 0
        for line in reader:
                outline = "{"
                for header in headers:
                        print(header)
                        print(line)
                loop = loop + 1
                #outputfile.write("{" + formatStr("id", "s", line[0]) + "," + formatStr("description","s", line[1]) +"}" +  "\n")
