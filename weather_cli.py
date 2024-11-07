import requests

# Replace 'your_api_key_here' with your OpenWeatherMap API key
API_KEY = 'your_api_key_here'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetches and displays weather information for a given city."""
    try:
        # Build the API request URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

        # Send a request to the OpenWeatherMap API
        response = requests.get(url)
        data = response.json()

        # Check if the city is found
        if data["cod"] != 200:
            print(
                f"City '{city}' not found. Please check the spelling or try another city.")
            return

        # Parse and display the weather information
        main = data["main"]
        wind = data["wind"]
        weather_desc = data["weather"][0]["description"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Wind Speed: {wind['speed']} m/s")
        print(f"Description: {weather_desc.capitalize()}")
    except Exception as e:
        print("An error occurred:", e)


def main():
    """Main function to run the CLI app."""
    print("Welcome to the Weather CLI App!")

    while True:
        city = input(
            "\nEnter the name of a city to get its weather (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        get_weather(city)


if name == "__main__":
    main()
