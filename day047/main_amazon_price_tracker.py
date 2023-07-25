import os
import re

import dotenv
import requests
from bs4 import BeautifulSoup


def get_amazon_product_code(amazon_product_url):
    try:
        return re.match(r'^https://www\.amazon\.com.+/dp/([A-Z0-9]+)/.+', amazon_product_url).group(1)
    except:
        return None
    
def urljoin(*args):
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


dotenv.load_dotenv()

product_url = os.environ.get('PRODUCT_URL')
amazon_product_code = get_amazon_product_code(product_url)
camelcamelcamel_url = 'https://au.camelcamelcamel.com/product/'
product_comparing_url = urljoin(camelcamelcamel_url, amazon_product_code)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}


response = requests.get(product_comparing_url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')
product_name = soup.select_one(f'h2 a[href="{product_comparing_url}"]').string
amazon_price_history = soup.find(name='table', class_='product_pane')
current_price = float(amazon_price_history.select_one('tbody > tr td:nth-of-type(2)').string[1:])
average_price = float(amazon_price_history.select_one('tbody tr:nth-of-type(4) td:nth-of-type(2)').string[1:])
lowest_price = float(amazon_price_history.select_one('tbody .lowest_price td:nth-of-type(2)').string[1:])

if current_price < average_price and current_price <= lowest_price * 1.2:
    print(f'Price for "{product_name}" has dropped to a reasonable range!\nCurrent price: {current_price}\nLowest price: {lowest_price}')


