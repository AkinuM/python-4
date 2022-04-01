import re

def split_words(text):
    words = re.split(r"(?:(?:[^a-zA-Z]+')|(?:'[^a-zA-Z]+))|(?:[^a-zA-Z']+)", text)
    return [word for word in words if len(word) != 0]

def split_sentences(text):
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)
    return [sentence for sentence in sentences if len(sentence) != 0]

def word_n_gram(word, n):
    n_grams = []
    if len(word) < n: 
        return n_grams
    else: 
        for counter in range(len(word) - n + 1):
            n_grams.append(word[counter: counter + n])
    return n_grams

def count_words(words):
    dict_words = {}
    for word in words:
        count = dict_words.get(word, 0)
        dict_words[word] = count + 1
    return dict_words