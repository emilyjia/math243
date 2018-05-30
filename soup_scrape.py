import re, urllib2
import numpy as np
from bs4 import BeautifulSoup
from rake_nltk import Rake

keyword = "trump"
clean = lambda s: str(re.sub('[\W_]+', ' ', s))

def getText(articleUrl):
  text = ""
  try:
    html = urllib2.urlopen(articleUrl).read()
    soup = BeautifulSoup(html)
    article = soup.body.findAll('article')
    text = ' '.join([(s.text) for s in article[0].findAll('p')])
  except:
    print "failure"
  return text

r = Rake()
file = open("wapo_url_file.txt", "r")
output = open("wapo_text_file.txt", "w")
count = 0
while count < 500:
  for url in file:
    text = getText(url)
    r.extract_keywords_from_text(text)
    phrases = r.get_ranked_phrases()
    keyword_bool = False
    for phrase in phrases[:10]:
      if keyword in phrase:
        keyword_bool = True
    if keyword_bool:
      print "writing"
      print count
      output.write("\n" + "=========================" + "\n")
      output.write(str(count) + "...." + url)
      output.write("\n" + "=========================" + "\n")
      output.write(text.encode('utf-8'))
      count+=1
    print "==="
