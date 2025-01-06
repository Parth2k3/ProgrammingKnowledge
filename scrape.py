import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Find all the products
product_wrappers = soup.find_all("div", class_ = 'product-wrapper')

# Loop through all the products
list = {}
for product_wrapper in product_wrappers:
    # Find the product name
    product_name = product_wrapper.find("a", class_ = 'title')['title']
    # Find the product price
    product_price = product_wrapper.find("h4", class_ = 'price').text
    list[product_name] = product_price

print(list)