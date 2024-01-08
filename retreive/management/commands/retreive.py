# runapscheduler.py
import logging
from datetime import date

from django.core.management.base import BaseCommand

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
  help = "Retreive one set of prices"

  def handle(self, *args, **options):
    
    logger.info("Retreiving prices")
    retreive()
