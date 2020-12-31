import time



try:
    x = open('ma/affirm.txt','r')
    print("file opened")
except:
    print('error')


for line in x.readlines():
    print(line)
    time.sleep(2)