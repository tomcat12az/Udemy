# In this Bonus we're going to use Dictionary to add "keys" to the list
# This will improve the bonus 9 example that we worked on before

password = input("Enter new password:  ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False


# This will check to see if there's a number in the password.
# It will check on item as a time that's in the list aka the "password
# If at anytime the "isdigit" incurs a number it will complete the last line and change the value of "digit" to True
# At the end it will append the current list with the digit value

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit



# This will check to see if there's a Uppercase in the password.
# It will check on item as a time that's in the list aka the "password
# If at anytime the "isdigit" incurs a number it will complete the last line and change the value of "upper" to True

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

# We'll use the "all" function to proof the results.  All results of the list must be True for the results to come back as True
# print(result)

print(result)
print(result.values())

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
