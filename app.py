from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world2():
    return "Hello, Flask! tt 24.1117"

if __name__ == '__main__':
    app.run(debug=True)