from cryptography.fernet import Fernet
import random
import string
import base64

def decrypt_password(encrypted_password, key):
    key = base64.urlsafe_b64encode(key.ljust(32)[:32].encode())
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

def read_passwords_from_file(filename='passwords.txt'):
    with open(filename, 'rb') as file:
        lines = file.readlines()
    return lines

encryption_key = input('enter the key: '); 

# Read the encrypted passwords from the file
encrypted_passwords = read_passwords_from_file('passwords.txt')

# Decrypt and print the passwords
for index, encrypted_password in enumerate(encrypted_passwords):
    decrypted_password = decrypt_password(encrypted_password.strip(), encryption_key)
    print(f"{index}) {decrypted_password}")