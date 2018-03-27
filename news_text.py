#!/usr/bin/python3
from newspaper import Article
import sys

def url_to_text(url_file, text_file, keyword):
  file = open(url_file, "r")
  output = open(text_file, "w")
  count = 0
  for url in file:
    count+=1
    print(url)
    if count%10 == 0:
      print("writing article: " + str(count))
    article = Article(url)
    try:
      article.download()
      while article.download_state == 0: #ArticleDownloadState.NOT_STARTED is 0
        time.sleep(1)
      article.parse()
      article.nlp()
      if keyword in article.keywords:
        output.write(article.text)
    except:
      pass

def main():
  print("news_text.py started")
  url_file = sys.argv[1]
  text_file = sys.argv[2]
  keyword = sys.argv[3]
  url_to_text(url_file, text_file, keyword)

if __name__ == "__main__":
    main()
