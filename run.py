from server import serverApp

app = serverApp()

if __name__ == "__main__":
    import api
    api.apiRoutes(app)
    app.run(debug=True)
