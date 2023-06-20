from flask import Flask, jsonify

# Import app code
app = Flask(__name__)


@app.route("/api/")
def root():
    return jsonify({"message": "Hello World"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)