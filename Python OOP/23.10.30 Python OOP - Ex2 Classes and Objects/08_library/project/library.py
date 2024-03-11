# Create a class called Library, where the information regarding the users and books rented/available will be stored.
# Create another one called User, where the information for each of the library users will be stored, and Registration
# class, where user information will be administrated (created/edited/deleted) and stored in the Library records.
#
# Class User
# In the user.py file, create the class User. Upon initialization, it should receive user_id (int) and username
# (string). The class should also have an instance attribute books that is an empty list.
# You should also create 2 instance methods:
# -	info() - returns a string containing the books currently rented by the user in ascending order
# separated by comma and space.
# -	__str__() - override the method to get a string in the following format "{user_id}, {username},
# {list of rented books}"
# Class Library
# In the library.py create a class Library.
# Upon initialization, it will not receive anything, but it should have the following instance attributes:
# o	user_records - an empty list that will store the users (users objects) of the library
# o	books_available - an empty dictionary that will keep information regarding the authors (key: str)
# and the books available for each of the authors (list of strings)
# o	rented_books - an empty dictionary that will keep information regarding the usernames (key: str)
# and nested dictionary as a value which will keep information regarding the book names (key: str) and days left before
# returning the book to the library (int) - ({usernames: {book names: days to return}}).
# You should also create 2 additional instance methods:
# -	get_book(author: str, book_name: str, days_to_return: int, user: User):
# o	If the book is available in the library add it to the books list for this user, update the library records
# rented_books and available_books dicts), and return the following message:
# "{book_name} successfully rented for the next {days_to_return} days!"
# o	If it is already rented, return the following message "The book "{book_name}" is already rented and will be
# available in {days_to_return provided by the user rented the book} days!"
# -	return_book(author:str, book_name:str, user: User):
# o	If the book is in the user's books list, returns it to the library
# (update books_available and rented_books class attributes) and remove it from the books list for this user
# o	Otherwise, returns the following message "{username} doesn't have this book in his/her records!"
# Class Registration
# In the registration.py, create a class called Registration. Upon initialization,
# It will not receive anything, but we'll have these three methods.
# -	add_user(user: User, library: Library):
# o	Adds the user if we do not have them in the library's user records already
# o	Otherwise, returns the message "User with id = {user_id} already registered in the library!"
# -	remove_user(user: User, library: Library):
# o	Removes the user from the library records if present
# o	Otherwise, returns the message "We could not find such user to remove!"
# -	change_username(user_id: int, new_username: str, library: Library):
# o	If there is a record with the same user id in the library and the username is different than the provided one,
# change the username with the new one provided and return the message
# "Username successfully changed to: {new_username} for user id: {user_id}".
# Changes his username in the rented_books dictionary as well (if present).
# o	If the new username is the same for this id, return the following message
# "Please check again the provided username - it should be different than the username used so far!".
# o	If there is no record for the provided id return "There is no user with id = {user_id}!"
from typing import List, Dict, Optional
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str, List[str]] = {}  # {author: [book_name]}
        self.rented_books: Dict[str, Dict[str, int]] = {}  # {username: {book_name: days_to_return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        for auth, books in self.books_available.items():
            if auth == author and book_name in books:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for book in self.rented_books.values():
            if book_name in book:
                days = book[book_name]
                return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self, author: str, book_name: str, user: User) -> Optional[str]:
        if book_name in user.books:
            user.books.remove(book_name)
            self.rented_books[user.username].pop(book_name)
            self.books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
