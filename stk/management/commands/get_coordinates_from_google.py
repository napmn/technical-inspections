import logging
import time
from pprint import pprint

import googlemaps
from django.core.management.base import BaseCommand
from django.conf import settings

from stk.models import Station

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

        stations = Station.objects.filter(google_longitude=None, google_latitude=None).exclude(region=None)
        total = stations.count()
        count = 0
        for station in stations:
            count += 1
            logger.debug(f'{count}/{total} Fetching coordinates for {station}')

            geocode_result = gmaps.geocode(f'{station.address}, {station.city}, Czech Republic')
            if geocode_result:
                station.google_latitude = geocode_result[0]['geometry']['location']['lat']
                station.google_longitude = geocode_result[0]['geometry']['location']['lng']
                logger.debug(f'\t--- Got response: lat={station.google_latitude}, lng={station.google_longitude}')
                station.save()
            time.sleep(0.2)
