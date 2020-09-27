from logic.shortest_path_logic import calculate_shortest_path
from utils.openroutes_utils import get_long_lat_for_city
from utils.openroutes_utils import calculate_travel_distance
from consts.cities import VISIT_CITIES
from consts.cities import VISIT_CITIES_LONG_LAT
from configs.APIkey import API_KEY
from models.travel_graph import Graph
import time
from pprint import pprint

if __name__ == "__main__":
    g = Graph()
    for city_x in VISIT_CITIES:
        for city_y in VISIT_CITIES:
            if city_x != city_y:
                city_x_long_lat = VISIT_CITIES_LONG_LAT[city_x]
                city_y_long_lat = VISIT_CITIES_LONG_LAT[city_y]
                spatial_distance, temporal_distance = calculate_travel_distance(city_x_long_lat, city_y_long_lat, API_KEY)
                g.add_edge(city_x, city_y, 10)
                print("(\"{}\", \"{}\", {}, {})".format(city_x, city_y, spatial_distance, temporal_distance))
                time.sleep(3)
    pprint(g.graph)
