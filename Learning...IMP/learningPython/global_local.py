# x = "global"

# def foo():
#     print("x inside:", x)


# foo()
# print("x outside:", x)

y = "global"
def halamadrid():
    y = "local"
    print(y)

halamadrid()
print(y)