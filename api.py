from flask import Flask
from flask import jsonify
from flask import request
from util import MODEL_NAME

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
    # Get JSON
    req_data = request.get_json()

    # Extract data from JSON
    question_text = req_data['question_text']
    question_type = req_data['question_type']
    answer_choices = req_data['answer_choices']
    answer_type = req_data['answer_type']

    # Get relevant URLs from Google Search
    num_urls = 3
    urls = get_urls(question_text, num_urls)

    # Get context by parsing content of URLs
    context = get_urls_context(urls)

    # Setup model for QA
    dir_ans_model = AutoModelForQuestionAnswering.from_pretrained(MODEL_NAME)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    # Get Answer
    answer = find_answer(dir_ans_model, tokenizer, question_text, question_type, answer_choices, answer_type, context)

    # ! Debug
    print(question_text, '---', answer)

    # Return successful request status
    return jsonify({'answer': answer}), 200


def run():
    app.run(host='0.0.0.0', port=5000)

