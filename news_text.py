#!/usr/bin/python3
from newspaper import Article
url = "https://www.nytimes.com/2018/01/30/us/politics/fact-check-sotu.html"

article = Article(url)
article.download()
article.parse()

print(article.text)
