import os
from pushbullet import Pushbullet
from flask import Flask, request, jsonify

app = Flask(__name__)
pb = Pushbullet('oYHlSULc3i998hvbuVtsjlH0ps23l7y2')

@app.route('/')
def hello():
    return 'python/flask'

@app.route('/send', methods=['POST'])
def send():
    return jsonify(**pb.push_note(request.form['title'],request.form['message']))
    #return 'done!'

if __name__ == "__main__":
    app.run(debug=True)
