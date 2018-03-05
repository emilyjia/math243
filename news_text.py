#!/usr/bin/python3
from newspaper import Article

def main():
  file_name = input("File with url's: ")
  write_to = input("Output file name: ")
  keyword = input("Keyword: ")
  file = open(file_name, "r")
  output = open(write_to, "w")
  for url in file:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    if keyword in article.keywords:
    # we don't actually want to print...
      output.write(article.text)

if __name__ == "__main__":
    main()
