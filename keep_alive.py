from flask import Flask
from threading import Thread
import time
import requests

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return "Alive - Codespace is running!"

# Run Flask server in the background
def run():
    app.run(host='0.0.0.0', port=8080)

# Function to ping GitHub periodically to prevent timeout
def ping_github():
    while True:
        try:
            requests.get("https://github.com")
            print("Pinged GitHub successfully.")
        except Exception as e:
            print(f"Ping failed: {e}")
        time.sleep(300)  # Wait 5 minutes

def keep_alive():
    # Start the Flask server and GitHub ping in separate threads
    Thread(target=run, daemon=True).start()
    Thread(target=ping_github, daemon=True).start()

if __name__ == '__main__':
    keep_alive()
    print("Keep-alive server started!")
    while True:
        time.sleep(3600)  # Keep the script running indefinitely
