from time import time

def getDay():
    times = []
    for i in range(24):
        for x in range(4):
            hour = i
            if hour < 10:
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