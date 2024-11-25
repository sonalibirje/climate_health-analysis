import requests
import pandas as pd
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Load the API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API Key not found! Make sure it is set in the .env file.")
    exit()

print(f"Using API Key: {API_KEY}")

# List of cities
cities = ["Delhi", "London", "New York"]

# Function to fetch air quality data for a city on a specific date
def fetch_air_quality_data(city, date, api_key):
    # Assuming WAQI supports a 'date' parameter (replace with actual if supported)
    url = f"https://api.waqi.info/feed/{city}/?token={api_key}&date={date}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("status") == "ok":
            print(f"Data fetched successfully for {city} on {date}")
            return data["data"]
        else:
            print(f"No data available for {city} on {date}. Error: {data.get('data', 'Unknown error')}")
            return None
    else:
        print(f"Failed to fetch data for {city} on {date}. Status code: {response.status_code}")
        print("Error response:", response.text)
        return None

# Main function to fetch data for all cities and save it to a CSV file
def main():
    all_data = []

    # Define date range: 15 years from today
    end_date = datetime.now()
    start_date = end_date - timedelta(days=15 * 365)  # Approximate 15 years
    current_date = start_date

    while current_date <= end_date:
        # Format the current date (YYYY-MM-DD)
        date_str = current_date.strftime("%Y-%m-%d")

        for city in cities:
            print(f"Fetching data for {city} on {date_str}...")
            data = fetch_air_quality_data(city, date_str, API_KEY)
            if data:
                city_data = {
                    "city": city,
                    "date": date_str,
                    "aqi": data.get("aqi"),  # Air Quality Index
                    "pm2_5": data.get("iaqi", {}).get("pm25", {}).get("v", None),  # Particulate Matter 2.5
                    "pm10": data.get("iaqi", {}).get("pm10", {}).get("v", None),  # Particulate Matter 10
                    "no2": data.get("iaqi", {}).get("no2", {}).get("v", None),    # Nitrogen Dioxide
                    "co": data.get("iaqi", {}).get("co", {}).get("v", None),      # Carbon Monoxide
                    "dominant_pollutant": data.get("dominentpol")  # Dominant pollutant
                }
                all_data.append(city_data)

        # Move to the next day
        current_date += timedelta(days=1)

    # Save all data to a CSV file
    if all_data:
        os.makedirs("data/raw", exist_ok=True)  # Ensure the output directory exists
        df = pd.DataFrame(all_data)
        df.to_csv("data/raw/air_quality_data_15_years.csv", index=False)
        print("Air quality data saved to data/raw/air_quality_data_15_years.csv")

if __name__ == "__main__":
    main()

