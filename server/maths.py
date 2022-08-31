from time import time
import schedule
from reqs import getFacilityOccupancy
from threading import Thread
import time

def getDay():
    times = []
    for i in range(24):
        for x in range(4):
            hour = i % 12
            if i == 0 or i == 12:
                hour = "12"
            elif hour < 10:
                hour = "0" + str(i)
            else:
                hour = str(hour)
            
            minute = str(x % 4 * 15)
            if x == 0:
                minute = "00"
            
            times.append(f"{hour}:{minute}")
    return times

def getCombo(lower, upper):
    combo = []
    for i in range(len(lower)):
        combo.append((lower[i] + upper[i])/2)
    return combo

def formatTime(hour, minute):
    fHour = hour % 12
    if fHour == 0 or fHour == 12:
        fHour = "12"
    elif fHour < 10:
        fHour = "0" + str(hour)
    else:
        fHour = str(fHour)

    fMinute = str(minute)
    if minute < 10:
        fMinute = "0" + str(minute)
    
    return(f"{fHour}:{fMinute}")

def format24Time(hour, minute):
    fHour = hour
    if fHour < 10:
        fHour = "0" + str(hour)
    else:
        fHour = str(fHour)

    fMinute = str(minute)
    if minute < 10:
        fMinute = "0" + str(minute)
    
    return(f"{fHour}:{fMinute}")

def startScheduler():
    for i in range(24):
        for x in range(12):
            t = format24Time(i, x*5)
            schedule.every().day.at(t).do(getFacilityOccupancy)
    Thread(target=runSchedule).start()

def runSchedule():
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(10)