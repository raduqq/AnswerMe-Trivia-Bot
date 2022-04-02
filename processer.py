import nltk
from string import punctuation
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


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

def filter_sentences(ess_question, ess_sentences):
    potential_sentences = []

    for sentence in ess_sentences:
        cnt = 0

        # count how many times the words in the question appear in the sentence
        for s_word in sentence:
            for q_word in ess_question:
                if s_word == q_word:
                    cnt = cnt + 1
        
        # if at least one word from the question appears in the sentence, add sentence
        # to potential sentences list
        if cnt > 0:
            potential_sentences.append(sentence)

    return potential_sentences

def tag_sentences(sentences, nlp):
    tagged_sentences = []

    for sentence in sentences:
        # join separate words in a single sentence
        joined_sentence = ' '.join(sentence)
        # tag words in sentence
        tagged_sentences.apped(nlp(joined_sentence))

    return tagged_sentences

def essentialize_sentences(sentences):
    ess_sentences = []

    # essentialize each and every sentence
    for token in sentences:
        ess_sentences.append(get_essential_words(token))

    return ess_sentences

# TODO evaluate words in sentences according to tags given by question
def get_answer(ess_question, ess_content):
    pass

def process_content(ess_question, content, nlp):
    sentences = content.split('.')

    print(sentences)

    # essentialize sentences
    # ess_sentences = essentialize_sentences(sentences)

    # filter 
    # sentences = filter_sentences(ess_question, ess_sentences)

    # assgin tags
    # tag_sentences(sentences, nlp)


def process(question, content):
    first_word = question.split()[0]

    nlp = spacy.load("en_core_web_sm")

    # get ess_question
    ess_question = get_essential_words(question)
    # get ess_content
    ess_content = process_content(ess_question, content, nlp)

    # get answer
    answer = get_answer(ess_question, ess_content)

    return question
