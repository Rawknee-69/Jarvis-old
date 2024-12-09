import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, hashed_password

def store_credentials(username, password):
    encrypted_password = hash_password(password)
    with open('credentials.txt', 'w') as file:
        file.write(f"Username: {username}\n")
        file.write(f"Password: {encrypted_password[0].hex()} {encrypted_password[1].hex()}")

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    store_credentials(username, password)
