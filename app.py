from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_talisman import Talisman
import os

app = Flask(__name__)
Talisman(app)
port = int(os.environ.get('PORT', 5000))


@app.route('/')
def index():
    return render_template('index.html')


app.run(host='0.0.0.0', port=port, debug=True)
