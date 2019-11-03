from flask import Flask, request
import database as db

app = Flask(__name__)

@app.route('/write-data', methods=['POST'])
def write_data():
    db.insert_row(db.DEFAULT_PATH, request.get_json())
    return 'Success!'

@app.route('/read-data', methods=['POST'])
def read_data():
    print(list(request.args))
    return 'Hello World!'

@app.route('/parse-image', methods=['POST'])
def parse_image():
    print(list(request.files))
    print(request.files['pic'])
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
