from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .table_services import sen_reminder_day_before



scheduler = BackgroundScheduler()
scheduler.add_job(sen_reminder_day_before,trigger=CronTrigger(hour=23, minute=35, second=0, timezone="Asia/Kolkata"))
