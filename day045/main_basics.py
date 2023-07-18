from bs4 import BeautifulSoup
# to use 'lxml' parser
# import lxml

with open('website.html') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.title)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())

# anchor_tags = soup.find_all('a')
# print(anchor_tags)
# for anchor in anchor_tags:
#     print(anchor.getText())
#     print(anchor.get('href'))

# print(soup.find(name='h1', id='name'))
# print(soup.find(name='h1', class_='title'))

print(soup.select_one('body p em strong a'))
print(soup.select_one('.title').string)