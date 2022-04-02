import nltk
from string import punctuation
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
import spacy
import nltk.data

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

    lancaster = LancasterStemmer()
    lancasted_words = [lancaster.stem(word) for word in filtered_list]

    lemmatizer = WordNetLemmatizer()

    lemmatized_words = [lemmatizer.lemmatize(word) for word in lancasted_words]

    return lemmatized_words

#
# def filter_sentences(ess_question, ess_sentences):
#     potential_sentences = []
#
#     for sentence in ess_sentences:
#         found = False
#
#         # count how many times the words in the question appear in the sentence
#         for s_word in sentence:
#             for q_word in ess_question:
#                 if s_word.lower() == q_word.lower():
#                     potential_sentences.append(sentence)
#                     found = True
#                     break
#             if found:
#                 break
#
#     # if at least one word from the question appears in the sentence, add sentence
#     # to potential sentences list
#
#     return potential_sentences


def tag_sentences(sentences, nlp):
    final_sentences = []

    for sentence in sentences:
        # tag words in sentence
        doc = nlp(sentence)
        essential_sentence = get_essential_words(sentence)
        print(essential_sentence, [(X.text, X.label_) for X in doc.ents])
        final_sentences.append((essential_sentence, [(X.text, X.label_) for X in doc.ents]))

    return final_sentences


def essentialize_sentences(sentences):
    ess_sentences = []

    # essentialize each and every sentence
    for token in sentences:
        ess_sentences.append(get_essential_words(token))

    return ess_sentences


def process_content(ess_question, content, nlp, tags):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    original_sentences = tokenizer.tokenize(content)

    # essentialize sentences
    ess_sentences = essentialize_sentences(original_sentences)

    # filter
    # filtered_sentences = filter_sentences(ess_question, ess_sentences)

    # assgin tags
    pair_sentences = tag_sentences(original_sentences, nlp)

    filter_pair_sentences = []
    for pair_sentence in pair_sentences:
        possible_answers = []
        sentence = pair_sentence[0]
        tagged_sentence = pair_sentence[1]

        for pair in tagged_sentence:
            if pair[1] in tags:
                possible_answers.append(pair[0])

        if len(possible_answers) > 0:
            filter_pair_sentences.append((sentence, possible_answers))

    # propozitia filtrata + posibile raspunsuri
    return filter_pair_sentences


def compute_scores(pair_sentences, ess_question):
    scores = []
    max_score = 0

    for pair_sentence in pair_sentences:
        sentence = pair_sentence[0]

        score = 0
        for word in ess_question:
            if word in sentence:
                score += 1

        max_score = max(max_score, score)
        scores.append(score)

    return max_score, scores


def get_best_sentences(max_score, scores, pair_sentences):
    final_pair_sentences = []

    for i in range(len(scores)):
        if scores[i] == max_score:
            final_pair_sentences.append(pair_sentences[i])

    return final_pair_sentences


def get_best_answer(best_pair_sentences, ess_question):
    freq = {}

    for best_pair_sentence in best_pair_sentences:
        possible_answers = best_pair_sentence[1]

        for possible_answer in possible_answers:
            if possible_answer not in ess_question:
                if possible_answer not in freq.keys():
                    freq[possible_answer] = 0
                freq[possible_answer] += 1

    final_answer = ""
    final_freq = 0
    for possible_answer in freq.keys():
        if freq[possible_answer] > final_freq:
            final_freq = freq[possible_answer]
            final_answer = possible_answer

    return final_answer


def process(question, content):
    first_word = question.split()[0]
    tags = []

    if first_word.lower() == 'who':
        tags = ['PERSON', 'ORG']
    elif first_word.lower() == 'where':
        tags = ['GPE', 'LOC']
    elif first_word.lower() == 'when':
        tags = ['DATE']
    elif first_word.lower() == 'what' or first_word.lower() == 'which':
        # TODO
        tags = ['PERSON', 'NORP', 'FACILITY', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART', 'LAW', 'LANGUAGE',
                'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL']

    # en_core_web_sm
    nlp = spacy.load("en_core_web_lg")

    # get ess_question
    ess_question = get_essential_words(question)
    print(ess_question)

    # get ess_content
    processed_content = process_content(ess_question, content, nlp, tags)

    max_score, scores = compute_scores(processed_content, ess_question)
    best_sentences = get_best_sentences(max_score, scores, processed_content)

    for best in best_sentences:
        print(best)

    final_answer = get_best_answer(best_sentences, question)

    return final_answer
