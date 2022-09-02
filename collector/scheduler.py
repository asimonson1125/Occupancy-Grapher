import schedule
from reqs import getFacilityOccupancy, getStartEndHour
from threading import Thread
import time
from datetime import datetime, timedelta
from pytz import timezone

est = timezone('US/Eastern')

def format24Time(hour, minute):
    fHour = hour % 24
    if fHour < 10:
        fHour = "0" + str(hour % 24)
    else:
        fHour = str(fHour)

    fMinute = str(minute)
    if minute < 10:
        fMinute = "0" + str(minute)

    return(f"{fHour}:{fMinute}")


def getSchedule():
    schedule.clear()
    schedule.every().day.at("04:30").do(getSchedule)
    start, end = getStartEndHour()
    now = datetime.now(est)
    if now.hour < 0:
        return
    for i in range(end - start):
        if now.hour <= i+start:
            for x in range(12):
                if not(now.hour == i+start and now.minute >= x*5):
                    t = format24Time((i+start) % 24, x*5)
                    schedule.every().day.at(t).do(getFacilityOccupancy)
    endoff = (end) % 24
    if endoff < 10:
        endoff = "0" + str(endoff)
    endoff = str(endoff)
    schedule.every().day.at(endoff + ":00").do(getFacilityOccupancy)    


def runSchedule():
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(10)


if __name__ == '__main__':
    getSchedule()
    Thread(target=runSchedule).start()
