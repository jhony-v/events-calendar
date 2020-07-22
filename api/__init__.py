from api.routes import user, event

api = [
    {
        'router': user.userRoute,
        'path': 'users'
    },
    {
        'router': event.eventRoute,
        'path': 'events'
    }
]
