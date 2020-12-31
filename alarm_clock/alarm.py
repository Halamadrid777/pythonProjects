import time
import playsound
import datetime
from playsound import playsound as ps


# set timer
print("set your timer")
print("time now is,"+str(time.localtime()))
# time_year=int(input("set your  (year): "))
# time_month =int(input("set your (month): "))
time_day =int(input("set your (day): "))
time_hour = int(input("set your (hour ) in 24 hour format:  "))
time_min =int(input("set your (min): "))

time_year = 2020
time_month = 9

timer_set = datetime.datetime(time_year, time_month,time_day,time_hour, time_min)
print(timer_set)
# check for time
print(datetime.datetime.now())
while True:
    time.sleep(1)
    if timer_set < datetime.datetime.now():
        print("press CTRL + C to exit")
        ps('alarm.mp3')
        ps('Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3')
        ps('Alarm-Fast-High-Pitch-A2-www.fesliyanstudios.com.mp3')
        ps('Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3')
        ps('Alarm-Fast-High-Pitch-A3-www.fesliyanstudios.com.mp3')
        ps('Alarm-Fast-High-Pitch-B1-www.fesliyanstudios.com-www.fesliyanstudios.com.mp3')
        ps('Alarm-Slow-A1-www.fesliyanstudios.com.mp3')
        ps('Alarm-Slow-A2-www.fesliyanstudios.com.mp3')
        ps('Alarm-Slow-A3-www.fesliyanstudios.com.mp3')
        ps('Alarm-Slow-B1-www.fesliyanstudios.com.mp3')

