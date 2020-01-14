from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

texts = ["Hello World",
         "This is a test"]


@app.route('/home')
def home():
    return render_template("home.html", title="Home", texts=texts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)
