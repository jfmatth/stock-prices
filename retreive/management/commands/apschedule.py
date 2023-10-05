# runapscheduler.py
import logging
from datetime import date

from django.conf import settings
from django.core.management.base import BaseCommand

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util


from yahooquery import Ticker

logger = logging.getLogger(__name__)

def retreive():
    from retreive.models import Retreive, Price

    for s in Retreive.objects.all():
        ticker = Ticker(s.symbol).price

        obj, created = Price.objects.get_or_create(
            symbol = s.symbol,
            datetime = ticker[s.symbol]['regularMarketTime']
        )
        if created:
            obj.price = ticker[s.symbol]['regularMarketPrice']            
            obj.save()
            logger.info(f"{s.symbol} - Captured price")
        else:
            logger.info(f"{s.symbol} - Skipped creating duplicate price")


class Command(BaseCommand):
  help = "Runs APScheduler."

  def handle(self, *args, **options):
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
      retreive,
      trigger=CronTrigger.from_crontab("* 13-21 * * 1-5"),
      id="retreive",
      replace_existing=True,
    )

    try:
      logger.info("Starting scheduler...")
      scheduler.start()
    except KeyboardInterrupt:
      logger.info("Stopping scheduler...")
      scheduler.shutdown()
      logger.info("Scheduler shut down successfully!")
