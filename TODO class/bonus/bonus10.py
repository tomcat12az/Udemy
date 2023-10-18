# This application we're testing error checking.
# We also put in a condition to check to see if they are measuring a square.  If so, the application exits.

try:
    width = float(input("Enter a width:  "))
    length = float(input("Enter a length:  "))

    if width == length:
        exit("Looks like you entered a square.")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")