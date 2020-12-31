import json

x = dict(Name="Prajal",Address="Kathmandu")
jsonX = json.dumps(x)
print(jsonX)
print(type(jsonX))
dictX = json.loads(jsonX)
print(type(dictX))