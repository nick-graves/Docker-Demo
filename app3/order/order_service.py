from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/orders")
def get_orders():
    users = requests.get("http://user-service:5001/users").json()
    return jsonify(orders=[{"user": user, "order": "Laptop"} for user in users["users"]])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)