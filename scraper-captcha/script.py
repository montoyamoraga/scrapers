# scraper-captcha
# by aaron montoya-moraga
# commissioned by ziyu he
# final for class detourning the web
# taught by sam lavigne at nyu itp
# april 2017

# requirements
# runs on python 2.7 on a macbook pro

# installation

# createa virtualenv called env
# virtual env

# activate it
# source env/bin/activate

#install modules
#pip install pillow
#pip install selenium

# here you can work on stuff
# when ready, deactivate environment
# deactivate

# running
# run it with
# python script.py

# reference

# guide for installation based ond
# http://docs.python-guide.org/en/latest/dev/virtualenvs/

# tkinter reference
# https://docs.python.org/2/library/tkinter.html
# http://effbot.org/tkinterbook

# script

#import libraries
import os
from os import system
import sys
import time
import string
import random
from PIL import Image, ImageDraw, ImageFont

# import selenium module for webscraping
# include webdriver for using chrome and Keys for using keyboard commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#python module for handling urls
import urllib

#function definition for
def download_captcha(captcha):

    # new driver using google chrome
    driver = webdriver.Chrome()

    # set the window size of the driver
    driver.set_window_size(1200, 800)

    print "go to fakecaptcha.com"

    # url to be scraped
    complete_url = "https://www.fakecaptcha.com/"

    # go to the url
    driver.get(complete_url)

    # wait for 2 seconds
    time.sleep(2)

    inputElement = driver.find_element_by_id("words")

    #print input_form

    #write captcha on the input form
    inputElement.send_keys(captcha)

    time.sleep(2)

    #hit enter
    inputElement.send_keys(Keys.ENTER)

    #wait
    time.sleep(10)

    print "retrieve button to proceed"

    #retrieve button to proceed
    captchaDone = driver.find_element_by_id("proceed_link")

    print "click on button to proceed"

    #click on the button to proceed
    captchaDone.click()

    #wait
    time.sleep(10)

    #retrieve captcha image
    captcha_image = driver.find_element_by_id("words")

    #retrieve captcha image address
    captcha_source = captcha_image.get_attribute('src')

    #wait
    time.sleep(2)

    #download it
    urllib.urlretrieve(captcha_source, captcha + ".png")

    #wait
    time.sleep(5)

    #close driver
    driver.close()

captchas = ["this", "another", "since", "whatever"]


for captcha in captchas:
    download_captcha(captcha)
