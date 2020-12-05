import pandas as pd
import numpy as np
import sys

def main():
    """
    Takes in 3 arguments
    1. Path to the file containing the osm data
    2. File name for the json output for amenities related to food
    3. File name for the json output for amenities not related to food
    """
    script, in_file, food_file, non_food_file = sys.argv
    amenities = pd.read_json(in_file, lines=True)
    places = amenities.dropna()

    food_list = [
        'cafe', 'fast_food', 'bbq', 'restaurant', 'pub', 
        'bar', 'food_court', 'ice_cream', 'marketplace', 
        'stripclub', 'bistro', 'juice_bar']

    food_df = places[places['amenity'].isin(food_list)]

    food_df = food_df.sort_values(by=['name'])
    food_df.to_json(food_file, orient='records', lines=True)

    non_food_df = places[~places['amenity'].isin(food_list)]
    non_food_df = non_food_df.sort_values(by=['amenity'])
    non_food_df.to_json(non_food_file, orient='records', lines=True)

if __name__=='__main__':
    main()