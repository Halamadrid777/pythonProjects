# Python program showing 
# use of json package 
"""Introduction of JSON in Python :
The full-form of JSON is JavaScript Object Notation. It means that a script (executable) file which is made of text in a programming language, 
is used to store and transfer the data.
 Python supports JSON through a built-in package called json. To use this feature, we import the json package in Python script.
 The text in JSON is done through quoted string which contains value in key-value mapping within { }. It is similar to the dictionary in Python. 
 JSON shows an API similar to users of Standard Library marshal and pickle modules and Python natively supports JSON features"""
import json 

# {key:value mapping} 
a ={"name":"John", 
"age":31, 
	"Salary":25000} 

# conversion to JSON done by dumps() function 
b = json.dumps(a) 
print(b[::-1])

# printing the output 
print(a)
print(type(a))
print(b) 
print(type(b))
print(bool(a==b))
