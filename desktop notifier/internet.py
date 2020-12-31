import time
import requests
from playsound import playsound as ps

onCount = 0


offcount = 0
def checkInternet():
    try:
        response = requests.get(
            'https://www.youtube.com/watch?v=WPni755-Krg&t=2724s&ab_channel=YellowBrickCinema-RelaxingMusic')
        ps("C:/Users/X/Desktop/D/X/desktop notifier/sound.wav")
        return True
    except:
      return False



while True:
    checkInternet()
    if checkInternet() ==True:
      print(str(onCount)+". Internet is  online")
      onCount += 1
      offcount = 0

    else:
      print(str(offcount)+". Internet is offline")
      offcount += 1
      onCount = 0
    time.sleep(2)
