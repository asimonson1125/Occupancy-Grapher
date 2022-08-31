import schedule 
from reqs import getFacilityOccupancy
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

def startScheduler():
    for i in range(24):
        for x in range(60):
            t = format24Time(i, x)
            schedule.every().day.at(t).do(getFacilityOccupancy)
    Thread(target=runSchedule).start()

def runSchedule():
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(10)

if __name__ == '__main__':
    startScheduler()