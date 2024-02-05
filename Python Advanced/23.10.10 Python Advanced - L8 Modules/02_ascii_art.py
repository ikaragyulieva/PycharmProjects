# Write a program that encrypts given words by using the characters: "-|_/\()" to structure the word.
# Use the pyfiglet module. You can read more about it here
# Directions
# 1.	First you need to install the module that we will be using. To install it go to
# Setting --> Project <your_project_name> --> Project Interpreter --> + --> search for pyfiglet --> install package.
# 2.	Import the module
# 3.	Implement the logic. We will be using the figlet_format method
# Hints
# 1.	First, we need to import the module:
# 2.	Then we implement the logic:
# 3.	Lastly, we print the message.

from pyfiglet import figlet_format

word = input()
text = figlet_format(word)
print(text)


