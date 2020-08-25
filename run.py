from server import serverApp
from database import database

app = serverApp()
db = database(app)
db.create_all()

if __name__ == "__main__":
    import api
    api.apiRoutes(app)
    app.run(debug=True)
