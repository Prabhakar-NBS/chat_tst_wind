import nltk
import numpy as np
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
def stem(word):
    return stemmer.stem(word.lower())
def bag_of_words(tokenized_sentence,all_words):
    """
    return bag of words array: 0 or 1 for each word in the bag that exists in the tokenized_sentence
    :param tokenized_sentence: a list of words
    :param all_words: a list of all words in the language
    :return: bag of words array
    """
    # stem each word
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    # initialize bag with 0 for each word
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag.tolist() if any(bag) else []