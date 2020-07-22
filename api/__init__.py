from api.routes import user

routers = [
    {
        'router': user.userRoute,
        'path': 'users'
    }
]

