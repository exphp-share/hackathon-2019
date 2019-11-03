from flask import Flask, request
app = Flask(__name__)

@app.route('/write-data', methods=['POST'])
def write_data():
    return 'Hello World!'

@app.route('/read-data', methods=['POST'])
def read_data():
    return 'Hello World!'

@app.route('/parse-image', methods=['POST'])
def parse_image():
    print(list(request.files))
    print(request.files['pic'])
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
