# Uniting nations through teamwork and excellence.
# Embracing diversity, forging victory.
# Write a function called team_lineup that receives information about certain football players and their countries and
# returns a sorted result. The function will receive a tuple of key-value pairs as arguments.
# The arguments will be passed as follows:
# •	The following arguments will be the tuples with two elements - the first one is the player’s name (string),
# and the second one is the county’s name (string).
# First, you need to sort the given information as stated below:
# •	Sort the data by the number of players per country (descending);
# •	If the number of players is equal in two or more countries,
# sort the data by country name length in descending order.
# In the end, return the output as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input from the console, just parameters passed to your function.
# Output
# •	The output should look like this:
#    "{country_name}:"
#    "  -{player1}"
#    "  -{player2}"
#    "  -{playerN}"
# * Please note that there are exactly two intervals before the player’s name.
# Constraints
# •	Each tuple given will always contain the player’s name with its national country.
# •	You will NOT receive the same player in two or more different countries.


def team_lineup(*args):
    countries = {}
    for name, country in args:
        if country not in countries:
            countries[country] = []
        countries[country].append(name)

    sorted_countries = sorted(countries.items(), key=lambda kvp: (-len(kvp[1]), kvp[0], -len(kvp[0])))

    result = ''

    for country, name in sorted_countries:
        result += f"{country}:\n  -"
        result += f'\n  -'.join(name)
        result += '\n'
    return result


# --- Tests: ---
# Test1:
print(team_lineup(
   ("Harry Kane", "England"), 
   ("Manuel Neuer", "Germany"), 
   ("Raheem Sterling", "England"), 
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

# Test2:
print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

# Test3:
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

# --- Outputs: ---

# Test1:
# Germany:
#   -Manuel Neuer
#   -Toni Kroos
#   -Thomas Muller
# England:
#   -Harry Kane
#   -Raheem Sterling
# Portugal:
#   -Cristiano Ronaldo

# Test2:
# England:
#   -Harry Kane
#   -Raheem Sterling
# Argentina:
#   -Lionel Messi
# Brazil:
#   -Neymar
# France:
#   -Kylian Mbappe
# Portugal:
#   -Cristiano Ronaldo
#
# # Test3:
# England:
#   -Harry Kane
#   -Raheem Sterling
#   -Harry Maguire
# Germany:
#   -Manuel Neuer
#   -Toni Kroos
#   -Thomas Muller
# Portugal:
#   -Cristiano Ronaldo
#   -Bruno Fernandes
#   -Bernardo Silva
