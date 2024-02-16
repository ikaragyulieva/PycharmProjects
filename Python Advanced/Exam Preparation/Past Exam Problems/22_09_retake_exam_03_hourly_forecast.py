# Patricia wants to go on vacation for the weekend and wants to know where the weather will be the best, so she can see
# the most sights. Patricia is busy at work and doesn't have time to think about the perfect place for her vacation,
# so she wants your help.
# Write a function called forecast that stores information about the weather, and returns sorted information for all
# locations. The function will receive a different number of arguments. The arguments will be passed as tuples with two
# elements - the first one is the location, and the second one is the weather:
# •	Location name: string
# o	any string
# •	Weather: string
# o	"Sunny"
# o	"Rainy"
# o	"Cloudy"
# First, sort all locations by weather. First are positioned the locations with sunny weather, next are the locations
# with cloudy weather, and last are the locations with rainy weather. For each sequence of locations
# (e.g. all sunny locations), sort them by their name in ascending order (alphabetically).
# In the end, return the output as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input from the console, just parameters passed to your function
# Output
# •	The output should look like this:
# "{first_sorted_location} - {weather}"
# "{second_sorted_location} - {weather}"
# …
# "{last_sorted_location} - {weather}"
# Constraints
# •	Each tuple given will always contain the location with its weather.
# •	You will never receive the same location twice or more times.

def forecast(*args):
    # weather_cities = {'Sunny': list(), 'Cloudy': list(), 'Rainy': list()}
    # for city in args:
    #     weather_cities[city[1]] += [city[0]]

    weather_cities = {}
    for el in args:
        if el[0] not in weather_cities:
            weather_cities[el[0]] = el[1]

    sorted_forecast = {k: v for k,v in sorted(weather_cities.items(), key=lambda x: (x[1], x[0]))}
    sunny = ''
    cloudy = ''
    rainy = ''
    for key, value in sorted_forecast.items():
        if value == 'Sunny':
            sunny += f'{key} - {value}\n'
        elif value == 'Cloudy':
            cloudy += f'{key} - {value}\n'
        elif value == 'Rainy':
            rainy += f'{key} - {value}\n'

    return sunny + cloudy + rainy


# --- Tests: ---
# Test1:
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

# Test2:
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

# Test3:
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


# --- Outputs: ---
# Test1:
# New York - Sunny
# Sofia - Sunny
# London - Cloudy
#
# # Test2:
# Beijing - Sunny
# Bourgas - Sunny
# Peru - Sunny
# Tokyo - Sunny
# Florence - Cloudy
# Sofia - Cloudy
# Hong Kong - Rainy
#
# # Test3:
# Sofia - Rainy
# Tokyo - Rainy
