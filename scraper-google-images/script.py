# google images scraper
# runs in python 3
# tested on macbook air and macbook pro
# running macos high sierra
# by aaron montoya-moraga
# august 2018

# python dependencies
# these dont need any installation
# os is used for doing directory operations
import os
# sys is used for retrieving arguments from the terminal
import sys
# time is used for making the script pause and wait
import time
# string is used for string operations
import string
# TODO argparse is used for retrieving arguments from the terminal
import argparse
# pip install urllib3
import urllib.request
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# pip install Pillow
import PIL.Image

# execute this file script.py with python 3
# to check the version of python you can open terminal and write
# python --version
# or
# python3 --version
# and it will tell you if you are using python 3

# in this machine my alias is python3, so the command is
# python3 script.py "subject to scrape" maxImages
# where
# script.py is this file, can be retrieved with sys.argv[0]
# "subject to scrape" is a string,  retrievable with sys.argv[1]
# maxImages is a number, retrievable with sys.argv[2]

# retrieve the script
script = sys.argv[0]

# retrieve the subject to be scraped
#  default to "broccoli"
try:
    scrapeSubject = sys.argv[1]
except:
    scrapeSubject = "broccoli"

# retrieve the times of scraping google images
#  default to 4
# try:
#     scrapeTimes = sys.argv[2]
# except:
#     scrapeTimes = 4

try:
    # maxImages = sys.argv[3]
    maxImages = int(sys.argv[2])
except:
    maxImages = 100

# declaration of scraping function
def scrape(subject):

    # number of failed images download in a row before giving up
    maxFails = 20

    # number of current fails
    currentFails = 0

    # print starting scraping
    print("scraping " + subject)

    # create a new folder for saving scraped imagess
    # replace spaces with underscores
    auxSubject = "images_" + subject.replace(" ", "_")
    # check that the folder does not exist
    if not os.path.exists(auxSubject):
        # create the folder
        os.makedirs(auxSubject)

    # open a new google chrome window
    driver = webdriver.Chrome()

    #declare actionChains for right-click
    actionChains = ActionChains(driver)

    # set the window size
    driver.set_window_size(1200, 800)

    # queryBegin for google images search
    queryBegin = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1044&bih=584&q="

    # append subject to complete the query URL
    queryURL = queryBegin + subject

    # do the query
    print("query google images")

    # do the query
    driver.get(queryURL)

    # wait for loading
    time.sleep(1)

    # for i in range(int(scrapeTimes)):
    while True:

        # scroll up and down
        scrollUpDown(driver)

        # wait for everything to load
        time.sleep(3)

        # retrieve buttons
        buttons = driver.find_elements_by_id("smb")

        # click on the first button
        # check that there are buttons
        if len(buttons) > 0:
            # if there is a button, click on it
            try:
                buttons[0].click()
            except:
                print("no button")
                break

    # find all the results
    results = driver.find_elements_by_class_name("rg_l")

    # print on console how many
    print(len(results))

    # change directory
    os.chdir(auxSubject)

    results[0].click()

    # initialize empty list to store downloaded addresses
    downloaded = list()

    counter = 0

    # right click on each of them
    while (len(downloaded) < maxImages) and (currentFails < maxFails):
        # click on it
        #results[i].click()

        # wait
        time.sleep(1.0)

        # save the image
        try:
            #imageXpath = driver.find_element_by_xpath('//img[@class="irc_mi"]')
            imagesXpath = driver.find_elements_by_xpath('//img[@class="irc_mi"]')

            for index in range(len(imagesXpath)):

                src = imagesXpath[index].get_attribute('src')

                subsetDownloaded = downloaded[-3:]

                if not(src in subsetDownloaded):
                # download it
                    urllib.request.urlretrieve(src, auxSubject + "_" +  str(len(downloaded)))
                    print("downloaded " + str(len(downloaded)))
                    time.sleep(0.1)
                    # append it to the downloaded list
                    downloaded.append(src)
                    # reset counter of fails
                    currentFails = 0

        except:
            print("could not save the image")
            # add up to errors
            currentFails = currentFails + 1

        # press the right arrow three times to advance three times
        webdriver.ActionChains(driver).send_keys(Keys.RIGHT).perform()
        webdriver.ActionChains(driver).send_keys(Keys.RIGHT).perform()
        webdriver.ActionChains(driver).send_keys(Keys.RIGHT).perform()
        time.sleep(0.1)

        counter = counter + 3

        # if counter > 1000:
        #     break

    # last sleep to make sure that we see whats going on
    time.sleep(5)

# function for scrolling the browser up and down
def scrollUpDown(driver):
    # repeat ten times
    for i in range(10):
        # go to the end of the site
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # wait
        time.sleep(0.1)
        # go to the beginning of the site
        driver.execute_script("window.scrollTo(0,0);")
        # wait
        time.sleep(0.1)
        # go to the end of the site
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def convertToJPG():
    try:
        os.makedirs("_jpg")
    except:
        print("folder already created")

    for filename in os.listdir(os.getcwd()):
        # open original image
        if (filename[0] == "i"):
            try:
                PIL.Image.open(filename).convert("RGB").save("_jpg/" + filename + ".jpg", quality=100)
                print("converted " + filename + " to jpg")
            except:
                print("could not convert " + filename)

# call the function for scraping
scrape(scrapeSubject)

# convert all the images to JPG format
convertToJPG()

# final message, goodbye, the end
print("finished scraping yay")
