from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    message = "Hello Clarusway"
    return render_template("index.html", num1=34, num2=45, greeting = message, greet_size=3)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)