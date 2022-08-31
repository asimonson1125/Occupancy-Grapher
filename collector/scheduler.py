import schedule 
from reqs import getFacilityOccupancy, getStartEndHour
from threading import Thread
import time

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
    for i in range(end - start):
        for x in range(12):
            t = format24Time(i+start, x*5)
            schedule.every().day.at(t).do(getFacilityOccupancy)
    schedule.every().day.at(str(end) + ":00").do(getFacilityOccupancy)
    

def startScheduler():
    schedule.every().day.at("03:00").do(getSchedule)
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