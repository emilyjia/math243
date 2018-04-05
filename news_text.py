#!/usr/bin/python3
from newspaper import Article
import sys
import time

def download_url(url):
  article = Article(url)
  article.download()
  article.parse()
  print(article.text)

def url_to_text(url_file, text_file, keyword):
  file = open(url_file, "r")
  output = open(text_file, "w")
  output.close()
  count = 0
  article_count = 0
  for url in file:
    url = str(url)
    article = Article(url)
    print(article.url)
    try:
      article.download()
      article.parse()
      print("downloaded")
      while article.download_state == 0: #ArticleDownloadState.NOT_STARTED is 0
        time.sleep(1)
      article.nlp()
      if keyword in article.keywords:
        output = open(text_file, "a")
        output.write('============================' + "\n")
        output.write(article_count + ": " + url)
        output.write('============================' + "\n")
        output.write(article.text)
        print(len(article.text))
        output.close()
        article_count+=1
    except:
      print("failure")
      pass
  output.write(str(article_count))

def main():
  print("news_text.py started")
  url_file = sys.argv[1]
  text_file = sys.argv[2]
  keyword = sys.argv[3]
  url_to_text(url_file, text_file, keyword)

if __name__ == "__main__":
    main()
