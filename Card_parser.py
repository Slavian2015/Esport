from bs4 import BeautifulSoup
import requests
import requests as req


resp = req.get('https://ru.dltv.org/matches/370181')
soup = BeautifulSoup(resp.text, 'lxml')

# print(soup.prettify())

with open("Match_card.html", "r", encoding='utf-8') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')