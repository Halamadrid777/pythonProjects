

# # import turtle

# # turtle.pensize(4)
# # turtle.pencolor('red')
# # count = 0
# # y = 90
# # x = 100
# # while True:

# #     turtle.forward(x)
# #     turtle.right(y)
# #     # turtle.forward(100)
# #     # turtle.right(90)
# #     # turtle.forward(100)
# #     # turtle.right(90)
# #     # turtle.forward(100)
# #     # count +=1
# #     # if count == 100:
# #     #     break

# # turtle.mainloop()


# def addTwo(x):
#     return x+2


# z = addTwo(4)
# print(z)


# def isZeros(li):
#     check = True
#     for element in li:
#         if element != 0:
#             check = False
#             break
#     if check:
#         print("True")
#     else:
#         print("False")

# isZeros([0,0,1,0,0])  # Calling this will result in True being printed to the screen


# def askQuestions():
#     name = input("Please type your name: ")
#     age = input("Please type your age: ")
#     country = input("Please type where you are from: ")
#     print("Your name is", name, "you are", age, "old and you are from", country + '.')

# for i in range(5):
#     askQuestions()  # This will call the function 5 times

def myfunc():
    try:
        f = open("x.txt","w")
    except:
        print(FileNotFoundError)

    lines = [x for x in range(0,100)]
    print(lines)

    if "hello world" in  lines:
        print("Harmful content")


    for line in lines:
        f.write(str(line)+"  ")

    f.writelines("x")