# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 22:08:11 2020

@author: John Zheng
"""
import numpy as np
import pandas as pd
from sys import argv
from os.path import exists
import json 


# code modified from https://gis.stackexchange.com/questions/73756/is-it-possible-to-convert-regular-json-to-geojson
script, in_file, out_file = argv
amenities = pd.read_json(in_file, lines=True)
print(amenities)
print(len(amenities.index))
#print(amenities['lat'].dtypes)
i = 0
geojson = dict()
iterate = {
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [amenities['lon'][i], amenities['lat'][i]],
            },
        "properties" : {
            "amenity": amenities['amenity'][i],
            "name": amenities['name'][i],
            "tags": amenities['tags'][i]
            },
      }for i in range(0,len(amenities.index))],
      "type": "FeatureCollection"
     }

output = open(out_file, 'w')
print(iterate)
json.dump(iterate, output)

