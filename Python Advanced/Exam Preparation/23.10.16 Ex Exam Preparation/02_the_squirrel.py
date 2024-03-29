# Here are the rules of the game:
# The game starts with 0 collected hazelnuts. Your goal is to collect 3 of them.
# You get as input the size of the field, which will be always a square shape. After that, you will receive the directions in which the squirrel can move – "left", "right", "down", and "up" in a sequence, each value separated by a comma and a space (", "). On the next rows, you will receive the field.
# Possible characters in the field:
# •	s - represents the squirrel's position.
# •	h – represents a hazelnut.
# •	* – the asterisk represents an empty position.
# •	t – represents a trap.
# The squirrel starts from the s - s-position.
# •	If the squirrel steps on a hazelnut, you have to increase them by 1.
# The position should be marked with an asterisk (*).
# o	If the squirrel collects all 3 hazelnuts, the game ends.
# •	Asterisk (*) does nothing, so nothing happens if the squirrel steps on it.
# •	If it steps on a trap, the game ends.
# •	If the squirrel moves out of the field, the game ends.
# After all commands you will have 4 possible results:
# •	You win if the squirrel collects 3 of the hazelnuts.
# •	The squirrel collects less than 3 hazelnuts.
# •	The squirrel steps on a trap.
# •	The squirrel moves out of the field.
# Input
# •	On the first line, you will receive the length of the field – an integer number in the range [3, 5].
# •	On the second line, you will receive the commands to move the squirrel – an array of strings separated by ", ".
# •	In the next N lines, you will receive the values for every row.
# Output
# •	On the first line:
# o	If the squirrel goes out of the field - "The squirrel is out of the field.".
# o	If the squirrel steps on a trap - "Unfortunately, the squirrel stepped on a trap...".
# o	If the squirrel hasn’t collected all the hazelnuts - "There are more hazelnuts to collect.".
# o	If the squirrel has collected all hazelnuts - "Good job! You have collected all hazelnuts!".
# •	On the second line, print the number of collected hazelnuts - "Hazelnuts collected: {hazelnutsCount}"
# Constraints
# •	The size of the field will be between [3,5].
# •	There could be one or no trap on the field.
# •	There will always be 3 hazelnuts on the field.


