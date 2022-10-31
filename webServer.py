from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def hi():
    return """<a href='/home'>/home</a>
              <br>
              <a href='/name'>/name</a>
              <br>
              <a href='/age'>/age</a>"""

@app.route('/home')
def index():
    return "Welcome, The server is up and running!"

@app.route('/name')
def jsony():
    return jsonify(name='tst')

@app.route('/age')
def test():
    return jsonify(age='19')

if __name__ == '__main__':
    app.run()