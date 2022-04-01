import re
import statistics

def split_words(text):
    words = re.split(r"(?:(?:[^a-zA-Z]+')|(?:'[^a-zA-Z]+))|(?:[^a-zA-Z']+)", text)

    return [word for word in words if len(word) != 0]

def split_sentences(text):
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)

    return [sentence for sentence in sentences if len(sentence) != 0]

def get_word_n_gram(word, n):
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

def print_top_n_grams(words, n, k):
    n_grams = []
    for word in words:
        n_grams.append(get_word_n_gram(word, n))
    new_n_grams = []
    for n_gram in n_grams:
        new_n_grams += n_gram
    count_n_grams = count_words(new_n_grams)
    count_n_grams = {key: count_n_grams[key] for key in sorted(count_n_grams, key=count_n_grams.get, reverse=True)}
    i = 0
    print(f"TOP {k} n-grams: ")
    for n_gram in count_n_grams:
        if i < k:
            print (n_gram, count_n_grams[n_gram])
            i += 1
        else:
            break

def solve(text, n, k):
    words = split_words(text) 
    dict_words = count_words(words)
    print("Number of repetitions of words: ")
    for word in dict_words:
        print (word, dict_words[word])

    sentences = split_sentences(text)
    word_count = []
    for sentence in sentences:
        word_count.append(len(split_words(sentence)))
    mean = statistics.mean(word_count)  
    print (f"Arithmetic mean: {mean}")
    median = statistics.median(word_count)
    print (f"Median: {median}")
    
    print_top_n_grams(words, n, k)