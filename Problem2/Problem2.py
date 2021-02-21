from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import re


# Given the Menu Dict and Key Value, returns the total cost for every item in Menu_Items[KeyVal]
def Find_Total(Menu_Items, item):
    total_cost = 0
    for container in Menu_Items[item]:
        food_price = Menu_Items[item][container]
        food_price_filtered = re.findall(r"[-+]?\d*\.\d+|\d+", food_price)

        for price in food_price_filtered:
            total_cost += float(price)
    return round(total_cost, 2)

if __name__ == "__main__":
    # Storage variables for each item
    # Structure will go: Menu_Items = {"Apps":{...}, "Desserts":{...}}
    Menu_Items = {}
    Apps = {}
    Desserts = {}

    # Key values for Menu_Items
    APPS_KEY = "Apps"
    DES_KEY = "Desserts"

    # URl to web scrap from.
    page_url = "https://armettasrestaurant.com/armettas-menu"

#-------------------------- Scrape Webpage --------------------------

    # opens the connection and downloads html page from url
    uClient = uReq(page_url)

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    # finds each App names and prices from the webpage
    app_item_names = page_soup.findAll("h4", {"data-aid":re.compile("MENU_SECTION0_ITEM.*_TITLE")})
    app_item_prices = page_soup.findAll("div", {"data-aid":re.compile("MENU_SECTION0_ITEM.*_PRICE")})

    # finds each Dessert names and prices from the webpage
    des_item_names = page_soup.findAll("h4", {"data-aid":re.compile("MENU_SECTION4_ITEM.*_TITLE")})
    des_item_prices = page_soup.findAll("div", {"data-aid":re.compile("MENU_SECTION4_ITEM.*_PRICE")})

#-------------------------- Store Data --------------------------

    # loops over each product and grabs attributes about
    # each product

    # Appetizers
    for i in range(0, len(app_item_names) - 1):
        name = app_item_names[i].contents[0] 
        price = app_item_prices[i].contents[0]
        Apps[name] = price

    # Desserts
    for i in range(0, len(des_item_names)):
        name = des_item_names[i].contents[0]
        price = des_item_prices[i].contents[0]
        Desserts[name] = price
        
    # Stores each item into the Menu_Items dict
    Menu_Items[APPS_KEY] = Apps
    Menu_Items[DES_KEY] = Desserts

#-------------------------- Find Total --------------------------

    # rounds the value to 2nd decimal place and converts to a string value 
    total_cost = str(round( (Find_Total(Menu_Items, APPS_KEY)) + (Find_Total(Menu_Items, DES_KEY) ) , 2))

    print("The total price for Appetizers and Desserts is: " + "$" + total_cost)

    input("Enter any Value: ")