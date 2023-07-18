class Post:
    def __init__(self, id, title, subtitle, body):
        self.id= id
        self.title = title
        self.subtitle = subtitle
        self.body = body


if __name__ == '__main__':
    posts = [{'id': 1, 'title': '1t', 'subtitle': '1s', 'body': '1b'}, {'id': 2, 'title': '2t', 'subtitle': '2s', 'body': '2b'}]
    posts_obj = []
    for post in posts:
        posts_obj.append(Post(**post)) # ** for dictionary unpacking

    for post in posts_obj:
        print(post.title)