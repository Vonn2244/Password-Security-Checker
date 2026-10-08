print("Password Security Checker")
# Get the password from the user
password = input("Enter a password to check: ")
print("Checking password security...")
# Check the password against basic security requirements
length_check = len(password) >= 8
uppercase_check = any(char.isupper() for char in password)
lowercase_check = any(char.islower() for char in password)
number_check = any(char.isdigit() for char in password)
special_check = any(not char.isalnum() for char in password)
print("\nSecurity Checks:")
print("At least 8 characters:", length_check)
print("Contains uppercase letter:", uppercase_check)
print("Contains lowercase letter:", lowercase_check)
print("Contains a number:", number_check)
print("Contains a special character:", special_check)
# Calculate the password security score
score = sum([
    length_check,
    uppercase_check,
    lowercase_check,
    number_check,
    special_check
])
print("\nPassword Score:", score, "/ 5")
if score <= 2:
    rating = "Weak"
elif score == 3:
    rating = "Moderate"
elif score == 4:
    rating = "Strong"
else:
    rating = "Very Strong"
print("Security Rating:", rating)