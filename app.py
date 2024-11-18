from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world2():
    return "Hello, Flask! tt 24.1118 branch1 modified on github"

if __name__ == '__main__':
    app.run(debug=True)
