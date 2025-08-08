from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    This function handles requests to the root URL and returns a "Hello, World!" message.
    """
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
