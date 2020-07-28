from server import serverApp
from database import database

app = serverApp()
db = database(app)
db.create_all()

if __name__ == "__main__":
    import api
    import client
    api.apiRoutes(app)
    client.clientRoutes(app)
    app.run(debug=True)
