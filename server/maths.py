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
        fMinute = "0" + minute
    
    return(f"{fHour}:{fMinute}")