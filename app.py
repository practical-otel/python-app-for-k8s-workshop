from flask import Flask
from opentelemetry.instrumentation.flask import FlaskInstrumentor

FlaskInstrumentor().instrument(enable_commenter=True, commenter_options={})

app = Flask(__name__)

def app_ready():
    # Code goes here to determine if your app is ready to start receiving traffic
    return True

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/livez', methods=['GET'])
def healthz_live():
    print('Liveness check ping')
    return 'ok\n'

@app.route('/readyz', methods=['GET'])
def healthz_ready():
    print('Readiness check ping')
    
    if app_ready():
        return 'ok\n'
    else:
        return 'not ready\n', 503

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
