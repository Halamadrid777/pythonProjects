# Python program showing that 
# json support different primitive 
# types 
import demjson
import json 

# list conversion to Array 
print(json.dumps(['Welcome', "to", "GeeksforGeeks"])) 


# tuple conversion to Array 
print(json.dumps(("Welcome", "to", "GeeksforGeeks"))) 

# string conversion to String 
print(json.dumps("Hi")) 

# int conversion to Number 
print(json.dumps(123)) 

# float conversion to Number 
print(json.dumps(23.572)) 

# Boolean conversion to their respective values 
print(json.dumps(True)) 
print(json.dumps(False)) 

# None value to null 
print(json.dumps(None)) 


json_var =""" 
{ 
	"Country": { 
		"name": "INDIA", 
		"Languages_spoken": [ 
			{ 
				"names": ["Hindi", "English", "Bengali", "Telugu"] 
			} 
		] 
	} 
} 
"""
var = json.loads(json_var) 
print(var)
print(type(var))

var11 = '{"a":0, "b":1, "c":2, "d":3, "e":4}'
text = demjson.decode(var11) 
print(type(text))
