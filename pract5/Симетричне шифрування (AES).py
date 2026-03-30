from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

text = "Hello world".encode()

encrypted = cipher.encrypt(text)
print(encrypted)

decrypted = cipher.decrypt(encrypted)
print(decrypted.decode())