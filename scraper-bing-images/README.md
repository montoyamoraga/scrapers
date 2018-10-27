# scraper-bing-images

## About

This tutorial is for scraping images from bing Images, using Python 3.

It works on both Mac and Windows.

For Mac, open the app Terminal to execute the commands.

For Windows, open Command prompt to execute the commands.

## Using this code

These instructions and the code of this tutorial live on a folder. A more detailed version is that it is a special type of folder called [repository](https://en.wikipedia.org/wiki/Software_repository), because it has [version control](https://en.wikipedia.org/wiki/Version_control), in particular [Git](https://en.wikipedia.org/wiki/Git), and is hosted at [GitHub](https://en.wikipedia.org/wiki/GitHub).

In order to use the code, you have two options, either download or clone this repository, either one is fine:

* Download this repository: click the green *Clone or download* button and choose *Download ZIP*. After downloading, uncompress the folder and place it somewhere you like, for example, your desktop.
*  Clone this repository: open terminal, cd to a location on your computer and run the following command

```bash
git clone https://github.com/montoyamoraga/scrapers/
```

## Terminal / Command prompt

### For Mac

For installing software and running the scraper, We will use the Terminal app. You can find it under Applications/Terminal.app. A cool alternative to the native Terminal app is [iTerm2](https://www.iterm2.com/), which can be downloaded for free and is highly customizable.

### For Windows

For installing software and running the scraper, We will use the Command Prompt app. You can find it by searching "Command Prompt" or even "Terminal" on your Windows system.

## Installation

### For Mac

* Install [Homebrew](https://brew.sh/). Follow the instructions on their website, it might take a while.

* Install Python3 with Homebrew

```bash
brew install python3
```

* Install Chromedriver with Homebrew

```bash
brew tap caskroom/cask
```

```bash
brew cask install chromedriver
```

### For Windows

* Download [Chromedriver](http://chromedriver.chromium.org/downloads) from their website.

* Unzip the folder and place the file *chromedriver.exe* inside of a folder of C:

* Now add this folder to the PATH with the following steps:

1. Search for the "Edit the system environment variables" in the "Control panel".
2. Click on the button "Environment Variables..."
3. Select "Path" and click on the button "Edit"
4. Click on the Button "New"
5. Add the folder where *chromedriver.exe* lives and click on OK.
6. Click on the next two OK buttons to save the changes.
7. If you have the "Command prompt" app open, close it and re-open it.
8. To make sure that "chromedriver" is part of "Path", on the command prompt do

```bash
chromedriver
```

### For Linux

TODO

## Instructions

* Open Terminal on Mac or Command Prompt on Windows and cd to the folder where this code lives. To check that you are on the right folder, you can execute on a Mac:

```bash
ls
```

or on a Windows

```bash
dir
```

and it should print on the Terminal / Command Prompt the contents of this folder, including at least these instructions (README.md) and the Python script (script.py).

* Create a virtualenv called *env*

TODO: explain why virtual environments are awesome.

```bash
python3 -m venv env
```

* Activate the instance of the virtual environment

Mac:

```bash
source env/bin/activate
```

Windows:

```bash
env\Scripts\activate.bat
```

Now the terminal should say (env) at the beginning of each new line, which means our virtual environment called *env* is activated, yay.

* Optional: upgrade [pip](https://en.wikipedia.org/wiki/Pip_(package_manager))

```bash
pip3 install --upgrade pip
```

* Install [selenium](https://www.seleniumhq.org/)

```bash
pip3 install selenium
```

* Install [Pillow](https://python-pillow.org/)

```bash
pip3 install Pillow
```

* Run the Python script *script.py*.

The first argument is *subject*, it is the query to be searched in Google Images. It is a [String](https://en.wikipedia.org/wiki/String_(computer_science)). You can replace it to whatever you want. Make sure that you use double quotes "". It defaults to "broccoli".

The second argument is *maxImages*, it equals the maximum amount of results you want to get, you can replace it with a number. It defaults to 100.

```bash
python3 script.py "subject" maxImages
```

* Find your scraped images

The raw files with the images will live in the folder *images_subject/*, where subject is the string that you scraped.

Inside of that folder, there is an additional folder *_jpg/* with the images converted to .jpg format

* To finish, deactivate the virtual environment with the following command

```bash
deactivate
```

or close the Terminal / Command Prompt.

## Contribute

If you find any bug or mistake, or want to propose any change, please submit an [issue](https://github.com/montoyamoraga/edu12-scraping-google-images/issues/new).

## License

[MIT License](LICENSE)
