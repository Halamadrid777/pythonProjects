# import requests
# import time 
from plyer import notification

# count = 0

# while True:
#     try:
#         response = requests.get('https://www.youtube.com/')
#         print('Internet is on')
#         count+=1
#     except:
#         print('internet is interupeed')
#         # count -= 1

#     if count <= 1:
#         # print("I am going to notify")
#         # print(count)
#         notification.notify(
#     title='Internet is On',
#     message='Finally',
#     app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
#     timeout=10,  # seconds
# )


import time
import requests
from playsound import playsound as ps

count= 0
def checkInternet():
    try:
        response = requests.get('https://www.youtube.com/watch?v=WPni755-Krg&t=2724s&ab_channel=YellowBrickCinema-RelaxingMusic')
        print("Internet is  online")
        ps("C:/Users/X/Desktop/D/X/desktop notifier/sound.wav")
        print(count)
    except:
        print("Internet is offline")
        print(count)

while True:
    checkInternet()
    count+=1
    time.sleep(0.2)
    


