from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return render_template('home.html', heading='My personal home page')


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
