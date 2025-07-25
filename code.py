import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"🌤 Weather in {data['name']}, {data['sys']['country']}")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"☁ Condition: {data['weather'][0]['description']}")
    elif response.status_code == 401:
        print("❌ Invalid API key. Please check it.")
    elif response.status_code == 404:
        print("❌ City not found. Try a different city.")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

# 🔑 Make sure this is your real API key
api_key = "your_actual_api_key_here"
city = input("Enter city name: ")
get_weather(city, api_key)