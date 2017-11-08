from __future__ import print_function
from flask import Flask, request

app = Flask(__name__)

# Change ngrok listening port accordingly
#    ./ngrok http 4567


@app.route("/payload", methods=['POST'])
def payload():
    print('I got some JSON: {}'.format(request.json))
    return 'ok'
