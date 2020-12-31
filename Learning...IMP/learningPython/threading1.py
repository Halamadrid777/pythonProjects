# import threading 
  
# def print_hello_three_times():
#   for i in range(3):
#     print("Hello")
  
# def print_hi_three_times(): 
#     for i in range(3): 
#       print("Hi") 

# t1 = threading.Thread(target=print_hello_three_times)  
# t2 = threading.Thread(target=print_hi_three_times)  

# t1.start()
# t2.start()


# import threading 
# import time
  
# def print_hello():
#   for i in range(4):
#     time.sleep(0.5)
#     print("Hello")
  
# def print_hi(): 
#     for i in range(4): 
#       time.sleep(0.7)
#       print("Hi") 

# t1 = threading.Thread(target=print_hello)  
# t2 = threading.Thread(target=print_hi)  
# t1.start()
# t2.start()


import threading
import time


class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      print ("Starting " + self.name + "\n")
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name + "\n")


def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s %s" % (threadName, time.ctime(time.time()), counter) + "\n")
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1.5)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")