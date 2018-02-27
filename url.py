import urllib2
import json
import time
from newsapi import NewsApiClient

# writes on a txt file the urls of articles that are from a specific news source
# & contain a keyword
# sources of interest : nyt-news, bbc-news, breitbard-news, fox-news, the-washington-post
# we can use any source from https://newsapi.org/sources
# pages is the number of pages of output we take urls from
#
# for the NYT we use their api, otherwise we use news-api

def get_url(keyword, source, file_name, pages):
  file = open(file_name + ".txt", "w")
  print "file made"
  for x in range(0, pages):
    if x%10 == 0:
      print "we are on page" + str(x)
    # we use the nyt-news specific api
    if source == "nyt-news":
      url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api_key=0cf7eae4173e435ebdcd59bc12ce8536&q=' + keyword +'&l=web_url,news_desk&page=' + str(x)
      response = urllib2.urlopen(url)
      urls_txt = response.read()
      urls_json = json.loads(urls_txt)
      for doc in urls_json['response']['docs']:
        # we probably should not only look at Washington
        if 'new_desk' in doc and doc['new_desk'] == "Washington":
          file.write(str(doc['web_url'])+"\n")
      time.sleep(1)
    # we use the newsapi.org api
    else:
      newsapi = NewsApiClient(api_key="db4d6ae37f90478d966e25d854213e1c")
      urls_json = newsapi.get_everything(q=keyword,sources=source,page=x)
      if 'articles' in urls_json:
        for doc in urls_json['articles']:
          if 'url' in doc:
            file.write(str(doc['url'])+"\n")
  file.close()

get_url("trump", "nyt-news", "test", 10)
