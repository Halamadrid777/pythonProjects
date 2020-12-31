import time
import sys

start_time = time.time()
def count_down(second):
    TotalTime = second
    time_now = time.time() - start_time
    time_remaining = TotalTime - time_now
    print(time_remaining)
    if time_remaining>2:
        time.sleep(0.9)
    elif time_remaining<2:
        time.sleep(0.1)
    if time_remaining <=0.00000000000:
        sys.exit()

while True:
    count_down(20)