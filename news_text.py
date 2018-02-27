#!/usr/bin/python3
from newspaper import Article

def main():
  file_name = input("File with url's: ")
  keyword = input("Keyword: ")
  file = open(file_name, "r")
  for url in file:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    if keyword in article.keywords)
    # we don't actually want to print...
      print(article.text)

if __name__ == "__main__":
    main()
