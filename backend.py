import requests

api_key = "c6f5d44e3f813f943f9e12c5edd24ed0"

def get_data(place,days = None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days #8 because, this API returns data for every 3 hour, which means for each day we have 8 readings.
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == '__main__':
    print(get_data(place= 'Mumbai',days=3))
