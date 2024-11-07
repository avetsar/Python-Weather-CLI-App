A simple command-line interface (CLI) application that fetches and displays real-time weather information for any city using the OpenWeatherMap API.

## 📋 Table of Contents
- About
- Features
- Installation
- Usage
- Demo
- Technologies Used
- License

## 🌟 About
The Weather CLI App allows users to check the current weather for any city worldwide. This app fetches temperature, humidity, pressure, and a brief description of weather conditions from the OpenWeatherMap API and displays it directly in the terminal.

## 🚀 Features
- Get real-time weather information.
- View temperature, humidity, pressure, wind speed, and weather description.
- Simple and easy-to-use command-line interface.

## 📦 Installation

Clone the Repository:
   ```bash
   git clone https://github.com/your-username/weather-cli-app.git
   cd weather-cli-app
   Install Dependencies:Make sure you have Python 3 installed, then install the required library:

bashCopy code

pip install requests
```
Get an API Key from OpenWeatherMap:

Sign up on OpenWeatherMap.
Go to API keys and generate a new API key.

Add Your API Key to the Code:
Open the weather_cli.py file.
Replace your_api_key_here with your OpenWeatherMap API key.

## 🖥️ Usage
Run the app from your terminal:
bash
Copy code

python weather_cli.py
```
Enter the name of a city to get its weather information, or type exit to quit.
Example
plaintextCopy code

Welcome to the Weather CLI App!
Enter the name of a city to get its weather (or type 'exit' to quit): London

Weather in London:
Temperature: 15°C
Humidity: 82%
Pressure: 1012 hPa
Wind Speed: 5 m/s
Description: Light rain
```
