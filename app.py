from flask import Flask, jsonify
import requests
import nosleep

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
    return "API is working fine -(TUX)"



@app.route("/<query>")
def main_(query):
    return jsonify(nosleep.main(query))

if __name__ == "_main_":
    app.debug = True
    app.run(host="0.0.0.0",port= 5000)