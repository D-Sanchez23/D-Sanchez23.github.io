import re
import hashlib
import requests

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
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        
        hashes = response.text.splitlines()
        for hash_suffix in hashes:
            hash_suffix, count = hash_suffix.split(':')
            if hash_suffix == suffix:
                return f"Password has been breached {count} times! Choose a different password."
        return "Password has not been breached."

    except requests.exceptions.Timeout:
        return "Error: The request to the breach database timed out. Please try again later."
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the breach database. Check your internet connection."
    except requests.exceptions.HTTPError as http_err:
        return f"Error: Unable to check password breach status. Server responded with {http_err}."
    except Exception as err:
        return f"An unexpected error occurred: {err}"


def check_password(password):
    strength_message = check_password_strength(password)
    if "strong" not in strength_message:
        return strength_message

    breach_message = check_password_breach(password)
    return breach_message

if __name__ == "__main__":
    # Prompt the user for a password
    password = input("Enter a password to check: ")
    # Run the checks and print the results
    print(check_password(password))
