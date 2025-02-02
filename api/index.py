from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Load the marks data
with open('q-vercel-python.json') as f:
    data = json.load(f)

# Create a dictionary for quick lookup
marks_dict = {student['name']: student['marks'] for student in data}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    result = [marks_dict.get(name, None) for name in names]
    return jsonify({"marks": result})

if __name__ == '__main__':
    app.run(debug=True)
