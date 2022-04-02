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

    #TODO
    return jsonify({'answer': 'some answer'}), 200

def run():
    app.run()
