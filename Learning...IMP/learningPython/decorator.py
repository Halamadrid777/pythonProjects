

def func(f):
    print("I am first here")
    f()
    print('I am thrid here')


@func
def func1():
    print("I am second here")


# func1()