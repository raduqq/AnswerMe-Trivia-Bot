import spacy


def process(question, content):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(content)
    print([(X.text, X.label_) for X in doc.ents])

    return question
