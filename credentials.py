import getpass
import hashlib
import os

def authenticate(username, password, correct_username, correct_password):
    if username == correct_username:
        salt_hex, correct_hashed_password_hex = correct_password
        salt = bytes.fromhex(salt_hex)
        correct_hashed_password = bytes.fromhex(correct_hashed_password_hex)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return hashed_password == correct_hashed_password
    return False

def main():
    with open('credentials.txt', 'r') as file:
        lines = file.readlines()
        correct_username = lines[0].split(": ")[1].strip()
        correct_password = tuple(lines[1].split(": ")[1].split())

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        if authenticate(username, password, correct_username, correct_password):
            print("Authentication successful. Running run.py...")
            os.system("python events.py")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print("Authentication failed. Please try again.")
                if attempts == 2:
                    print("japanese exam")  # Replace with your hint
            else:
                print("Authentication failed. Maximum attempts reached. Exiting.")
                break

