# coding=utf-8

from flask import Flask, session, jsonify, request, Blueprint, render_template
from connect.conn import conn

index_page = Blueprint('index_page', __name__, template_folder="templates")
db = conn()


@index_page.route('/')
def hello_world():
    return render_template("login.html")


@index_page.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        type = request.form.get("type")
        user = db.the_one.find_one({"name": str(name)})
        if user:
            pass
        else:
            return jsonify({"loginstatus": "600"})
        user1 = db.the_one.find_one({"name": name, "password": password})
        if user1:
            session["id"] = str(user1["_id"])
            session['name'] = str(user1["name"])
            session["type"] = type
            return jsonify({"loginstatus": "200", "name": name, "password": password})
        else:
            return jsonify({"loginstatus": "700"})


@index_page.route('/index', methods=['POST', 'GET'])
def index1():
    if session.has_key("id"):
        pass
    else:
        render_template('login.html')
    name = session["name"]
    return render_template('index.html', name=name)
