import requests
import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, URLField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, URL
import dotenv


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1870)])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = DecimalField('Rating', validators=[DataRequired(), NumberRange(min=0, max=10)])
    # ranking = IntegerField('Ranking', validators=[DataRequired(), NumberRange(min=1, max=10)])
    # ranking will be calculated after inserting to the db, so there's no need to asking users to provide it
    review = TextAreaField('Review', validators=[DataRequired()])
    img_url = URLField('Image URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Add')


class MovieEditForm(FlaskForm):
    rating = DecimalField('Your Rating Out of 10 e.g. 7.5', places=1, validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = TextAreaField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class MovieImportForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Search in TMDB')


def url_join(*args):
    """Join url parts together to form a complete one. '/' on both ends will be
    left unchanged if exist."""
    if len(args) == 0:
        return
    if len(args) == 1:
        return args[0]
    url = ''
    for index, arg in enumerate(args):
        if not arg.startswith('/') and index != 0:
            arg = '/' + arg
        if arg.endswith('/') and index < len(args) - 1:
            arg = arg.rstrip('/')
        url += arg
    return url


def search_movies_by_title(title):
    url = 'https://api.themoviedb.org/3/search/movie'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + TMDB_API_READ_ACCESS_TOKEN
    }
    params = {
        'query': title
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()['results']


def get_movie_details_by_id(tmdb_id):
    url = 'https://api.themoviedb.org/3/movie'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + TMDB_API_READ_ACCESS_TOKEN
    }
    response = requests.get(url_join(url, tmdb_id), headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster_url(movie_details, size='w500'):
    url = 'https://api.themoviedb.org/3/configuration'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + TMDB_API_READ_ACCESS_TOKEN
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return url_join(response.json()['images']['secure_base_url'], size, movie_details['poster_path'])


def recalculate_ranking():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    for index, movie in enumerate(movies):
        movie.ranking = index + 1
    db.session.commit()


dotenv.load_dotenv()
# TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
TMDB_API_READ_ACCESS_TOKEN = os.environ.get('TMDB_API_READ_ACCESS_TOKEN')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b' # secret key for csrf token
bootstrap = Bootstrap5(app)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_movies.db'
# create the sqlachemy extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)

# define model
class Movie(db.Model): # only db has Model, sa does not
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    year = sa.Column(sa.Integer, nullable=False)
    description = sa.Column(sa.String, nullable=False)
    rating = sa.Column(sa.Float, nullable=False)
    ranking = sa.Column(sa.Integer)
    review = sa.Column(sa.String, nullable=False)
    img_url =sa.Column(sa.String, nullable=False)

# create table
with app.app_context():
    # table will not be created if already exists
    db.create_all()

@app.route('/')
def home():
    # query the data, must be within a Flask view or CLI command
    # db.session.add(Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favorite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # ))
    # db.session.commit()
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    return render_template("index.html", movies=movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    """
    Edit an existing movie's rating and review, or adding rating and review of a
    new movie to the db. The rankings will be recalculated after editing.
    """
    movie_edit_form = MovieEditForm()
    id = request.args.get('id')
    if request.method == 'GET':
        if id: # if movie already in db
            movie = db.get_or_404(Movie, id)
            movie_edit_form.rating.data = movie.rating
            movie_edit_form.review.data = movie.review
            title = movie.title
        else:
            title = request.args.get('title')
        return render_template('edit.html', form=movie_edit_form, title=title)

    elif movie_edit_form.validate_on_submit():
        if id:
            movie = db.get_or_404(Movie, id)
            movie.rating = float(f'{movie_edit_form.rating.data:.1f}')
            movie.review = movie_edit_form.review.data
        else:
            tmdb_id = request.args.get('tmdb_id')
            print(f'{tmdb_id=}')
            movie_details = get_movie_details_by_id(tmdb_id)
            movie = Movie()
            movie.title = movie_details['title']
            movie.year = int(movie_details['release_date'].split('-')[0])
            movie.description = movie_details['overview']
            movie.img_url = get_poster_url(movie_details)
            movie.rating = float(f'{movie_edit_form.rating.data:.1f}')
            movie.review = movie_edit_form.review.data
            db.session.add(movie)
        db.session.commit()

        # recalculate ranking
        recalculate_ranking()

        return redirect(url_for('home'))


@app.route('/delete')
def delete():
    """
    Delete the movie from the db. After deleting, the rankings will be recalculated.
    """
    id = request.args.get('id')
    db.session.delete(db.get_or_404(Movie, id))
    db.session.commit()
    # recalculate ranking
    recalculate_ranking()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Add movie by hand, i.e. providing all the info of the movie by user itself.
    After the movie being added to the library db, the rankings of all movies in
    the db will be calculated.
    """
    form = MovieForm()
    if form.validate_on_submit():
        movie = Movie()
        movie.title = form.title.data
        movie.year = int(form.year.data)
        movie.description = form.description.data
        movie.rating = float(f'{form.rating.data:.1f}')
        movie.ranking = int(form.ranking.data)
        movie.review = form.review.data
        movie.img_url = form.img_url.data
        db.session.add(movie)
        db.session.commit()
        # recalculate ranking
        recalculate_ranking()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route('/import_movie', methods=['GET', 'POST'])
def import_movie():
    """
    Import movie from TMDB by searching the movie's title and selecting from the results.
    Then user will be asked to give rating and review for the movie on edit.html.
    """
    movie_import_form = MovieImportForm()
    if movie_import_form.validate_on_submit():
        movies = search_movies_by_title(movie_import_form.title.data)
        return render_template('select.html', movies=movies)
    return render_template('import.html', form=movie_import_form)


if __name__ == '__main__':
    app.run(debug=True)
