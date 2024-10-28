import re

def check_password_strength(password):
    if len(password) < 8:
        return "Password too short. Must be at least 8 characters."

    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."

    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        return "Password must contain at least one special character."

    return "Password is strong."


def check_password_breach(password):
    breached_passwords = ['123456', 'password', 'qwerty'] 

    if password in breached_passwords:
        return "Password has been breached! Choose a different password."
    return "Password has not been breached."


def check_password(password):
    strength_message = check_password_strength(password)
    if "strong" not in strength_message:
        return strength_message

    breach_message = check_password_breach(password)
    return breach_message
