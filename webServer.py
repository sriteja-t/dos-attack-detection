from flask import Flask,jsonify
import time
app = Flask(__name__)

@app.route('/')
def home():
    return """<a href='/home'>/home</a>
              <br>
              <a href='/name'>/name</a>
              <br>
              <a href='/age'>/age</a>"""

@app.route('/home')
def index():
    time.sleep(5)
    return "Welcome, The server is up and running!"

@app.route('/name')
def name():
    return jsonify(name='tst')

@app.route('/age')
def age():
    return jsonify(age='19')

if __name__ == '__main__':
    app.run(host='0.0.0.0')