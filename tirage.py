from flask import Flask

app = Flask(__name__)

@app.route("/") #default route
def home():
    return "Tirage <h1>Hello<h1>"

if __name__ == "__main__":
    app.run()