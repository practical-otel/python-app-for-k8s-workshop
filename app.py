from flask import Flask

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