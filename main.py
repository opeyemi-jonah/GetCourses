import re
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/greeting/<name>')
def greet(name):
    return jsonify(greeting=f'Hello, {name}!')

@app.route('/extract-text', methods=['POST'])
def extract_text():
    data = request.json
    text = data.get('text', '')
    
    # Regex to extract text between "TITLE" and "Course Credits"
    pattern = re.compile(r'TITLE\s+(.+?)\s+Course Credits')
    match = pattern.search(text)

    if match:
        extracted_text = match.group(1).strip()
        print("THIS IS THE EXTRACTED TEXT: ",extracted_text)
        return jsonify({"extracted_text": extracted_text}), 200
    else:
        print("ERROR!!!")
        return jsonify({"error": "No match found"}), 404


if __name__ == '__main__':
    app.run(debug=True)

