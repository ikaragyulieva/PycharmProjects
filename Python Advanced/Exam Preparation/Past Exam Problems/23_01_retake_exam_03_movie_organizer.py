# Mary has a large collection of films, from old black-and-white classics to the newest blockbusters.
# But her collection is an unorganized jumble. She spends hours searching for a particular movie,
# only to find it in the most unexpected place. Mary needs your help to organize her movies.
# Write a function called "movie_organizer" that groups movies by genre.
# The function will receive a different number of arguments, passed as tuples containing two elements:
# the first one is the movie's name, and the second is the genre for example ("Movie Name", "Genre").
# The function should sort the movies by their genre.
# Arrange Mary's collection by the number of movies in each genre in descending order.
# If two or more genres have the same number of movies, return them in ascending order (alphabetically) by genre.
# Each genre group should be sorted in ascending order (alphabetically) by the movie's name.
# To help Mary keep track of her movies, add next to each genre the number of movies in the group.
# In the end, return the output as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input from the console, just parameters passed to your function
# Output
# •	The output should look like this:
# "{genre_1} - {number_of_movies_in_the_genre_group}
# * {movie_name_1}
# * {movie_name_2}
# * {movie_name_3}
# …
# * {movie_name_n}
# {genre_2} - {number_of_movies_in_the_genre_group}
# * {movie_name_1}
# * {movie_name_2}
# …
# * {movie_name_n}
# {genre_n} - {number_of_movies_in_the_genre_group}
# * {movie_name_1}
# …
# * {movie_name_n}"
# Constraints
# •	Each tuple given will always contain a movie with its genre.
# •	You will never receive the same movie twice or more times.


def movie_organizer(*args):
    movies_gender = {}
    for movie, gender in args:
        if gender not in movies_gender:
            movies_gender[gender] = []
        movies_gender[gender].append(movie)

    sorted_collection = sorted(movies_gender.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''
    for gender in sorted_collection:
        result += f"{gender[0]} - {len(gender[1])}\n* "
        result += f'\n* '.join(sorted(gender[1]))
        result += '\n'

    return result


# --- Tests: ---
# Test1:
print(movie_organizer(
    ("The Matrix", "Sci-fi")))

# Test2:
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

# Test3:
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))


# --- Outputs: ---
# Test1:
# Sci-fi - 1
# * The Matrix
#
# Test2:
# Drama - 3
# * The Godfather
# * The Pursuit of Happiness
# * The Shawshank Redemption
# Comedy - 2
# * The Hangover
# * The Hangover Part II
#
# Test3:
# Action - 4
# * Avatar: The Way of Water
# * The Dark Knight
# * The Warrior
# * Top Gun
# Comedy - 4
# * 21 Jump Street
# * Duck Soup
# * Like A Boss
# * Ted
# Drama - 2
# * House Of Gucci
# * The Green Mile
# Musicals - 1
# * A Star Is Born
