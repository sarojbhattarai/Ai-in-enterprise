# The function is expected to return a string.
# The function accepts string as parameter.

#HUffmann encoding (returns the number of consecutive letters in a string )

def logic(my_input):

    compressed = []
    count = 1
    char = my_input[0]
    for i in range(1, len(my_input)):
        if my_input[i] == char:
            count = count + 1
        else:
            compressed.append([char, count])
            char = my_input[i]
            count = 1
    compressed.append([char, count])
    return compressed


# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))
