from cryptography.fernet import Fernet

KEY = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='


def encrypted_password(password):
    '''Takes an unencrypted password and encrypts it'''
    cipher_suite = Fernet(KEY)
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    return encrypted_password


def decrypt_password(encrypted_password):
    '''Takes an encrypted password and unencrypts it'''
    cipher_suite = Fernet(KEY)
    decrypted_password = cipher_suite.decrypt(encrypted_password)
    return decrypted_password.decode("utf-8")
