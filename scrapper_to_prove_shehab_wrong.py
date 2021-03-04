import requests
import json
import re
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import numpy as np

from selenium import webbrowser
from splinter import Browser
from selenium.webbrowser.common.keys import Keys

import time
from selenium.webbrowser.support.ui import WebbrowserWait
from selenium.common.exceptions import TimeoutException

from selenium import webbrowser
from webbrowser_manager.chrome import ChromebrowserManager

browser = webbrowser.Chrome(ChromebrowserManager().install())

vegan = "https://www.walmart.com/grocery/browse?shelfId=3480448166&povid=opd_plant-based_zone3"
dessert = "https://www.walmart.com/grocery/products?aisle=1255027787071_1255027788061"

executable_path = {'executable_path': '/usr/local/bin/chromebrowser'}
browser = Browser('chrome', incognito=False)


browser.visit(vegan)
addToCartBurrito = "//*[@id='item-149883737']/div/div[3]/div/div/button"
browser.find_by_xpath(addToCartBurrito).click()

# for a in burrito_button:
#     a.click()

addToCartDeli = "//*[@id='item-156009403']/div/div[3]/div/div/button"
browser.find_by_xpath(addToCartDeli).click()

# for b in deli_button:
#     b.click()

addToCartPizza = "//*[@id='item-686683837']/div/div[3]/div/div/button"
pizza_button = [browser.find_by_xpath(addToCartPizza), browser.find_by_xpath(addToCartPizza)]

for c in pizza_button:
    c.click()

timeout = 5
try:
    myElem = WebbrowserWait(browser, timeout)
except TimeoutException:
    print("Timed out waiting for page to load")


browser.visit(dessert)
addToCartCoconutPie = '//*[@id="item-12166772"]/div/div[3]/div/div/button'
browser.find_by_xpath(addToCartCoconutPie).click()

# for d in coconutPie_button:
#     d.click()

addToCartCheeseCake12 = '//*[@id="item-12166772"]/div/div[3]/div/div/button'
browser.find_by_xpath(addToCartCheeseCake12).click()

# for e in cheeseCake12_button:
#     e.click()

checkout = "//*[@id='shoppingCart']/div/div/footer/div/button"
browser.find_by_xpath(checkout).click()

# for f in checkout_button:
#     f.click()


email = "nadaibrahim96@gmail.com"
psw = "White1996!"
address = '3513 John F Kennedy Blvd'
line_2 = 'Apt 4'
city = 'Jersey City'
state = 'NJ'
zipcode = '07307'


try:

    # time.sleep(3)

    # browser.find_by_xpath("//*[@id='email-su']").first.fill(email)

    # time.sleep(3)

    # browser.find_by_xpath("//*[@id='password-su']").first.fill(psw)

    time.sleep(3)

    sign_in = '//*[@id="sign-in-form"]/button[1]'
    browser.find_by_xpath(sign_in).click()

    # for g in signIn_button:
    #     g.click()
    
    delivery = '/html/body/div/div[1]/div/section/div[1]/div/div/section/div[1]/div/div[1]/button[2]'
    browser.find_by_xpath(delivery).click()

    # for h in delivery_tab:
    #     h.click()

    # addAddress = '//*[@id="panel-1"]/div/button'
    # addAddy_button = browser.find_by_xpath(addAddress)

    # for i in addAddy_button:
    #     i.click()
    
    # time.sleep(3)

    # browser.find_by_xpath('//*[@id="addAddressForm"]/div[1]/div[1]/input').first.fill(address)

    # time.sleep(3)

    # browser.find_by_xpath('//*[@id="line2"]').first.fill(line_2)

    # time.sleep(3)

    # browser.find_by_xpath('//*[@id="city"]').first.fill(city)

    # time.sleep(3)

    # browser.find_by_xpath('//*[@id="state"]').first.fill(state)

    # time.sleep(3)

    # browser.find_by_xpath('//*[@id="postalCode"]').first.fill(zipcode)

    # time.sleep(3)

    # browser.find_by_xpath('//*[@id="primaryPhoneNumber"]').first.fill('2016268719')

    # time.sleep(3)

    savedAddy = '//*[@id="panel-1"]/div/ul/li[2]/label/i'
    savedAddy_button = browser.find_by_xpath(savedAddy).click()

    continue_button = '/html/body/div/div[2]/div[1]/section[2]/div/div[2]/button'
    browser.find_by_xpath(save).click()

    # for j in save_button:
    #     j.click()

    change_button = '/html/body/div/div[2]/div[2]/section/div/button'
    browser.find_by_xpath(change_button).click()

    express_shipping = '/html/body/div/div[1]/div/section/div[1]/div/div/section/div[1]/div/div[3]/div[3]/label/i'
    browser.find_by_xpath(express_shipping).click()

    continue_pt2 = '/html/body/div/div[1]/div/section/div[1]/div/div/section/div[1]/div/div[6]/div/button'
    browser.find_by_xpath(continue_pt2).click()

    addPayment = '/html/body/div[1]/div[1]/div/section/div[1]/main/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div/span/span[1]/i'
    browser.find_by_xpath(addPayment).click()

    CVV = '/html/body/div[1]/div[1]/div/section/div[1]/main/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div/span/span[2]/div/div[2]/div[2]/form/label/div/div/input'
    browser.find_by_xpath(CVV).first.fill('500')

    enterButton = '/html/body/div[1]/div[1]/div/section/div[1]/main/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div/span/span[2]/div/div[2]/div[3]/button[2]'
    browser.find_by_xpath(enterButton).click()

    continue_pt3 = '/html/body/div[1]/div[1]/div/section/div[1]/main/div/div[4]/button'
    browser.find_by_xpath(continue_pt3).click()

    placeOrder = '/html/body/div[1]/div[1]/div/section/div[1]/div/div[10]/div/div/button'
    browser.find_by_xpath(placeOrder).click() 
    
    print("You're stupid shehab")

except:
    print("welp, you were right shehab")











