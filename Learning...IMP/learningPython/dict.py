
import django

x = {"a":1,"b":2,"d":{"A":2,"B":3,"C":3}}

y = x.copy()

print(y is x)

for keys, values  in x.items():
    print(keys,values)

# x.update({"G":4})
# print(y)
# print(x)
