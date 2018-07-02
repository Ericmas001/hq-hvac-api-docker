#!/usr/bin/python

import logging 
from logging.handlers import RotatingFileHandler
from threading import Lock
from datetime import datetime, time
from flask import Flask, request, jsonify
from flask.json import JSONEncoder
import handler

from const import KEY

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, time):
            return obj.isoformat()
        
        return obj.__dict__

class MyFlask(Flask):
    def make_response(self, rv):
        if hasattr(rv, 'response') and rv.response is None:
            return super(MyFlask, self).make_response(rv)
        if hasattr(rv, 'new_url') and rv.new_url is not None:
            return super(MyFlask, self).make_response(rv)
        return super(MyFlask, self).make_response(jsonify(rv))

app = MyFlask(__name__)
app.json_encoder = CustomJSONEncoder
lock = Lock()
@app.route('/' + KEY + '/', methods=['GET'])
def index():
    with lock:
    	return handler.get_index(app)

@app.route('/config/' + KEY + '/', methods=['GET'])
def list_config():
    with lock:
        return handler.list_config(app)

@app.route('/hvac/off/' + KEY + '/', methods=['GET'])
def power_off():
    with lock:
        return handler.power_off(app)

@app.route('/hvac/on/' + KEY + '/', methods=['GET'])
def power_on():
    with lock:
        return handler.send_last_command(app)

@app.route('/hvac/on/' + KEY + '/', methods=['POST'])
def send_command():
    with lock:
        return handler.send_command(app, request.json)

@app.route('/last/command/' + KEY + '/', methods=['GET'])
def last_command():
    with lock:
        return handler.last_command(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=42099)