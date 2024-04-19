# Create a generator function called reverse_text that receives a string and yields all string characters on one
# line in reversed order.
# Note: Submit only the function in the judge system

def reverse_text(frase):
    # reversed_frase = list(reversed(frase))
    # index = 0
    # while index < len(frase):
    #     yield reversed_frase[index]
    #     index += 1

    # second solution
    current = len(frase) - 1
    end = 0
    while current >= end:
        yield frase[current]
        current -= 1


for char in reverse_text("step"):
    print(char, end='')
