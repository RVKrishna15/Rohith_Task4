import requests

API_KEY = "3989dc7eebd409563fd551643de18f1a"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)   # Remove this line later after testing

if data["cod"] == 200:

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n===== Weather Report =====")
    print("City:", city_name)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", weather.title())
    print("Wind Speed:", wind_speed, "m/s")

else:
    print("Error:", data["message"])