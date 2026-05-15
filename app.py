from flask import Flask  # was 'rom' - typo 1
app = Flask(__name__)

@app.route("/")
def hello():  # was 'def hello():f' - typo 2, extra 'f'
    return "Hello, Jenkins CI/CD from Flask App on Windows!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)