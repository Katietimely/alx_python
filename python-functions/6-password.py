def validate_password(password):
    password = len(password) > 8
    if len(password) < 8:
        return False


has_uppercase = False
has_lowercase = False
has_digit = False
has_space = False

for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit():
        has_digit = True
    elif char.isspace():
        has_space = False
     
     
       

print(validate_password("Password123"))


