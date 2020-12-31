# # import time
# # import sys


# # def stopwatch(seconds):
# #     start = time.time()
# #     elapsed = 0
# #     while seconds>elapsed:
# #         elapsed = time.time() - start
# #         if seconds >24:
# #             print(elapsed)
# #     sys.exit()


# # stopwatch(25)

# # # 25.000139236450195
# import time

# while True:
#   localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result)
#   time.sleep(1)

# # print(time.localtime())


import time
def stopWatch(sec):

  start_time = time.time()
  elapsed =0
  while elapsed <20:
    elapsed = time.time()-start_time
    time.sleep(1)
    print(elapsed)


stopWatch(20)