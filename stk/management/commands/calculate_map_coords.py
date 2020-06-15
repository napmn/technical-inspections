import logging
import pandas as pd

from django.conf import settings
from django.core.management.base import BaseCommand

from stk.models import Station

logger = logging.getLogger(__name__)


class Command(BaseCommand):


    def handle(self, *args, **options):
        lat_range = settings.CZ_MAX_LATITUDE - settings.CZ_MIN_LATITUDE
        lat_coeff = settings.MAP_HEIGHT / lat_range
        long_range = settings.CZ_MAX_LONGITUDE - settings.CZ_MIN_LONGITUDE
        long_coeff = settings.MAP_WIDTH / long_range

        logger.debug(f'lat coeff {lat_coeff}, long coeff {long_coeff}')

        for station in Station.objects.exclude(longitude=None, latitude=None):
            station.map_x = (float(station.google_longitude) - settings.CZ_MIN_LONGITUDE) * long_coeff
            station.map_y = settings.MAP_HEIGHT - ((float(station.google_latitude) - settings.CZ_MIN_LATITUDE) * lat_coeff) \
                + settings.MAP_TOP_PADDING
            station.save()
