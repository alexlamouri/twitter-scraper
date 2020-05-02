# --------------------------- Imports ---------------------------


# for scraping
import requests
from bs4 import BeautifulSoup

# for output
import csv
import datetime


# --------------------------- Tweet Data ---------------------------


def get_tweet_author(tweet):
    
    # Find name box
    name_box = tweet.find("strong", {"class": "fullname show-popup-with-id u-textTruncate"})
    
    # Get tweet author
    name = name_box.text   
    
    return name


def get_tweet_date(tweet):
    
    # Find timestamp box
    timestamp_box = tweet.find("small", {"class": "time"})
    
    # Get timestamp
    timestamp = timestamp_box.find("a", {"class": "tweet-timestamp js-permalink js-nav js-tooltip"})
    
    return timestamp["title"]
         
                       
def get_tweet_text(tweet):
    
    # Get tweet text
    text_box = tweet.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
    text = text_box.text
    
    # Remove images
    images = text_box.find_all("a", {"class": "twitter-timeline-link u-hidden"})
    for image in images:
        text = text.replace(image.text, '')

    return text


def get_tweet_num_replies(tweet):
    
    # Find reply button
    reply_button = tweet.find("button", {"class": "ProfileTweet-actionButton js-actionButton js-actionReply"})
    
    # Get number of replies
    num_replies = reply_button.find("span", {"class": "ProfileTweet-actionCountForPresentation"}).text
    
    # Return number of replies or 0 if undefined
    if num_replies:
        return num_replies
    else:
        return 0
    
    
def get_tweet_num_retweets(tweet):
    
    # Find retweet button
    retweet_button = tweet.find("button", {"class": "ProfileTweet-actionButton js-actionButton js-actionRetweet"})
    
    # Get number of retweets
    num_retweets = retweet_button.find("span", {"class": "ProfileTweet-actionCountForPresentation"}).text
    
    # Return number of retweets or 0 if undefined
    if num_retweets:
        return num_retweets
    else:
        return 0
    
    
def get_tweet_num_likes(tweet):
    
    # Find like button
    like_button = tweet.find("button", {"class": "ProfileTweet-actionButton js-actionButton js-actionFavorite"})
    
    # Get number of likes
    num_likes = like_button.find("span", {"class": "ProfileTweet-actionCountForPresentation"}).text
    
    # Return number of likes or 0 if undefined
    if num_likes:
        return num_likes
    else:
        return 0


# --------------------------- Scraper ---------------------------


if __name__ == "__main__":
    
    # Print info and usage details
    print("======================================================================")
    print("DESCRIPTION")
    print("======================================================================")
    print("This tool is used for analytics on a Twitter profile's tweets")
    print("This tool will parse a profile's most recent tweets and return metrics")
    print("======================================================================")
    print()
    
    print("======================================================================")
    print("USAGE") 
    print("======================================================================")
    print("Enter a PUBLIC Twitter profile URL")
    print("Note: Analytics can only be performed on PUBLIC Twitter profiles")
    print("======================================================================")
    print()
    
    
    # Prompt for profile(s)
    while(True):
        
        profile = input("Twitter profile: ")
        
        # Check if Twitter profile
        if profile.find("twitter") != -1:
        
                data = requests.get(profile)
                
                # Check if Twitter profile is valid
                if data.status_code < 400:  # https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
                    
                    # Request profile
                    data = requests.get(profile)
                    
                    # Parse HTML from profile
                    html = BeautifulSoup(data.text, "html.parser")   
                    
                    # Parse most recent tweets (~20)
                    tweets = html.find_all("li", {"data-item-type": "tweet"})  
                    
                    break
                
                else:
                    
                    print("ERROR: Invalid Twitter profile")
                    
                    continue
                
        else:
                
            print("ERROR: Invalid URL")
                
            continue       
        
  
    # Prompt for output type
    while True:
    
            output = input("Please select between console or CSV file output [CONSOLE/CSV]: ")
            
            print()
            
            # Check if valid output
            if output.upper() == "CONSOLE":            
                
                print("======================================================================")
                
                # Timestamp
                print(datetime.datetime.today())
                
                # Perform analytics on each tweet
                for tweet in tweets:
                    
                    print("======================================================================")
                   
                    # Metadata
                    print("Author: ", get_tweet_author(tweet))
                    print("Date: ", get_tweet_date(tweet))
                    print("Text: ", get_tweet_text(tweet))
                    
                    print()
                    
                    # Metrics
                    print("Replies: ", get_tweet_num_replies(tweet))
                    print("Retweets: ", get_tweet_num_retweets(tweet))
                    print("Likes: ", get_tweet_num_likes(tweet))           
            
                print("======================================================================")
                print("Analytics completed")
                print("======================================================================")
    
                break
                
            elif output.upper() == "CSV":

                # Prompt for csv file   
                csv_file_name = input("Enter the name of the CSV file to output: ")
                
                # Check if CSV file
                if csv_file_name.split('.')[-1] != "csv":
                    # Add CSV extension
                    csv_file_name += ".csv"
                        
                with open(csv_file_name, mode='w') as csv_file:
                    
                    csv_writer = csv.writer(csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                    
                    # Write timestamp
                    csv_writer.writerow([str(datetime.datetime.today())])
                    
                    # Write header
                    csv_writer.writerow(["tweet_author", "tweet_date", "tweet_text", "", "num_replies", "num_retweets", "num_likes"])
                
                    # Perform analytics on each tweet
                    for tweet in tweets:                                
                    
                        # Write data
                        csv_writer.writerow([get_tweet_author(tweet), get_tweet_date(tweet), get_tweet_text(tweet), "",  get_tweet_num_replies(tweet), get_tweet_num_retweets(tweet), get_tweet_num_likes(tweet)])
                   
                print("======================================================================")       
                print("CSV file generated:", csv_file_name)
                print("======================================================================")
                    
                break
                
            else:
                
                print("ERROR: Invalid output type")
                
                continue