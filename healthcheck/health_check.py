from threading import Thread
from flask import Flask, jsonify

app = Flask(__name__)
Healthy = True


@app.route('/healthz')
def is_healthy():
    if Healthy:
        return jsonify({'status': 'OK'})
    else:
        return jsonify({'status': 'UNHEALTHY'}), 503


def start_health_endpoint():
    app.run(host='0.0.0.0', port=5000)


def run():
    t = Thread(target=start_health_endpoint, daemon=True)
    t.start()
