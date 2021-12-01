from flask import Flask, request, jsonify
import requests

class Api:
    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)