# import string


# listofascci = [x for x in string.ascii_letters]
# # print(listofascci)


# # list_of_lower = [lambda: if string.ascii_uppercase not in string.ascii_letters]


# if string.ascii_lowercase not in string.ascii_letters:
#     print("x")

x = lambda x,y,z: x+y+z
print(x(4,5,6))

odds = [x for x in range(1,101) if x%2!=0]
print(odds)

y = lambda x, y:x + y
print(y(1,2))