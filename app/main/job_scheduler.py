import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


def print_date_time():
    print time.strftime("%A, %d. %B %Y %I:%M:%S %p")

def printName(n):
    print n

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=(lambda: printName('tyler')),
    trigger=IntervalTrigger(seconds=5),
    id='printing_job',
    name='Print date and time every five seconds',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
