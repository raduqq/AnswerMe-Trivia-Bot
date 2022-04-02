import spacy

import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from string import punctuation


def get_essential_words(worf_quote):
    worf_quote = worf_quote.translate(str.maketrans('', '', punctuation))
    words_in_quote = word_tokenize(worf_quote)

    stop_words = set(stopwords.words("english"))
    filtered_list = []

    for word in words_in_quote:
        if word.casefold() not in stop_words:
            filtered_list.append(word)

    lemmatizer = WordNetLemmatizer()

    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_list]

    return lemmatized_words


def process(question, content):
    first_word = question.split()[0]

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(content)
    # print([(X.text, X.label_) for X in doc.ents])


    return get_essential_words(content)

    # return question
