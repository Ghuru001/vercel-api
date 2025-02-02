from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load the marks data
with open('q-vercel-python.json') as f:
    data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [data.get(name, None) for name in names]
    return jsonify({"marks": marks})

app = app
