import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://example.com/products?page='
all_data = []

for page in range(1, 6):  # Adjust the range according to the number of pages
    url = base_url + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    products = soup.find_all('div', class_='product')
    
    for product in products:
        name = product.find('h2', class_='product-name').text
        price = product.find('span', class_='product-price').text
        description = product.find('p', class_='product-description').text
        all_data.append({'Name': name, 'Price': price, 'Description': description})

df = pd.DataFrame(all_data)
df.to_csv('all_products.csv', index=False)
