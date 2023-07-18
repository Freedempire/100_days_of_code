from datetime import datetime

from flask import Flask, render_template
from markupsafe import escape
import requests

from post import Post

genderize_endpoint = 'https://api.genderize.io'
agify_endpoint = 'https://api.agify.io'
blog_fake_endpoint = 'https://api.npoint.io/c790b4d5cab58020d391'

def guess_gender(name):
    params = {
        'name': name
    }
    response = requests.get(genderize_endpoint, params)
    response.raise_for_status()
    return response.json()['gender']

def guess_age(name):
    params = {
        'name': name
    }
    response = requests.get(agify_endpoint, params)
    response.raise_for_status()
    return response.json()['age']


app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.now().year
    return render_template('dynamic_copyright_year.html', year=year)

@app.route('/guess/<name>')
def guess(name):
    name = escape(name)
    gender = guess_gender(name)
    age = guess_age(name)
    return render_template('guess_gender_age.html', name=name, gender=gender, age=age)

@app.route('/blog')
@app.route('/blog/<int:id>')
def blog(id=None):
    response = requests.get(blog_fake_endpoint)
    response.raise_for_status()
    posts = []
    for post_dict in response.json():
        posts.append(Post(**post_dict)) # ** for dictionary unpacking
    print(posts)
    if id:
        return render_template('post.html', post=posts[id - 1])
    return render_template('blog.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)