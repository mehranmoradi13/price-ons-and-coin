import requests
from bs4 import BeautifulSoup
url = "https://www.tgju.org"
page = requests.get(url)
# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
results_sekeh = soup.find(id="l-sekee")
results_ons = soup.find(id="l-ons")
# print(results_sekeh.prettify())
# print(results_ons.prettify())

ons = results_ons.findChild(class_="info-price")
ons = ons.text
sekeh = results_sekeh.findChild(class_="info-price")
sekeh = sekeh.text
print("sekeh = ",sekeh)
print("ons = ",ons)
print('*' * 40)
# dolar = (sekeh / ons ) * 4.5
# print("dolar = ". dolar)