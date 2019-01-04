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


def start_health_endpoint(port):
    app.run(host='0.0.0.0', port=port)


def run(options):
    t = Thread(target=start_health_endpoint(options.port), daemon=True)
    t.start()
