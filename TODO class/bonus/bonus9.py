# This application will ask for a password and check to see if it meets certain conditions.

password = input("Enter new password:  ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)


# This will check to see if there's a number in the password.
# It will check on item as a time that's in the list aka the "password
# If at anytime the "isdigit" incurs a number it will complete the last line and change the value of "digit" to True
# At the end it will append the current list with the digit value

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

# This will check to see if there's a Uppercase in the password.
# It will check on item as a time that's in the list aka the "password
# If at anytime the "isdigit" incurs a number it will complete the last line and change the value of "upper" to True

upper = False
for i in password:
    if i.isupper():
        upper = True

result.append(upper)

# We'll use the "all" function to proof the results.  All results of the list must be True for the results to come back as True
# print(result)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")
