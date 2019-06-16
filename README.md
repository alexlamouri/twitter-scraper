Program

Description

In our project proposal, we proposed to build a suite of web scraping tools for different websites. 

For our final project, we instead built a suite of web scraping tools for social media analytics.

Our suite of web scraping tools uses the Requests external library to perform an HTTP request on a given URL and the BeautifulSoup library to extract the HTML code from the given website.

Our suite of web scraping tools is compatible with Instagram and Twitter.

Our instagram_scraper.py performs analytics on multiple Instagram accounts and outputs the account name, account handle, account bio, account type, account website, number of followers, number of following and number of posts.

Our twitter_scraper.py performs analytics on a Twitter account’s tweets and outputs the tweet author, tweet date, tweet text, number of likes, number of retweets and number of replies.

Our suite of web scraping tools is capable of outputting data directly to the console or exporting it to a CSV file.


Usage

Despite performing different analytics on different social medias, both scrapers function similarly

The Instagram scraper prompts the user for the URL of one or more Instagram accounts. The user can input as many Instagram accounts as necessary (one per line) and uses the “Enter” key to signal the program to stop prompting for additional accounts. The program then performs analytics on each given Instagram account.

The Twitter scraper prompts the user for the URL to a Twitter account. The user inputs the URL to the Twitter account and the program then performs analytics on the ~20 most recent Tweets.

For both programs, the user is prompted for the method of output. If the user chooses the console as the method of output, the output of the programs will be displayed on the user’s console. If the user chooses a CSV file as the method of output, the user will be prompted for the name of a CSV file. A CSV file will then be created with the CSV module, timestamped using the datetime module and the output will then be written to it. 





Setup

Our suite web scraping tools rely on two external libraries that require installation.

Requests can be installed through here:
http://docs.python-requests.org/en/master/user/install/

BeautifulSoup can be installed through here: https://www.crummy.com/software/BeautifulSoup/#Download


Project Outcome

Successes

We were able meet the requirements for the project and made significant use of input, output and external packages.

Our code was also well composed for reuse through the use of functions and followed the code format standard with clear and concise internal code comments.

We solved the problem we outlined in the project proposal and were able to parse social medias without the use of an API.


Failures

In our original proposal, we outline that we wanted two facets to the web scraper; a social media scraper capable of receiving data from Twitter, Facebook and Instagram, and a marketplace scraper which would download data from an Amazon item page. 

Unfortunately, due to technical limitations, we were restricted to operating with Twitter and Instagram, the latter of which still did not allow for full capabilities. 

Due to Facebook's use of an Application Programming Interface (API) we were unable to extract any data from the website without the use of one. 

Due to Facebook's ownership over Instagram, we were also unable to parse most of the information without the use of an API. We were not able to scrape a user’s timeline or different posts and were instead limited to only the metadata on each profile. 

In regard to the marketplace scraper aspect of our web scraper, we were once again unable to scrape information from Amazon due to their use of an API. We were therefore forced to discontinue the marketplace aspect of the project. 
