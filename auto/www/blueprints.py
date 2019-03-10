# -*- coding: utf-8 -*-
from functools import wraps
from flask import  logging
__author__ = "苦叶子"

"""

公众号: 开源优测

Email: lymking@foxmail.com

"""
from flask import Blueprint, render_template, session, redirect, url_for, current_app, send_file, request
from flask_login import login_required
from utils.file import get_splitext, exists_path
from utils.tools import run_log_decorate,Tools

routes = Blueprint('routes', __name__)

@run_log_decorate
@routes.before_request
def before_routes():
    Tools.runLogHander.debug(session)
    if 'username' in session:
        pass
    else:
        pass
        # return redirect(url_for('routes.index'))

@run_log_decorate
@routes.route('/index')
@routes.route('/')
def index():
    Tools.runLogHander.debug("登陆页面")
    print("登陆页面")
    return render_template('login.html')

@run_log_decorate
@routes.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return render_template('login.html')

@run_log_decorate
@routes.route('/tree_demo')
def tree_demo():
    return render_template('tree_data1.json')

@run_log_decorate
@routes.route("/editor/<project>/<suite>/<case>")
def editor(project, suite, case):
    t = get_splitext(case)

    default = "default.html"
    if t[1] in (".txt", ".robot", ".py", ".js"):
        default = "editor.html"
    elif t[1] in (".bmp", ".jpg", ".jpeg", ".png", ".gif"):
        default = "view_img.html"

    return render_template(default, project=project, suite=suite, case=case)

@run_log_decorate
@routes.route("/task_list/<name>")
def task_list(name):

    return render_template('task_list.html', project=name)

@run_log_decorate
@routes.route("/scheduler/")
def scheduler():
    return render_template('scheduler.html')

@run_log_decorate
@routes.route("/user/")
def user():
    return render_template('user.html')

@run_log_decorate
@routes.route("/view_report/<project>/<task>")
def view_report(project, task):
    app = current_app._get_current_object()

    job_path = app.config["AUTO_HOME"] + "/jobs/%s/%s/%s/log.html" % (session['username'], project, task)

    return send_file(job_path)

@run_log_decorate
@routes.route("/q_view_report/<username>/<project>/<task>")
def q_view_report(username, project, task):
    app = current_app._get_current_object()

    job_path = app.config["AUTO_HOME"] + "/jobs/%s/%s/%s/log.html" % (username, project, task)

    return send_file(job_path)

@run_log_decorate
@routes.route("/view_img")
def view_img():
    args = request.args.to_dict()
    app = current_app._get_current_object()
    img_path = app.config["AUTO_HOME"] + "/workspace/%s" % session['username'] + args["path"]
    img_path.replace("\\", "/")
    if exists_path(img_path):
        return send_file(img_path)

    return False

@run_log_decorate
@routes.route("/welcome")
def welcome():

    return render_template("welcome.html")

