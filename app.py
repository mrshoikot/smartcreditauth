from verifier import verify
from flask import Flask
import serverless_wsgi

app = Flask(__name__)


@app.route('/')
def verifyCredentials():
    result = verify('mrshoikot@gmail.com', 'password')
    return str(result)

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

if __name__ == '__main__':
    app.run(host="0.0.0.0")