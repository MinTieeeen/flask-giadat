from flask import Flask, send_from_directory, render_template, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder='.')
# Cấu hình CORS để cho phép truy cập từ mọi nguồn
CORS(app, resources={r"/*": {"origins": "*"}})

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
    try:
        return send_from_directory('data', filename)
    except:
        # Nếu không tìm thấy file, trả về lỗi 404
        return jsonify({"error": f"File {filename} not found"}), 404

# Thêm route đặc biệt cho dữ liệu giá đất
@app.route('/api/land-prices/current')
def get_current_land_prices():
    try:
        with open('data/Bang_gia_dat.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/land-prices/state')
def get_state_land_prices():
    try:
        with open('data/Bang_gia_dat_Nha_nuoc.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add this to ensure all routes work properly with Render
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    # Render automatically assigns PORT env variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)