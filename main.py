from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all("section", class_="listing-search-item")

with open('output.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Price']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_='listing-search-item__link listing-search-item__link--title').text.replace('\n',
                                                                                                                 '')
        price = list.find('div', class_='listing-search-item__price').text.replace('\n', '')

        info = [title, price]
        thewriter.writerow(info)
