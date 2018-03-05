# number of occurrences of ROOT
# number of occurrences of SBAR, POS, double JJ
import fnmatch

def main():
  file_name = raw_input("File with trees: ")
  with open(file_name, 'r') as f:
    print(sum(line.count("(ROOT") for line in f))
  with open(file_name, 'r') as f:
    print(sum(line.count("(SBAR") for line in f))
  with open(file_name, 'r') as f:
    print(sum(line.count("(POS") for line in f))
  with open(file_name, 'r') as f:
    print(sum(line.count("(JJ *) (JJ *))") for line in f))

if __name__ == "__main__":
    main()
