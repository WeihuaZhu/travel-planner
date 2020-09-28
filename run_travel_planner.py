from logic.shortest_path_logic import calculate_shortest_path
from utils.openroutes_utils import get_long_lat_for_city
from utils.openroutes_utils import calculate_travel_distance
from consts.cities import CITY_DISTANCE_PAIRS
from configs.APIkey import API_KEY
from models.travel_graph import Graph

if __name__ == "__main__":
    g = Graph()
    for entry in CITY_DISTANCE_PAIRS:
        src_city, dest_city, spatial_dist, temporal_dist = entry
        g.add_edge(src_city, dest_city, temporal_dist)
    print(len(g.vertices))
    lowest_cost, shortest_path = calculate_shortest_path(g)
    print(lowest_cost)
    print(shortest_path)
