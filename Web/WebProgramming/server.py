from functools import wraps
from flask import Flask, url_for, request, render_template, Response

#method to carry out the authentication
app = Flask(__name__)

@app.route("/")
def sign_in():
    pass

@app.route("/addasset", methods=["GET","POST"])
def add_asset():
    pass

@app.route("/addusers")
def add_users():
    pass

@app.route("/assignasset")
def assign_asset():
    pass

@app.route("/unassignasset")
def unassign_asset():
    pass

@app.route("/viewassigned")
def view_assigned():
    pass

@app.route("/repportlost")
def report_lost():
    pass

@app.route("/reportfound")
def report_found():
    pass