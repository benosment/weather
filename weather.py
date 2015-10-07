#!/usr/bin/env python3

from geopy.geocoders import Nominatim
import os
import requests

if __name__ == '__main__':
    geolocator = Nominatim()
    location = geolocator.geocode('Cary, NC')
    print('%s (%s, %s)' % (location.address,
                           location.latitude,
                           location.longitude))
    api_key = os.getenv('DARK_SKY_API', '')
    url = 'https://api.forecast.io/forecast/%s/%s,%s' % (api_key,
                                                         location.latitude,
                                                         location.longitude)
    response = requests.get(url).json()
    print('Currently %s. %d degrees with %d chance of rain' %
          (response['currently']['summary'],
           response['currently']['temperature'],
           response['currently']['precipProbability']))
