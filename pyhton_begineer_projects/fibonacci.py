import sys
import time
start = time.time()
def stopWatch(second):
    time_now = time.time() - start
    time.sleep(1)
    print(time_now)
    if time_now>=20.000000000000:
        sys.exit()
        


while True:
    stopWatch(20)

