import requests
from pprint import pprint
from bs4 import BeautifulSoup
url:str = "https://scrapeme.live/shop/"



def scrap_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")
def get_pokemon_list(soup):
    unordered_list = soup.find("ul",class_="products")
    list_li = unordered_list.find_all("li")
    return list_li
def parse_pokemon(li):
    for i in li:
        title= i.find("h2",class_="woocommerce-loop-product__title").text
        price = i.find("span",class_="price").text
        link = i.find("a",class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")['href']
    pokemon = {
        "name" : title,
        "price" : price,
        "link" : link
    }
    return pokemon
    
    

    
pages = 5
for page in range(1,pages):
    url = "https://scrapeme.live/shop/page/%d"%page
    soup = scrap_page(url)
    listOfLi = get_pokemon_list(soup)
    data = parse_pokemon(listOfLi)
    print(data)