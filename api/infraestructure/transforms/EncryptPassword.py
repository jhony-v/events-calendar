import bcrypt

class EncryptPassword():

    @staticmethod
    def setBytesValue(value : str):
        return bytes(value, encoding='utf8')

    @staticmethod
    def encrypt(password : str):
        return bcrypt.hashpw(EncryptPassword.setBytesValue(password), bcrypt.gensalt())

    @staticmethod
    def validate(password : str,hashedPassword : str):
        return bcrypt.checkpw(EncryptPassword.setBytesValue(password),hashedPassword)
