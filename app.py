from flask import Flask
from flask import request   

app = Flask(__name__)

@app.route("/")
def hello_world():
    REMOTE_ADDR = request.environ.get('REMOTE_ADDR', request.remote_addr) 
    HTTP_X_REAL_IP = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) 
    HTTP_X_FORWARDED_FOR = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr) 
    return f"REMOTE_ADDR: {REMOTE_ADDR}, HTTP_X_REAL_IP: {HTTP_X_REAL_IP}, HTTP_X_FORWARDED_FOR: {HTTP_X_FORWARDED_FOR}"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
