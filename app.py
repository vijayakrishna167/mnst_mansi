from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return "Notes App Running Inside Docker!"

@app.route('/note', methods=['POST'])
def add_note():
    data = request.json
    notes.append(data['note'])
    return jsonify({"message": "Note added"})

@app.route('/notes')
def get_notes():
    return jsonify(notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)