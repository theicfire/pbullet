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
    if request.form['phone_nickname']:
        bike = next(x for x in pb.devices if x.nickname == request.form['phone_nickname'])
        print 'special', bike
        return jsonify(**bike.push_note(request.form['title'], request.form['message']))
    return jsonify(**pb.push_note(request.form['title'],request.form['message']))

if __name__ == "__main__":
    app.run(debug=True)
