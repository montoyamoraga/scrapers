#instagram scraper
#march 2017
#by aaron montoya-moraga

#first install virtualenv
#pip install virtualenv env

#then initiate the virtualenv with python 2.7s
#virtualenv -p python2.7 env

#here starts the script

#import sys, time, string, random, urllib, bs4, system, pil modules
import os
from os import system
import sys
import time
import string
import random

#import selenium module for webscraping
#include webdriver for using chrome and Keys for using keyboard commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import urllib

#main function declaration
def download_instagram_pics(handle):

    #new driver using google chrome
    driver = webdriver.Chrome()

    #set the window size of the driver
    driver.set_window_size(1200, 800)

    #variable for going to next page
    isNext = True

    #url to be scraped
    base_url = "https://www.instagram.com/"

    complete_url = base_url + handle

    #go to the url
    driver.get(complete_url)

    #wait for 2 seconds
    time.sleep(2)

    print "retrieve pics"
    x = retrieve_pics(driver, 100)
    #next_pic = driver.find_element_by_css_selector("._ovg3g")
    #next_page.click()
    #catches the exception and breaks the while loop
    #to close the browser window
    driver.quit()

#function for retrieving headline on every page
#gets passed the driver in order to be able to access to its methods
def retrieve_pics(driver, scrollTimes):
    #retrieve the titles of each pinera speech on each page
    #images = driver.find_elements_by_css_selector("._ovg3g")

    #images[0].click()
    time.sleep(10)

    #you have 10 seconds to hit on load more!!!!
    print "user: go to the browser, scroll down and click on the load more button plz"

    #create new folder pics
    system("mkdir pics")
    #cd into the folder
    system("cd pics")

    #make all of the images appear
    for i in range(scrollTimes):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.1)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.1)

    #find images on the site
    images = driver.find_elements_by_tag_name("img");

    #reset counter
    counter = 0

    #iterate through all of the images
    for image in images:
        imageSrc = image.get_attribute('currentSrc')
        print imageSrc
        #save the images to the pics folder, as counter.png
        urllib.urlretrieve(imageSrc, "./pics/" + str(counter) + ".png")
        counter = counter + 1

    #wait 1 seconds
    time.sleep(1)

    #return and end main
    return 1

#call the download_jessen function
download_instagram_pics("skylarjessen")
