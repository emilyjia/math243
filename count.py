# number of occurrences of ROOT
# number of occurrences of SBAR, POS, double JJ
import fnmatch

metrics = ["ROOT", "(S", "SBAR", "SBARQ", "SINV", "SQ", "ADJP"] + \
  ["ADVP", "CONJP", "FRAG", "INTJ", "LST", "NAC"] + \
  ["NP", "NX", "PP", "PRN", "PRT", "QP", "RRC", "UCP", "VP"] + \
  ["WHADJ", "WHAVP", "WHNP", "WHPP"]

words = ["JJ", "JJR", "JJS", "RB", "RBR", "RBS", "UH"]

def main():
  # file_name = raw_input("File with trees: ")
  # for metric in metrics:
  #   with open(file_name, 'r') as f:
  #     print(sum(line.count(metric) for line in f))
  # for word in words:
  #   with open(file_name, 'r') as f:
  #      print(sum(line.count(word) for line in f))
  # with open(file_name, 'r') as f:
  #   x = sum(1 if (line.count("JJ") > 2) else 0 for line in f)
  #   print x
  file_name = raw_input("File with trees: ")
  with open(file_name, 'r') as f:
    print(sum(line.count("(S ") for line in f))

if __name__ == "__main__":
    main()
