# mugshots scraper
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
    maxImages = sys.argv[1]
except:
    maxImages = 1000

# you can optionally index the scraping
# to annotate each time you try scraping
try:
    currentIndex = sys.argv[2]
except:
    currentIndex = 0

folderName = "images_" + str(currentIndex)

# declaration of scraping function
def scrapeMugshots():

    # number of failed images download in a row before giving up
    maxFails = 20

    # number of current fails
    currentFails = 0

    # downloaded images
    downloaded = 0

    # print starting scraping
    print("scraping mugshots")

    # create a new folder for saving scraped imagess
    # check that the folder does not exist
    if not os.path.exists(folderName):
        # create the folder
        os.makedirs(folderName)

    # change diretory
    os.chdir(folderName)

    # open a new google chrome window
    driver = webdriver.Chrome()

    #declare actionChains for right-click
    actionChains = ActionChains(driver)

    # set the window size
    driver.set_window_size(1200, 800)

    # queryBegin for google images search
    queryURL = "https://mugshots.com/US-states/"

    # do the query
    print("query mugshots")

    # do the query
    driver.get(queryURL)

    # wait for loading
    time.sleep(2.0)

    # find div with id subcategories
    mainDiv = driver.find_element_by_id("subcategories")

    # wait for loading
    time.sleep(0.1)

    # fin links inside of the div
    links = mainDiv.find_elements_by_tag_name("a")

    # wait for loading
    time.sleep(0.1)

    # save the links as counties
    counties = list()

    for link in range(len(links)):
        counties.append(links[link].get_attribute("href"))
        print(counties[link])

    # print length of counties
    print("found " + str(len(counties)) + " counties" )

    # wait for loading
    time.sleep(0.1)

    # iterate over each county
    for county in counties:

            # go to county
            print("go to: " + county)

            # open new tab with county
            driver.get(county)

            # wait for loading
            time.sleep(1.0)

            # infinite loop
            # break when can't find images
            while True:
                # retrieve the areas inside of the county
                try:
                    mainDiv = driver.find_element_by_id("subcategories")
                except:
                    break

                # wait for loading
                time.sleep(0.1)

                # fin links inside of the div
                links = mainDiv.find_elements_by_tag_name("a")

                # wait for loading
                time.sleep(0.1)

                # save the links as areas
                areas = list()
                for link in range(len(links)):
                    areas.append(links[link].get_attribute("href"))
                    print(areas[link])

                # print length of counties
                print("found " + str(len(areas)) + " areas" )

                # wait for loading
                time.sleep(0.1)

                # go to each one of them
                # iterate over each county
                for area in areas:

                    # go to county
                    print("go to: " + area)

                    # wait for loading
                    time.sleep(1.0)

                    # open new tab with src
                    driver.get(area)

                    # find the body of the page
                    try:
                        bodyDiv = driver.find_element_by_tag_name("tbody")
                    except:
                        bodyDiv = None

                    # if there is a body
                    if bodyDiv != None:

                        # find the images
                        images = bodyDiv.find_elements_by_tag_name("img")

                        # if there are no images, break
                        if len(images) == 0:
                            break

                        # iterate through images to retrieve links
                        for img in range(len(images)):
                            # get the link of the thumbnail
                            srcThumbnail = images[img].get_attribute("src")

                            # split the srcThumbnail on the period
                            # and append new ending to download full res img
                            src = srcThumbnail.split("110x110.jpg")[0] + "400x800.jpg"

                            # download the image
                            urllib.request.urlretrieve(src, "mugshot_" + str(downloaded))
                            time.sleep(0.1)

                            # print on terminal
                            print("downloaded " + src)

                            # update downloaded counter
                            downloaded = downloaded + 1

                        # find a next button and press it
                        # if there is no button, break
                        try:
                            nextButton = driver.find_element_by_class_name("next page")
                            # press the button
                            nextButtton.click()
                        except:
                            break



    # last sleep to make sure that we see whats going on
    time.sleep(5)

def convertToJPG():

    # change directory if needed
    if os.path.exists(folderName):
        os.chdir(folderName)

    # try to create new folder to store jpg converted files
    try:
        os.makedirs("_jpg")
        print("_jpg folder created")
    except:
        print("_jpg folder already exists, moving on")

    for filename in os.listdir(os.getcwd()):
        # open original image
        if (filename[0] == "i"):
            try:
                PIL.Image.open(filename).convert("RGB").save("_jpg/" + filename + ".jpg", quality=100)
                print("converted " + filename + " to jpg")
            except:
                print("could not convert " + filename)

# call the function for scraping
scrapeMugshots()

# convert all the images to JPG format
convertToJPG()

# final message, goodbye, the end
print("finished scraping yay")
