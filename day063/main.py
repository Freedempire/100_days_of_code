from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

from book_form import BookForm
import library_db

app = Flask(__name__)
app.secret_key = 'demo secret'
bootstrap = Bootstrap5(app)

# books = []


@app.route('/')
def home():
    books = library_db.get_books()
    return render_template('index.html', books=sorted(books, key=lambda x: x['id']), titles=[
        ('id', 'ID'),
        ('title', 'Title'),
        ('author', 'Author'),
        ('rating', 'Rating')
    ])

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # books.append({
        #     'title': form.title.data,
        #     'author': form.author.data,
        #     'rating': int(form.rating.data)
        # })

        # always use None for the NULL value of id
        library_db.add_book((None, form.title.data, form.author.data, int(form.rating.data)))
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route('/change_rating/<int:id>', methods=['GET', 'POST'])
def change_rating(id):
    book_form = BookForm()
    book = library_db.get_book(id)
    if request.method == 'GET':
        book_form.title.data = book['title']
        book_form.title.render_kw = {'disabled':''}
        book_form.author.data = book['author']
        book_form.author.render_kw = {'disabled':''}
        book_form.rating.data = book['rating']
        book_form.submit.render_kw = {'value': 'Update'}
    else:
        # data will become None if field disabled
        book_form.title.data = book['title']
        book_form.author.data = book['author']
        if book_form.validate_on_submit():
            library_db.update_book_rating(id, int(book_form.rating.data))
            return redirect(url_for('home'))
    return render_template('change_rating.html', form=book_form)
    
@app.route('/delete/<int:id>')
def delete(id):
    library_db.delete_book(id)
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)