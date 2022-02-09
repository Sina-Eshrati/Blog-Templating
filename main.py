from flask import Flask, render_template
import requests


app = Flask(__name__)

response_api = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blogs_data = response_api.json()


@app.route('/')
def home_page():
    return render_template("index.html", blogs_data=blogs_data)


@app.route('/post/<int:num>')
def show_posts(num):
    return render_template("post.html", blogs_data=blogs_data, num=num)


if __name__ == "__main__":
    app.run(debug=True)
