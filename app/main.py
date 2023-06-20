from flask import Flask, jsonify

# Import app code
app = Flask(__name__)

# After creating the app, so that cors can import it
import cors
from flask_cors import cross_origin

@app.route("/api/")
@cross_origin
def root():
    return jsonify({"message": "Hello World"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)