from flask import Flask
from flask import jsonify
from flask import request

from transformers import AutoModelForQuestionAnswering, AutoTokenizer

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
    question = req_data['question_text']

    num_urls = 3
    urls = get_urls(question, num_urls)
    # for url in urls:
    #     print(url)

    context = get_urls_context(urls)
    # print(context)

    model_name = 'deepset/roberta-base-squad2'

    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    answer = find_answer(model, tokenizer, question, context)
    return jsonify({'answer': answer}), 200


def run():
    app.run(host='0.0.0.0', port=5000)

