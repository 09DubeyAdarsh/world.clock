import datetime
import pytz

# Dictionary of cities and their corresponding time zones
cities = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Tokyo': 'Asia/Tokyo',
    'Sydney': 'Australia/Sydney',
    'Mumbai': 'Asia/Kolkata',
}

def get_local_time(city):
    tz = pytz.timezone(cities[city])
    local_time = datetime.datetime.now(tz)
    return local_time.strftime("%Y-%m-%d %H:%M:%S")

# Example usage:
print("World Clock Timer")
print("------------------")

# Display the local time for each city
for city in cities:
    local_time = get_local_time(city)
    print(f"{city}: {local_time}")
