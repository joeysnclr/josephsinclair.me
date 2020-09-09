from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import os
import github

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))


@app.route('/')
def index():
    repos = github.getReposCount()
    stars = github.getStarCount()
    contributions = github.getContributionsCount()
    return render_template('index.html', repos=repos, stars=stars, contributions=contributions)


app.run(host='0.0.0.0', port=port, debug=True)
