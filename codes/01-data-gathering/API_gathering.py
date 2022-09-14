import requests
import json
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

#-----------------------------------------------------
#USER PARAM
#-----------------------------------------------------
read_file=False     #if false then pull from newsapi
file_name="2021-09-24-H12-M20-S09-newapi-raw-data.json" #ignored if read_file=False

baseURL = "https://newsapi.org/v2/everything?"
total_requests=2
verbose=True

API_KEY='603a31167a5d42eda89f3a1679fa7c08'
TOPIC='American election'


#-----------------------------------------------------
#READ JSON OR GET DICTIONARY FROM CLOUD
#-----------------------------------------------------

#READ FILE INTO DICTIONARY 
if(read_file):
    with open(file_name) as f:
        response = json.load(f)

#GET DATA FROM CLOUD
else:
    URLpost = {'apiKey': API_KEY,
               'q': '+'+TOPIC,
               'sortBy': 'relevancy',
               'totalRequests': 1}

    #GET DATA FROM API
    response = requests.get(baseURL, URLpost) #request data from the server
    # print(response.url); exit()
    response = response.json() #extract txt data from requests

    #GET TIMESTAMP FOR PULL REQUEST
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d-H%H-M%M-S%S")

    with open(timestamp+'-newapi-raw-data.json', 'w') as outfile:
        json.dump(response, outfile, indent=4)

#-----------------------------------------------------
#FUNCTION TO CLEAN STRINGS
#-----------------------------------------------------
def string_cleaner(input_string):
    try: 
        out=re.sub(r"""
                    [,.;@#?!&$-]+  # Accept one or more copies of punctuation
                    \ *           # plus zero or more copies of a space,
                    """,
                    " ",          # and replace it with a single space
                    input_string, flags=re.VERBOSE)

        #REPLACE SELECT CHARACTERS WITH NOTHING
        out = re.sub('[’.]+', '', input_string)

        #ELIMINATE DUPLICATE WHITESPACES USING WILDCARDS
        out = re.sub(r'\s+', ' ', out)

        #CONVERT TO LOWER CASE
        out=out.lower()
    except:
        print("ERROR")
        out=''
    return out
