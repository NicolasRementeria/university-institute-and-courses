import json
import csv

with open("./thesaurus_dict.json") as jsonFile:
    jsonContent = json.load(jsonFile)

with open("./thesaurus_csv.csv", "a+") as csvFile:
    csvFile.write("Expression;Definition\n")
    for expression in jsonContent.keys():
        csvFile.write("%s;%s\n" % (expression, jsonContent[expression]))



# import csv
# toCSV = [{'name':'bob','age':25,'weight':200},
#          {'name':'jim','age':31,'weight':180}]
# with open('people.csv', 'w', encoding='utf8', newline='') as output_file:
#     fc = csv.DictWriter(output_file, 
#                         fieldnames=toCSV[0].keys()
#                        )
#     fc.writeheader()
#     fc.writerows(toCSV)