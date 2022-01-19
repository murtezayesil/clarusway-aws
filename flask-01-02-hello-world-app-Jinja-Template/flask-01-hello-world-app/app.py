from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world!"

@app.route('/second')
def second():
    return "This is the second page"

@app.route('/dyn/<string:id>')
def dyn(id):
    return f"This page's ID is {id}"

if __name__=="__main__" :
    app.run(debug=True)