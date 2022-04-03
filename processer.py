from transformers import pipeline
from scraper import get_url_context

def find_answer(model, tokenizer, question, context):
    # max_score = 0.0
    # best_answer = ''

    tokenizer.encode(question, truncation=True, padding=True)
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

    answer = nlp({'question': question, 'context': context})['answer']
    return answer

    # for url in urls:
    #     context = get_url_context(url)
    #
    #     answer_data = nlp({ 'question': question, 'context': context })
    #     answer = answer_data['answer']
    #     score = answer_data['score']
    #
    #     print(score, answer)
    #
    #     if score > max_score:
    #         max_score = score
    #         best_answer = answer
    #
    # return best_answer
