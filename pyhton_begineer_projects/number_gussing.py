import random
import sys



base = 0
high = 101
random_num = random.randint(base,high)
while True:
    input_num = int(input("Guess a number between "+str(base)+" & "+str(high)+ " :"))
    if input_num > random_num:
        print("High! try smaller ones")
    elif input_num < random_num:
        print("Low!!! Try higher ones")
    else:
            print("you have guessed the right num "+ str(random_num))
            sys.exit()


