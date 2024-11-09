from flask import Flask

app = Flask(__name__)

# Mock database query
def get_hello_message():
    return "Hello from Flask App!"

@app.route('/api/hello', methods=['GET'])
def hello():
    message = get_hello_message()
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
