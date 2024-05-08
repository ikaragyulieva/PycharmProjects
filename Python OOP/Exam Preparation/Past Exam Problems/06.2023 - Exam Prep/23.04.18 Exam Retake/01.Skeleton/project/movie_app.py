from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        try:
            user = [u for u in self.users_collection if u.username == username][0]
            raise Exception("User already exists!")
        except IndexError:
            self.users_collection.append(User(username, age))
            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = [u for u in self.users_collection if u.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = [u for u in self.users_collection if u.username == username][0]
        if movie not in self.movies_collection:
            raise Exception(F"The movie {movie.title} is not uploaded!")
        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        if user == movie.owner:
            raise Exception(F"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(F"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]
        if movie not in user.movies_liked:
            raise Exception(F"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if self.movies_collection:
            sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
            return "\n".join([movie.details() for movie in sorted_movies])
        return "No movies found."

    def __str__(self):
        result = ""
        if self.users_collection:
            result += f"All users: {', '.join([user.username for user in self.users_collection])}"
            result += "\n"
        else:
            result += f"All users: No users.\n"

        if self.movies_collection:
            result += f"All movies: {', '.join([movie.title for movie in self.movies_collection])}"
        else:
            result += f"All users: No movies."

        return result
