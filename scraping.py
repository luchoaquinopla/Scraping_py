import requests
from bs4 import BeautifulSoup

url = 'https://listado.mercadolibre.com.ar/televisores#D[A:televisores]'
search_term = 'Smart'

# Enviar la solicitud GET
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')

    # Ajusta el selector según la estructura real del HTML
    products = soup.find_all('li', class_='ui-search-layout__item')

    for product in products:
        title = product.find('h2',class_='poly-box').text.strip()
        price = product.find('span', class_='andes-money-amount__fraction').text.strip()
        print(title, price)

