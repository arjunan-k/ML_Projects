# ------------------------------------Process Started------------------------------------- #

# Including packages of beautifulsoup.
from bs4 import BeautifulSoup
import requests

# Setting the zillow website customized URL and headers parameter.
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22map" \
             "Bounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37" \
             ".609299211511704%2C%22north%22%3A37.94091184009742%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3A" \
             "true%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%" \
             "7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22" \
             "value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%" \
             "2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A800%7D%2C%22price%22%3A%7B%22min%" \
             "22%3A179019%7D%7D%2C%22isListVisible%22%3Atrue%7D"
HEADERS = {
    "User-Agent": "Type your user agent",
    "Accept-Language": "Type your accept language"
}


class Zillow:                     # Creating a class.

    def __init__(self):
        self.addresses = []
        self.prices = []
        self.links = []

    # Creating a method to get address list.

    def address_list(self):
        response = requests.get(url=ZILLOW_URL, headers=HEADERS)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")

        address = soup.find_all(class_="list-card-addr")
        for each in address:
            self.addresses.append(each.text)
        return self.addresses

    # Creating a method to get price list.

    def price_list(self):
        response = requests.get(url=ZILLOW_URL, headers=HEADERS)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")

        price = soup.find_all(class_="list-card-price")
        for each in price:
            self.prices.append(each.getText().split()[0].replace("+", ""))
        return self.prices

    # Creating a method to get link list.

    def link_list(self):
        response = requests.get(url=ZILLOW_URL, headers=HEADERS)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")

        start_link = "https://www.zillow.com"
        link = soup.find_all('a', class_="list-card-link")
        for each in link:
            if str("https") not in each['href']:
                self.links.append(start_link + each['href'])
            else:
                self.links.append(each['href'])
        return self.links

# ------------------------------------Process Finished------------------------------------ #