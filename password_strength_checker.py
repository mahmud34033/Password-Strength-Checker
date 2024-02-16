# Import 'Regular Expression' or 'RegEx' Module
import re 

# Input
password = input("Type your password: ")

# Check each character of password
length = len(password)
check_uppercase = re.search(r'[A-Z]', password)
check_lowercase = re.search(r'[a-z]', password)
check_digit = re.search(r'[0-9]', password)
check_special_char = re.search(r'\W', password)

# Check the strength
is_strong_password = check_uppercase and check_lowercase and check_digit and check_special_char and length >= 8
is_moderate_password = ((check_uppercase and check_lowercase and check_digit)
                        or (check_uppercase and check_lowercase and check_special_char)
                        or (check_uppercase and check_digit and check_special_char)
                        or (check_lowercase and check_digit and check_special_char)) and length >= 6
is_weak_password = ((check_uppercase and check_lowercase)
                        or (check_uppercase and check_digit)
                        or (check_uppercase and check_special_char)
                        or (check_lowercase and check_digit)
                        or (check_lowercase and check_special_char)
                        or (check_digit and check_special_char))

# Output
if is_strong_password :
    print("Password is strong")
elif is_moderate_password :
    print("Password is moderate")
elif is_weak_password :
    print("Password is weak")
else:
    print("Password is very weak")


