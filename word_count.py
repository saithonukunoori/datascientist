import pandas as pd
import string


def remove_punc(str1) :
    str2=str1.translate(str.maketrans("", "", string.punctuation))
    # the other way
    # res = re.sub(r'[^\w\s]', '', paragraph) using regex
    return str2

def word_split(str2) :
    l1 = str2.split()
    return l1

def word_dict(L1) :
    d1 = {}
    for word in L1:
      if word in d1:
          d1[word] += 1
      else:
          d1[word] = 1
    return d1

def word_freq_table(d1) :
    df = pd.DataFrame(list(d1.items()), columns=["word", "No of occurrences"])
    return df


