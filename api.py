from flask import Flask
from flask import jsonify
from flask import request

from transformers import AutoModelForQuestionAnswering, AutoModelForMultipleChoice, AutoTokenizer

from urls_getter import get_urls
from scraper import get_urls_context
from processer import find_answer

app = Flask(__name__)


@app.route('/sanity', methods=['GET'])
def sanity_check():
    return '', 200


@app.route('/question', methods=['POST'])
def ask_me():
    req_data = request.get_json()
    question_text = req_data['question_text']
    question_type = req_data['question_type']
    answer_choices = req_data['answer_choices']
    answer_type = req_data['answer_type']

    num_urls = 3
    urls = get_urls(question_text, num_urls)

    context = get_urls_context(urls)

    # ~18
    model_name = 'deepset/roberta-base-squad2'

    # ~14
    # model_name = 'deepset/bert-base-cased-squad2'

    # ~ ; fara truncation setat; foarte lent
    # model_name = 'deepset/bert-large-uncased-whole-word-masking-squad2'

    # ~18; dureaza prea mult
    # model_name = 'deepset/roberta-large-squad2'

    dir_ans_model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    # mult_ch_model = AutoModelForMultipleChoice.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    answer = find_answer(dir_ans_model, tokenizer, question_text, question_type, answer_choices, answer_type, context)

    print(question_text, '---', answer)

    return jsonify({'answer': answer}), 200


def run():
    app.run(host='0.0.0.0', port=5000)

