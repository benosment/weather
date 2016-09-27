#!/usr/bin/env python3

from geopy.geocoders import Nominatim
from datetime import datetime
import os
import requests

if __name__ == '__main__':
    geolocator = Nominatim()
    location = geolocator.geocode('Cary, NC')
    print('%s (%s, %s)' % (location.address,
                           location.latitude,
                           location.longitude))
    api_key = os.getenv('DARK_SKY_API', '')
    url = 'https://api.darksky.net/forecast/%s/%s,%s' % (api_key,
                                                         location.latitude,
                                                         location.longitude)
    response = requests.get(url).json()
    print('Right now:\n  %s\n  %d\N{DEGREE SIGN} with %d%% of rain' %
          (response['currently']['summary'],
           response['currently']['temperature'],
           response['currently']['precipProbability']))
    print('')
    print('Today:')
    print('  %s' % response['daily']['data'][0]['summary'])
    min_time = datetime.fromtimestamp(response['daily']['data'][0]['apparentTemperatureMinTime'])
    max_time = datetime.fromtimestamp(response['daily']['data'][0]['apparentTemperatureMaxTime'])
    print('  Low of %d\N{DEGREE SIGN} at %s' %
          (response['daily']['data'][0]['apparentTemperatureMin'],
           min_time.strftime('%H:%M:%S')))
    print('  High of %d\N{DEGREE SIGN} at %s' %
          (response['daily']['data'][0]['apparentTemperatureMax'],
           max_time.strftime('%H:%M:%S')))
    print('')
    print('Next 7 days:')
    print('  %s' % response['daily']['summary'])
