from flask import Flask, send_from_directory, render_template
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/map')
def map_view():
    return send_from_directory('.', 'map.html')

@app.route('/login')
def login():
    return send_from_directory('.', 'login.html')

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

@app.route('/data/<path:filename>')
def serve_data(filename):
    return send_from_directory('data', filename)

# Add this to ensure all routes work properly with Render
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)