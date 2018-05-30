import nltk
import collections
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def yule():
  file_name = raw_input("File with text: ")
  file_content = open(file_name).read()
  k_file_name = raw_input("K file name: ")
  k_file = open(k_file_name, "w")
  tokens = nltk.word_tokenize(file_content.decode('utf-8'))
  #split tokens into token_list
  article_lst = []
  curr_article = []
  article = True
  for i in range(len(tokens)):
    word = tokens[i]
    if "=" in word:
      article = not article
      if len(curr_article) > 0:
        article_lst.append(curr_article)
        curr_article = []
    if article:
      if word.isalpha():
        curr_article.append(word)
  for article in article_lst:
    token_counter = collections.Counter(word.upper() for word in article)
    m1 = sum(token_counter.values())
    m2 = sum([freq ** 2 for freq in token_counter.values()])
    k = 10000.0 * ((m2-m1)*1.0/(m1*m1) * 1.0)
    k_file.write(str(k))
    k_file.write("\n")

def plot():
  nyt = np.loadtxt('nyt_k_file.txt')
  # nyt_weights = np.ones_like(nyt)/float(len(nyt))
  fox = np.loadtxt('fox_k_file.txt')
  # fox_weights = np.ones_like(fox)/float(len(fox))
  ap = np.loadtxt('ap_k_file.txt')
  # ap_weights = np.ones_like(ap)/float(len(ap))
  breitbart = np.loadtxt('breitbart_k_file.txt')
  # breitbart_weights = np.ones_like(breitbart)/float(len(breitbart))
  plt.hist(nyt, bins = 'auto', label = 'nyt', alpha = 0.2)
  plt.hist(fox, bins = 'auto', label = 'fox', alpha = 0.2)
  plt.hist(ap, bins = 'auto', label = 'ap', alpha = 0.2)
  plt.hist(breitbart, bins = 'auto', label = 'breitbart', alpha = 0.2)
  plt.legend(loc='upper right')
  plt.show()

if __name__ == "__main__":
    yule()
