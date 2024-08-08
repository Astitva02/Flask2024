from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi World!'
def input():
    a = input("my name is:")
    return ("answer",a)

if __name__== "__main__" :
    app.run(debug=True)

