from flask import Flask
from app import app
from app.models import user

@app.route('/users', methods=['GET'])
