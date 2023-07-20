import word_count

paragraph = "Pandas allows us to analyze big data and make conclusions based on statistical theories. Pandas can clean messy data sets, and make them readable and relevant.Relevant data is very important in data science."
modified_para = word_count.remove_punc(paragraph)
list = word_count.word_split(modified_para)
dict = word_count.word_dict(list)
table = word_count.word_freq_table(dict)
print(table)
