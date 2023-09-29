from django.core.management.base import BaseCommand

import logging
from datetime import date

from yahooquery import Ticker

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Load prices in the retreive table"

    def handle(self, *args, **options):
        retreive()

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
        else:
            logger.info(f"{s.symbol} - Skipped creating duplicate price")

        # p = Price()
        # p.symbol = s.symbol
        # p.datetime = ticker[s.symbol]['regularMarketTime']
        # p.price = ticker[s.symbol]['regularMarketPrice']

        # p.save()
