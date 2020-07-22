from server import Server

app = Server().initialize()

if __name__ == "__main__":
    app.run(debug=True)
