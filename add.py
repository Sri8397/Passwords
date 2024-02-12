from cryptography.fernet import Fernet
import random
import string
import base64

def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def encrypt_password(password, key):
    key = base64.urlsafe_b64encode(key.ljust(32)[:32].encode())
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def save_password_to_file(encrypted_password, filename='passwords.txt'):
    with open(filename, 'ab') as file:
        file.write(encrypted_password + b'\n')

encryption_key = input('enter the key: '); 

# Generate a random password
random_password = generate_password()
print(f'new password is: {random_password}'); 

tag = input('enter the tag: '); 
random_password = tag + ' ' + random_password; 

# Encrypt the password
encrypted_password = encrypt_password(random_password, encryption_key)

# Save the encrypted password to a file
save_password_to_file(encrypted_password)

