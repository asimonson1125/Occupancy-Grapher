import schedule 
from reqs import getFacilityOccupancy, getStartEndHour
from threading import Thread
import time
from datetime import datetime, timedelta
from pytz import timezone

def getOffset():
    tz = timezone('US/Eastern')
    return datetime.now().hour - datetime.now(tz).hour

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

def getSchedule():
    start, end = getStartEndHour()
    now = datetime.now()
    offset = getOffset()
    for i in range(end - start):
        if now.hour <= i+start:
            for x in range(12):
                if now.hour != i+start or now.minute < x*5:
                    t = format24Time(i+start-offset, x*5)
                    schedule.every().day.at(t).do(getFacilityOccupancy)
    schedule.every().day.at(str(end-offset) + ":00").do(getFacilityOccupancy)
    

def startScheduler():
    schedule.every().day.at("04:30").do(getSchedule)
    Thread(target=runSchedule).start()

def runSchedule():
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(10)

if __name__ == '__main__':
    getSchedule()
    startScheduler()