from flask import Flask
from flask import jsonify
from flask import request
from q_url_getter import get_question_url
from wiki_scraper import get_wiki_content
from processer import process

app = Flask(__name__)


@app.route('/sanity', methods=['GET'])
def sanity_check():
    return '', 200


@app.route('/question', methods=['POST'])
def ask_me():
    req_data = request.get_json()
    question = req_data['question_text']
    url = get_question_url(question)
    print(url)
    content = get_wiki_content(url)
    answer = process(question, content)

    # TODO
    return jsonify({'answer': answer}), 200


def run():
    app.run(host='0.0.0.0', port=5000)

