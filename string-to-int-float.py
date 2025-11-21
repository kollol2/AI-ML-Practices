
'''The user enters a string containing a number (e.g., "45"). Convert it to:
an integer
a float
a string again
Print all three values with their types.'''

num_str = input("Enter a number (string format): ")

# convert to integer
num_int = int(num_str)

# convert to float
num_float = float(num_str)

# convert back to string
num_string_again = str(num_int)

print(num_int, type(num_int))
print(num_float, type(num_float))
print(num_string_again, type(num_string_again))
