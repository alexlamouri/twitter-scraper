# Social Media Scraper

## Description

The suite of web scraping tools uses the Requests external library to perform an HTTP request on a given URL and the BeautifulSoup library to extract the HTML code from the given website.

The suite of web scraping tools is compatible with Instagram and Twitter.

The instagram_scraper.py performs analytics on multiple Instagram accounts and outputs the account name, account handle, account bio, account type, account website, number of followers, number of following and number of posts.

The twitter_scraper.py performs analytics on a Twitter account’s tweets and outputs the tweet author, tweet date, tweet text, number of likes, number of retweets and number of replies.

The suite of web scraping tools is capable of outputting data directly to the console or exporting it to a CSV file.

## Usage

Despite performing different analytics on different social medias, both scrapers function similarly

The Instagram scraper prompts the user for the URL of one or more Instagram accounts. The user can input as many Instagram accounts as necessary (one per line) and uses the “Enter” key to signal the program to stop prompting for additional accounts. The program then performs analytics on each given Instagram account.

The Twitter scraper prompts the user for the URL to a Twitter account. The user inputs the URL to the Twitter account and the program then performs analytics on the ~20 most recent Tweets.

For both programs, the user is prompted for the method of output. If the user chooses the console as the method of output, the output of the programs will be displayed on the user’s console. If the user chooses a CSV file as the method of output, the user will be prompted for the name of a CSV file. A CSV file will then be created with the CSV module, timestamped using the datetime module and the output will then be written to it. 

## Setup

The suite of web scraping tools rely on two external libraries that require installation.

Requests can be installed through here:
http://docs.python-requests.org/en/master/user/install/

BeautifulSoup can be installed through here: https://www.crummy.com/software/BeautifulSoup/#Download
