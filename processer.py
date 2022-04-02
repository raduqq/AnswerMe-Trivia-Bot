import spacy

# ! de primit de la Horia   
def essentialize():
    pass

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
        ess_sentences.append(essentialize(token))

    return ess_sentences

# TODO evaluate words in sentences according to tags given by question
def get_answer():
    pass

def process_content(ess_question, content, nlp):
    sentences = content.split('.')

    # essentialize sentences
    ess_sentences = essentialize_sentences(sentences)

    # filter 
    sentences = filter_sentences(ess_question, ess_sentences)

    # assgin tags
    tag_sentences(sentences, nlp)

    # get answer
    get_answer()


def process(question, content):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(content)
    
    # ! TESTING
    # print([(X.text, X.label_) for X in doc.ents])

    return question
