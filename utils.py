# utils.py
import re
# import os

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_password(password):
    return bool(re.search(r'[a-zA-Z]', password) and
                re.search(r'\d', password) and
                re.search(r'[@&]', password))

def validate_registration_data(username, email, name, password, existing_users):
    """Validate all registration data and return list of errors"""
    errors = []
    
    # Check username
    if not username:
        errors.append("Username cannot be empty.")
    elif any(u.username == username for u in existing_users):
        errors.append("Username already taken.")
    
    # Check email
    if not email:
        errors.append("Email cannot be empty.")
    elif any(u.email == email for u in existing_users):
        errors.append("Email already registered.")
    elif not validate_email(email):
        errors.append("Invalid email format.")
    
    # Check name
    if not name:
        errors.append("Name cannot be empty.")
    
    # Check password
    if not password:
        errors.append("Password cannot be empty.")
    elif not validate_password(password):
        errors.append("Password must contain letters, digits, and @ or &.")
    
    return errors

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

def print_sep(title: str | None = None, width: int = 60):
    line = "-" * width
    if title:
        print(f"\n{line}\n{title}\n{line}")
    else:
        print(f"\n{line}")