import threading
import string

ascciLower = [x for x in string.ascii_lowercase]
ascciUpper = [x for x in string.ascii_uppercase]
def print_ascci_lower():
    for x in ascciUpper:
        threadLock.acquire() #which essentialy means don't let another thread run until this thread finishes
        print(x)
        threadLock.release()

def print_ascci_upper():
    for x in ascciLower:
        threadLock.acquire()
        print(x)
        threadLock.release()

def print_ascci_lower1():
    for x in range(0,28):
        threadLock.acquire()
        print(x)
        threadLock.release()

def print_ascci_upper1():
    for x in range(50,80):
        # threadLock.acquire()
        print(x)
        # threadLock.release()
threadLock = threading.Lock()
t1 = threading.Thread(target=print_ascci_lower)
t2 = threading.Thread(target=print_ascci_upper)
t3 = threading.Thread(target=print_ascci_lower1)
t4 = threading.Thread(target=print_ascci_upper1)

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()