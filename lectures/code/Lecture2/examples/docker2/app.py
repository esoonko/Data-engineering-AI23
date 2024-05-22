from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

"""
@app.route('/new_functionality')
def new_functionality():
    # Your code for the new functionality goes here
    return "This is the new functionality!"
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)