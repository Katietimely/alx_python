def validate_password(password):
    if len(password) < 8:
        return False

has_uppercase = False
has_lowercase = False
has_digits = False

for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigits():
        has_digits = True


        
if not (has_uppercase and has_lowercase and has_digits):
    return False
if ' ' in password:
     return False

else:
    return True