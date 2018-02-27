# gets urls of articles from the NYT that contain the word "trump" and are in the Washington news desk
import urllib2
import json
import time
from newsapi import NewsApiClient

def nyt_api():
  file = open("times_url_trump_news.txt", "w")
  for x in range(0,100):
    if x%10 == 0:
      print "we are on page" + str(x)
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api_key=0cf7eae4173e435ebdcd59bc12ce8536&q=trump&fl=web_url,news_desk&page=' + str(x)
    response = urllib2.urlopen(url)
    urls_txt = response.read()
    urls_json = json.loads(urls_txt)
    for doc in urls_json['response']['docs']:
      if 'new_desk' in doc and doc['new_desk'] == "Washington":
        file.write(str(doc['web_url'])+"\n")
    time.sleep(1)ad

  file.close()

def news_api(q, source):
  # gets urls from articles from WaPo, BBC, Breitbard, Fox
  for x in range(0, 100):
    newsapi = NewsApiClient(api_key="db4d6ae37f90478d966e25d854213e1c")
    urls_json = newsapi.get_everything(q=q,sources=source,page=x)
    if 'articles' in urls_json:
      for doc in urls_json['articles']:
        if 'url' in doc:
          print doc['url']

news_api("trump", "bbc-news")
