from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_route():
    return 'Hello, Traveller!'