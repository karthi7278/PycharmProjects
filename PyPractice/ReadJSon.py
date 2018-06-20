import json

json_data=open("D:/sparkecosystem/data/test.json")
#print(json_data.read())
abc=json.load(json_data)
json_data.close()
print(abc)