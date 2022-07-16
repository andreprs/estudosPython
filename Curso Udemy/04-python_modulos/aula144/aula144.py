import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

# os termos seguidos de ponto ' . ' são classes CSS dos sites
# para cada web scraping isso será diferente e dependerá do site
for pergunta in html.select('.s-post-summary.js-post-summary'):
    titulo = pergunta.select_one('.s-post-summary--content-title')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')
    print(data.text, titulo.text, votos.text, sep='\t')
    