from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from DevOps Project!',
        'status': 'running'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy'
    })

@app.route('/metrics')
def metrics():
    return jsonify({
        'app': 'devops-project',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)