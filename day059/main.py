import requests
from flask import Flask, render_template, request

from post import Post

posts_url = 'https://api.npoint.io/c790b4d5cab58020d391'

def get_posts():
    response = requests.get(posts_url)
    response.raise_for_status()
    posts = []
    for post_dict in response.json():
        posts.append(Post(**post_dict))
    return posts

posts = get_posts()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', data=request.form)
    else:
        return render_template('contact.html')

# @app.post('/submit')
# def submit():
#     return '<h1>Submitted</h1>'


@app.route('/post/<int:id>')
def post(id):
    for post in posts:
        if post.id == id:
            return render_template('post.html', post=post)
    return render_template('404.html') 


if __name__ == '__main__':
    app.run(debug=True)