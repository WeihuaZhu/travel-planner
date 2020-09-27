import requests

DIRECTION_BASE_URL = "https://api.openrouteservice.org/v2/directions/"
GEOCODE_BASE_URL = "https://api.openrouteservice.org/geocode/"


def get_long_lat_for_city(name, api_key):
    """
    get long lat as a tuple for city
    :param name: <str>, e.g. "Paris, France"
    :param api_key: <str>, API key for openroutes service
    :return: <tuple> of length 2, (long, lat)
    """
    response = requests.get("{}search?api_key={}&text={}".format(GEOCODE_BASE_URL, api_key, name))
    if response.status_code == 200:
        result = response.json()
        features = result.get("features")
        if features:
            return tuple(features[0].get("geometry").get("coordinates"))
        else:
            return None
    else:
        print("response error: {}, {}".format(response.status_code, response.reason))
        return None


def generate_long_lat_for_cities(cities, api_key):
    """
    utility to print out city: (long, lat) format to be used as constants
    :param cities: <collection> of cities
    """
    for city in cities:
        long_lat = get_long_lat_for_city(city, api_key)
        print("\"{}\": {}".format(city, long_lat))


def calculate_travel_distance(src_long_lat, dest_long_lat, api_key):
    """

    :param src_long_lat:
    :param dest_long_lat:
    :return:
    """
    src_long_lat_str = "{},{}".format(src_long_lat[0], src_long_lat[1])
    dest_long_lat_str = "{},{}".format(dest_long_lat[0], dest_long_lat[1])
    response = requests.get(
        "{}driving-car?api_key={}&start={}&end={}".format(DIRECTION_BASE_URL, api_key, src_long_lat_str, dest_long_lat_str))
    if response.status_code == 200:
        result = response.json()
        features = result.get("features")
        if features:
            spatial_distance = (features[0].get("properties").get("segments"))[0].get("distance")
            temporal_distance = (features[0].get("properties").get("segments"))[0].get("duration")
            return (spatial_distance / 1000, temporal_distance / 60)
        else:
            return None, None
    else:
        print("response error: {}, {}".format(response.status_code, response.reason))
        return None, None