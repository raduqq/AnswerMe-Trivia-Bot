import difflib
import random
import re

from transformers import pipeline
from util import text2int


def find_answer(dir_ans_model, tokenizer, question_text, question_type, answer_choices, answer_type, context):
    tokenizer.encode(question_text, truncation=True, padding=True)
    nlp = pipeline('question-answering', model=dir_ans_model, tokenizer=tokenizer)

    answer = nlp({'question': question_text, 'context': context})['answer']

    curr_answer = answer

    if answer_type == 'numeric':
        if answer[0].isalpha():
            curr_answer = text2int(answer)
        else:
            answer = re.sub('[^0-9]', '', answer)
            curr_answer = int(answer)

    if question_type == 'multiple_choice':
        curr_answer = str(curr_answer)
        curr_poss_answers = curr_answer.split(' ')

        for poss_answer in curr_poss_answers:
            if poss_answer in answer_choices:
                return poss_answer

        final_choices = difflib.get_close_matches(curr_answer, answer_choices)

        if len(final_choices) == 0:
            print("!!!!!!!!!!!! RANDOM FINAL CHOICE !!!!!!!!!!!!!!!!")
            final_choice = random.choice(answer_choices)
        else:
            final_choice = final_choices[0]

        return final_choice

    return curr_answer

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
