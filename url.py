import urllib2
import json
import time
from newsapi import NewsApiClient
import requests
import sys

# writes on a txt file the urls of articles that are from a specific news source
# & contain a keyword
# sources of interest : nyt-news, bbc-news, breitbart-news, fox-news, the-washington-post
# we can use any source from https://newsapi.org/sources
# pages is the number of pages of output we take urls from
#
# for the NYT we use their api, otherwise we use news-api

def url_to_file(keyword, source, url_file, pages):
  file = open(url_file, "w")
  file.close()
  print "file made"
  for x in range(0, pages):
    file = open(url_file, "a")
    # if x%10 == 0:
      # print "we are on page" + str(x)
    # we use the nyt-news specific api
    if source == "nyt-news":
      api_key = "d0f50c9ffa054618af85585df5488cca"
      # api_key = "9d2b6db663c540fdadbbccdb9829695f"
      # api_key = "0cf7eae4173e435ebdcd59bc12ce8536"
      try:
        url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api_key=' + api_key + '&q=' + keyword +'&l=web_url,news_desk&page=' + str(x)
        print(url)
        response = urllib2.urlopen(url)
        urls_txt = response.read()
        urls_json = json.loads(urls_txt)
        for doc in urls_json['response']['docs']:
          # we probably should not only look at Washington
          if 'new_desk' in doc and doc['new_desk'] == "Washington":
            file.write(doc['web_url'].encode('utf-8')+"\n")
        time.sleep(1)
        file.close()
      except:
        file.close()
        print "failed" + str(x)
        pass
    # we use the newsapi.org api
    else:
      #apiKey="02bdf3a4b50a4fa0aee7ba5fd4a38115"
      #apiKey="963778fe197b4fddbc7d3455d30a8ee0"
      #apiKey="db4d6ae37f90478d966e25d854213e1c"
      apiKey="b980781d85c34978894cf98a61f90fc0"
      newsapi = NewsApiClient(apiKey)
      print "connected"
      start_url = 'https://newsapi.org/v2/everything?'
      keyword_url = 'q=' + keyword
      source_url = '&sources=' + source
      pagesize_url = '&pageSize=' + str(100)
      page_url = '&pages=' + str(x)
      api_url = '&apiKey=' + apiKey
      url = start_url + keyword_url + source_url + pagesize_url + page_url+api_url
      print url
      #urls_json = newsapi.get_everything(q=keyword,sources=source, pageSize=100, page=x)
      response = urllib2.urlopen(url)
      urls_txt = response.read()
      urls_json = json.loads(urls_txt)
      if 'articles' in urls_json:
        for doc in urls_json['articles']:
          if 'url' in doc:
            file.write(doc['url'].encode('utf-8')+"\n")
  file.close()
  print "urls done"

def main():
  keyword = sys.argv[1]
  source = sys.argv[2]
  file_name = sys.argv[3]
  pages = int(sys.argv[4])
  url_to_file(keyword, source, file_name, pages)

if __name__ == "__main__":
    main()
