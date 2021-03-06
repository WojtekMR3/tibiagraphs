from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .tbapi import get_hs_as, get_character

def start():
  scheduler = BackgroundScheduler(timezone="Europe/Warsaw")
  #scheduler.add_job(schedule_api, 'cron', second=0)
  #scheduler.add_job(get_hs_as, 'cron', second=5)
  #scheduler.add_job(get_hs_as, 'cron', minute=50)
  scheduler.add_job(get_hs_as, 'cron', second=30)
  scheduler.start()