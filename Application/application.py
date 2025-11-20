from flask import Flask, jsonify
import platform
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from Elastic Beanstalk!',
        'instance_id': 'demo-instance',
        'timestamp': str(datetime.datetime.now()),
        'status': 'healthy'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': str(datetime.datetime.now())})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)