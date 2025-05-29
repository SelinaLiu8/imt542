from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from scraper import extract_defined_terms_from_paragraph

app = Flask(__name__)

CORS(app, origins=["https://selinaliu8.github.io"])

INPUT_FILE = "input.txt"

@app.route('/input', methods=['PUT'])
def put_input_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" in request body'}), 400

    with open(INPUT_FILE, 'w') as f:
        f.write(data['text'])

    return jsonify({'message': 'Text saved successfully.'}), 200


@app.route('/definitions', methods=['GET'])
def get_definitions():
    try:
        with open(INPUT_FILE, 'r') as f:
            paragraph = f.read()
    except FileNotFoundError:
        return jsonify({'error': 'Input file not found. Use PUT /input first.'}), 404

    results = extract_defined_terms_from_paragraph(paragraph)
    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
