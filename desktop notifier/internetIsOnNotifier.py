import time
import requests
from playsound import playsound as ps

count = 0


coount = 0
def checkInternet():
    global coount
    try:
        response = requests.get(
            'https://www.youtube.com/watch?v=WPni755-Krg&t=2724s&ab_channel=YellowBrickCinema-RelaxingMusic')
        print(str(coount)+". Internet is  online")
        ps("C:/Users/X/Desktop/D/X/desktop notifier/sound.wav")
        coount += 1
    except:
        coount = (coount)
        print(str(coount)+". Internet is offline")
        coount += 1


while True:
    checkInternet()
    count += 1
    time.sleep(2)
