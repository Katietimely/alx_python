def validate_password(password):
    if char(password) < 8:
        return False

has_uppercase = False
has_lowercase = False
has_digits = False
empty_space = False

for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigits():
        has_digits = True
    elif ' ' in password:
        empty_space = False
    else:
        has_digits =  False

password ="MyPassword"
result= validate_password(password)



print(result)