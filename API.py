from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


@app.route('/sanity', methods=['GET'])
def sanity_check():
    return '', 200


@app.route('/question', methods=['POST'])
def ask_me():
    req_data = request.get_json()
    # print(req_data['name'])
    #TODO
    return jsonify({'answer': 'some answer'}), 200


if __name__ == '__main__':
    app.run()
