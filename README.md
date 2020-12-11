# Vancouver-Amenities-Cleaner
The goal of the project is to visualize Vancouver restaurants and pubs and provide ways to update the data with a web app.

# Please follow steps 1-7 in order to acquire the neccessary data.
"amenities-vancouver.json.gz", "CanadaFoodChains.csv", "json_to_geojson.py", and "amenities.zip" should be in your directory. "amenities.zip" contains all required csv files.

1. "travel-amenities.ipynb" or "food-amenities.py" will output "transportation-amenities-vancouver.json".
2. "food-amenities.ipynb" will output "food-amenities-vancouver.json", and "non-food-amenities-vancouver.json".
3. "vancouver-hotels.ipynb" will output "vancouver-hotels.json".
4. "establishment_matcher.ipynb" or "establishment_matcher.py" will "output alcohol-licensed-vancouver.json", "no-alcohol-licensed-vancouver.json", and "licenseless-bar-pub-vancouver.json".
5. "chain-restaurants-vancouver.ipynb" use "food-amenities-vancouver.json" and multiple csv files of US food chain categories. The output is "chain-resturants-vancouver.json" along with a list of json files based on US fast food chain categories.
6. "cluster-nearest-hotels.ipynb" use 'chain-resturants-vancouver.json', 'transportation-amenities-vancouver.json', 'alcohol-licensed-vancouver.json', and 'vancouver-hotels.json'. The output is "closest-hotel-food-chains.json", "closest-hotel-transport.json", and "closest-hotel-alcohol.json".
7. The output json files from 1-6 were then converted to geojson format using "json_to_geojson.py".

8. The resulting geojson format files are imported into Mapbox api. The result is "vancouver-map.html".
