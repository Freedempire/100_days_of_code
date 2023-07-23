import sqlite3


def dict_factory(cursor, row):
    fields = [item[0] for item in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def get_books():
    con = sqlite3.connect(library_filename)
    con.execute(
        """CREATE TABLE IF NOT EXISTS book(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            rating INTEGER NOT NULL)"""
    )
    # con.row_factory = sqlite3.Row
    con.row_factory = dict_factory
    result = con.execute('SELECT * FROM book ORDER BY title').fetchall()
    con.close()
    return result

def add_book(book):
    con = sqlite3.connect(library_filename)
    with con:
        con.execute(
            'INSERT INTO book VALUES(?, ?, ?, ?)', book
        )
    con.close()

def get_book(id):
    con = sqlite3.connect(library_filename)
    con.row_factory = dict_factory
    result = con.execute('SELECT * FROM book WHERE id = ?', (id,)).fetchone()
    con.close()
    return result

def update_book_rating(id, rating):
    con = sqlite3.connect(library_filename)
    with con:
        con.execute('UPDATE book SET rating = ? WHERE id = ?', (rating, id))
    con.close()

def delete_book(id):
    con = sqlite3.connect(library_filename)
    with con:
        con.execute('DELETE FROM book WHERE id = ?', (id,))
    con.close()

library_filename = 'library.db'

if __name__ == '__main__':
    books = get_books()
    print(books)
    add_book((None, 'f','f',1))