from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Home Page</h1>"


@app.route("/hello/<city>")
def hello(city):
    return f"<h1>Hello, {city}!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
