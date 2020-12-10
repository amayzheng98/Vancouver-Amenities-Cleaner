import pandas as pd
import numpy as np
import sys
import difflib

def main():
    """
    Takes in 3 arguments
    1. Path to the file containing the food related osm data
    2. File name for the data containing a column of 'establishment name' to match the osm data to
    3. File name for the output of amenities with alcohol licenses
    4. File name for the output of amenities with no alcohol licenses
    5. File name for the output of amenities labeled bar/pub that do not have alcohol licenses
    """
    script, in_file, esta_name_file, alco_lic_output, non_alco_output, no_lic_bar_output = sys.argv
    amenities = pd.read_json(in_file, lines=True)
    names = pd.read_csv(esta_name_file)
    amenities['closest_name'] = amenities['name'].apply(
        lambda title: difflib.get_close_matches(title, names['establishment name'].values, 1, .85))
    amenities['closest_name'] = amenities['closest_name'].apply(lambda title: ''.join(title)) 
    
    alco = amenities[amenities['closest_name'] != '']
    alco.to_json(alco_lic_output, orient='records', lines=True)

    non_alco = amenities[amenities['closest_name'] == '']
    non_alco = non_alco.sort_values(by=['amenity'])
    non_alco.to_json(non_alco_output, orient='records', lines=True)

    licenseless_bar_pub = non_alco[(non_alco['amenity'] == 'pub') | (non_alco['amenity'] == 'bar')]
    licenseless_bar_pub.to_json(no_lic_bar_output, orient='records', lines=True)

if __name__=='__main__':
    main()