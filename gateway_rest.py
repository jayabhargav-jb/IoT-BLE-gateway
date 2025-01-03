import requests
from json import loads

def post_to_thingspeak(temperature:int, humidity:int) -> int:
    url = f"https://api.thingspeak.com/update?api_key=3UYHGO4V3AKY6WBF&field1={temperature}&field2={humidity}"
    request_object = requests.get(url)
    return request_object.status_code

def get_from_thingspeak() -> int:
    url = f"https://api.thingspeak.com/channels/2560176/fields/3.json?api_key=U753623NPSUMMFBS&results=1"
    request_object = requests.get(url)
    data = request_object.content.decode()
    data_dict = loads(data)
    actuation = data_dict["feeds"][0]["field3"]

    return actuation

if __name__ == "__main__":
    print(get_from_thingspeak())