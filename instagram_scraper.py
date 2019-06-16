# --------------------------- Imports ---------------------------


# for scraping
import requests
from bs4 import BeautifulSoup

# for output
import csv
import datetime


# --------------------------- Account Metadata ---------------------------


def get_account_name(metadata):
    
    # Return name or '' if undefined
    if 'name' in metadata:
        index = metadata.index('name') + 2
        return metadata[index]
    else:
        return ''


def get_account_type(metadata):
    
    # Return type or '' if undefined
    if '@type' in metadata:
        index = metadata.index('@type') + 2
        return metadata[index]
    else:
        return '' 


def get_account_handle(metadata):
    
    # Return handle or '' if undefined
    if 'alternateName' in metadata:
        index = metadata.index('alternateName') + 2
        return metadata[index]
    else:
        return ''


def get_account_bio(metadata):
    
    # Return bio or '' if undefined
    if 'description' in metadata:
        index = metadata.index('description') + 2
        return metadata[index]
    else:
        return ''
    
    
def get_account_website(metadata):
    
    # Return website or '' if undefined
    if 'url' in metadata:
        index = metadata.index('url') + 2
        return metadata[index]
        
    else:
        return ''  


# --------------------------- Account Metrics ---------------------------


def get_account_num_followers(data):
    
    # Get string representation of followers
    followers = data.replace('-', ',').split(", ")[0]
    
    # Get number of followers
    num_followers = followers.replace("Followers", '')
    
    # Remove thousand separator
    if ',' in num_followers:
        
        num_followers = num_followers.replace(',', '')          
    
    # Remove decimal separator and apply thousand multiplier
    elif 'k' in num_followers:
        
        num_followers = num_followers.replace('k', '')
        
        num_followers = float(num_followers) * 1000
    
    # Remove decimal separator and apply million multiplier    
    elif 'm' in num_followers:
            
        num_followers = num_followers.replace('m', '')    
        
        num_followers = float(num_followers) * 1000000
      
    # Return number of followers  
    return int(num_followers)


def get_account_num_following(data):
    
    # Get string representation of following
    following = data.replace('-', ',').split(", ")[1]
    
    # Get number of following
    num_following = following.replace("Following", '')
    
    # Remove thousand separator
    if ',' in num_following:
        
        num_following = num_following.replace(',', '')      
    
    # Remove decimal separator and apply thousand multiplier
    if 'k' in num_following:
        
        num_following = num_following.replace('k', '')
        
        num_following = float(num_followers) * 1000
     
    # Remove decimal separator and apply million multiplier   
    if 'm' in num_following:
            
        num_following = num_following.replace('m', '')    
        
        num_following = float(num_following) * 1000000
    
    # Return number of following
    return int(num_following)


def get_account_num_posts(data):
    
    # Get string representation of posts
    posts = data.replace('-', ',').split(", ")[2]
    
    # Get number of posts
    num_posts = posts.replace("Posts", '')
    
    # Remove thousand separator
    if ',' in num_posts:
        
        num_posts = num_posts.replace(',', '')
    
    # Remove decimal separator and apply thousand multiplier
    elif 'k' in num_posts:
        
        num_posts = num_posts.replace('k', '')
        
        num_posts = float(num_posts) * 1000
        
    # Remove decimal separator and apply thousand multiplier
    elif 'm' in num_posts:
            
        num_posts = num_posts.replace('m', '')    
        
        num_posts = float(num_posts) * 1000000     
     
    # Return number of posts   
    return int(num_posts)


# --------------------------- Scraper ---------------------------


if __name__ == "__main__":
    
    # Print info and usage details
    print("=============================================================")
    print("DESCRIPTION")
    print("=============================================================")
    print("This tool is used for analytics on Instagram profiles")
    print("This tool will parse a profile and return metadata and metrics")
    print("=============================================================")
    print()
    
    print("==============================================================")
    print("USAGE") 
    print("==============================================================")
    print("Enter one or more Instagram profile URLs (one URL per line)")
    print("Press the 'ENTER' key when done entering URLs")
    print("==============================================================")
    print()
    
    
    # Initialize profile list
    profile_list = []
    
    # Prompt for profile(s)
    while(True):
        
        profile = input("Instagram profile: ")
        
        # Check if URL is entered
        if profile != "":
            
            # Check if Instagram profile
            if profile.find("instagram") != -1:
        
                data = requests.get(profile)
                
                # Check if Instagram profile is valid
                if data.status_code < 400:  # https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
          
                    # Add to Instagram profile list
                    profile_list.append(profile)
                
                else:
                    
                    print("ERROR: Invalid Instagram profile")
                    
                    continue
                
            else:
                
                print("ERROR: Invalid URL")
                
                continue                
        
        # Check if 'ENTER' key is pressed
        else:
            
            print()
            break
        
  
    # Prompt for output type
    while True:
    
            output = input("Please select between console or CSV file output [CONSOLE/CSV]: ")
            
            print()
            
            # Check if valid output
            if output.upper() == "CONSOLE":
                
                print("==============================================================")
                
                # Timestamp
                print(datetime.datetime.today())
                
                for profile in profile_list:
                    
                    # Request website
                    data = requests.get(profile)
                    
                    # Parse HTML from website
                    html = BeautifulSoup(data.text, "html.parser")
                        
                    # Extract metadata and data from HTML
                    metadata = html.find("script", {"type": "application/ld+json"}).text.split('"')
                    data = html.find("meta", {"name": "description"})["content"]                      
                
                    print("==============================================================")
                    
                    # Metadata
                    print("Account name:", get_account_name(metadata))
                    print("Account handle:", get_account_handle(metadata))
                    print("Account type:", get_account_type(metadata))
                    print("Account bio:", get_account_bio(metadata))
                    print("Account website:", get_account_website(metadata))
                    
                    print()
    
                    # Metrics
                    print("Followers:", get_account_num_followers(data))
                    print("Following:", get_account_num_following(data))
                    print("Posts:", get_account_num_posts(data))
                    
                print("==============================================================")
                print("Analytics completed")
                print("==============================================================")
    
                break
                
            elif output.upper() == "CSV":   
                
                # Prompt for CSV file
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
                    csv_writer.writerow(["account_name", "account_handle", "account_type", "account_bio", "account_website", "", "followers", "following", "posts"])
                    
                    # Perform analytics on each profile
                    for profile in profile_list:
                        
                        # Request profile
                        data = requests.get(profile)
                        
                        # Parse HTML from profile
                        html = BeautifulSoup(data.text, "html.parser")
                            
                        # Extract metadata and data from HTML
                        metadata = html.find("script", {"type": "application/ld+json"}).text.split('"')
                        data = html.find("meta", {"name": "description"})["content"]                                  
                    
                        # Write data
                        csv_writer.writerow([get_account_name(metadata), get_account_handle(metadata), get_account_type(metadata), get_account_bio(metadata), get_account_website(metadata), "",  get_account_num_followers(data), get_account_num_following(data), get_account_num_posts(data)])
                   
                print("==============================================================")     
                print("CSV file generated:", csv_file_name)
                print("==============================================================")
                    
                break
                
            else:
                
                print("ERROR: Invalid output type")
                
                continue