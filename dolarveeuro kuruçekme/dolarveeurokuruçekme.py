from bs4 import BeautifulSoup
import requests

## Dolar Kuru

url1 = "https://www.google.com/finance/quote/USD-TRY?hl=tr"

sayfa1 = requests.get(url1)

html_sayfa = BeautifulSoup(sayfa1.content,"html.parser")

dolar = html.sayfa1.find("div",class_="YMlKec fxKbKc").getText()

roundeddolar = round(float(dolar.replace(",",".")),2)

dolarmessage = "Dolar = " + str(roundeddolar) + " TL"

print(dolarmessage)


## Euro Kuru

url2 = "https://www.google.com/finance/quote/USD-TRY?hl=tr"

sayfa2 = requests.get(url2)

html_sayfa = BeautifulSoup(sayfa2.content,"html.parser")

euro = html.sayfa2.find("div",class_="YMlKec fxKbKc").getText()

roundedeuro = round(float(euro.replace(",",".")),2)

euromessage = "Euro = " + str(roundedeuro) + " TL"

print(euromessage)

