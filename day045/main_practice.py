import json

import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')
response.raise_for_status()

# print(response.content)
# print(response.text)

# soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.content, 'html.parser')
anchor_titles = soup.select('.title .titleline>a')
span_subtext = soup.select('.subtext')

if len(anchor_titles) == len(span_subtext):
    result = []
    for index in range(len(anchor_titles)):
        score_span = span_subtext[index].select_one('.score')
        if score_span:
            score = score_span.string
        else:
            score = ''
        result.append(
            {
                'title': anchor_titles[index].string,
                'link': anchor_titles[index].get('href'),
                'score': score
            }
        )
    with open('hn_output.txt', 'w') as f:
        json.dump(result, f, indent=4)
