import json

import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')
div_articles = soup.find_all(name='div', class_='article-title-description__text')[::-1]
# div_articles.reverse()
movies = []

for div_article in div_articles:
    title_section = div_article.find(name='h3', class_='title').string
    title_parts = title_section.split(') ')
    if len(title_parts) < 2:
        title_parts = title_section.split(': ')
    try:
        year = div_article.select_one('.descriptionWrapper p strong').string
    except:
        year = 'N/A'
    movies.append({
        'rank': title_parts[0],
        'title': title_parts[1],
        'year': year
    })

with open('best_movies.txt', 'w') as f:
    json.dump(movies, f, indent=4)