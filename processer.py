import difflib
import random
import re

from transformers import pipeline
from util import text2int


def find_answer(dir_ans_model, tokenizer, question_text, question_type, answer_choices, answer_type, context):
    # Setup NLP pipeline
    tokenizer.encode(question_text, truncation=True, padding=True)
    nlp = pipeline('question-answering', model=dir_ans_model, tokenizer=tokenizer)

    # Get answer through pipeline
    answer = nlp({'question': question_text, 'context': context})['answer']

    # Invaluire
    curr_answer = answer

    if answer_type == 'numeric':
        if answer[0].isalpha():
            # If answer is a number written in letters ("eight" i.o. "8"), convert it to a letter
            curr_answer = text2int(answer)
        else:
            # If answer is a number written in... numbers, keep only the numbers (strip %, +, etc.)
            answer = re.sub('[^0-9]', '', answer)
            curr_answer = int(answer)

    # If question is multiple choice, do some extra meddling
    if question_type == 'multiple_choice':
        curr_answer = str(curr_answer)
        curr_poss_answers = curr_answer.split(' ')

        # If answer is made up of multiple words, and one of these words is in the grile, return said grila
        for poss_answer in curr_poss_answers:
            if poss_answer in answer_choices:
                return poss_answer

        # Find closest match between answer and the grile
        final_choices = difflib.get_close_matches(curr_answer, answer_choices)

        if len(final_choices) == 0:
            # If we found no match between our algorithm's answer and the grile, pick any grila as random.
            final_choice = random.choice(answer_choices)
        else:
            # Else, extract answer from answer "struct"
            final_choice = final_choices[0]

        # Return multiple choice answer
        return final_choice

    # Return direct answer answer
    return curr_answer
