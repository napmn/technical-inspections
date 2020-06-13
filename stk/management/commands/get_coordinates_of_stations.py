import logging
import time
import requests

from django.core.management.base import BaseCommand
from django.conf import settings

from stk.models import Station

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        for station in Station.objects.all():
            logger.debug(f'Getting coordinates for station {station.city} {station.address}')
            try:
                response = requests.get(
                    'http://api.positionstack.com/v1/forward',
                    params={
                        'access_key': settings.POSITIONSTACK_ACCESS_KEY,
                        'query': f'{station.city} {station.address}',
                        'country': 'CZ',
                        'limit':'10'
                    }
                )
                json_data = response.json()['data']
                if not json_data:
                    continue
                for option in json_data:
                    if station.city in option['label']:
                        station.longitude = option['longitude']
                        station.latitude = option['latitude']
                        station.save()
                        break
            except Exception as e:
                logger.debug(str(e))

            time.sleep(0.1)
