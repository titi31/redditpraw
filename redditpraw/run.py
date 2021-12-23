import praw
import requests
import logging
from praw.models import Comment, Submission
import pprint
import json
from io import StringIO
from pathlib import Path
import configparser

home_dir = Path.home()
home_dir_str = str( home_dir )
configFile = Path.home().joinpath( 'dossierConfig', 'config.ini' )
config = configparser.ConfigParser()
config.read(configFile)

reddit = praw.Reddit(
   client_id=config['DEFAULT']['client_id'],
   client_secret=config['DEFAULT']['client_secret'],
   password=config['DEFAULT']['password'],
   user_agent=config['DEFAULT']['user_agent'],
   username=config['DEFAULT']['username'],
)

print(reddit.user.me())

savedcontent = reddit.user.me().saved(limit=None)
listeDesDict=[]
for item in savedcontent:
   print(repr(item))

   if isinstance(item, Comment):
     # print(item.body_html)
      comment=dict(type="comment",body=item.body,url="https://www.reddit.com"+item.permalink)
      listeDesDict.append(comment)
      #print(listeDesDict)
      #print(comment)
      
   elif isinstance(item, Submission):
      submission=dict(type="submission",title=item.title,url=item.url,text=item.selftext)
      #print(submission)
      listeDesDict.append(submission)
      #print("url ",item.url)
      #print("title ",item.title)
      #print("text ",item.selftext)

pprint.pprint(listeDesDict)  

with open('listSaved.json', 'w') as f:
    data = f.write(json.dumps(listeDesDict,indent=4)
)
    print(data)
#print(list(savedcontent))







