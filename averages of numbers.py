# Ask the user to enter two integer and one float. convert them all to floats and print their average.

a = int (input("Enter first integer number: "))
b = int (input("Enter second integer number: "))
c = float (input("Enter a float number: "))

#covert all to float

a = float(a)
b = float(b)

#calculate average 

avg = (a + b + c) / 3

print("average =", avg)