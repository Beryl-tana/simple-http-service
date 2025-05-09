from flask import Flask, jsonify, request
import logging
from datetime import datetime

app = Flask(__name__)

# Configure access log format
logging.basicConfig(
    filename='service.log',
    level=logging.INFO,
    format='%(message)s'
)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/health')
def health():
    return jsonify(status="ok"), 200

# Log all /health requests in standard format
@app.after_request
def log_request(response):
    if request.path == '/health':
        log_line = f'{request.remote_addr} - - [{datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")}] "GET {request.path} HTTP/1.1" {response.status_code}'
        app.logger.info(log_line)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

