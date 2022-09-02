from time import time
from pytz import timezone
from datetime import datetime

def getDay():
    times = []
    for i in range(24):
        for x in range(12):
            hour = i
            if hour < 10:
                hour = "0" + str(i)
            else:
                hour = str(hour)
            
            minute = str(x * 5)
            if x == 0:
                minute = "00"
            elif x == 1:
                minute = "05"
            
            times.append(f"{hour}:{minute}")
    return times

def getOffset():
    tz = timezone('US/Eastern')
    return datetime.now(tz).hour - datetime.now().hour

def getCombo(lower, upper):
    combo = []
    for i in range(len(lower)):
        combo.append((lower[i] + upper[i])/2)
    return combo

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