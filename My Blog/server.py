from flask import Flask, render_template
from post import Post
p = Post()
app = Flask(__name__)


@app.route('/')
def home():
    data = p.blog()
    return render_template("index.html", posts=data)


@app.route('/post/<int:num>')
def read(num):
    data = p.blog()
    return render_template("post.html", posts=data, id=num)

# Debug mode is currently off.
# if __name__ == "__main__":
#     app.run(debug=True)