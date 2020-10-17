from api.infraestructure.repositories.UserAuthRepository.SignUpRepository import SignUpRepository
from databases import mysqlConnection

def signUpUser(user):
    signUpUserRepository = SignUpRepository(dataAccess=mysqlConnection)
    return signUpUserRepository.signUp(user=user)