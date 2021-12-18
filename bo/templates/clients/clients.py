from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from bo.models import *
from bo.templates.clients.clients_process import *


client = Blueprint("client", __name__)


@client.route("/", methods=['GET','POST'])
def clientlist():
    if request.method == "POST":
        all = request.form.to_dict()
        client_add(**all)
    clientresults = db.session.query(Clients).all()
    states = db.session.query(States).all()
    cities = db.session.query(Clients.city).order_by(Clients.city).distinct()
    context = {"user": User, "clients": clientresults, 'states':states,
               'cities':cities}
    return render_template("clients/clients.html", **context)

@client.route('/editclient/<id>', methods=['GET','POST'])
def clientedit(id):
    if request.method == "POST":
        all = request.form.to_dict()
        print (all)
        client_edit(id, **all)
        return redirect(url_for('client.clientlist'))
    clients = db.session.query(Clients).filter_by(id=id).all()
    states = db.session.query(States).all()
    cities = db.session.query(Clients.city).distinct(Clients.city).order_by(Clients.city).all()
    context = {"user": User, 'states':states, 'clients':clients,
               'cities':cities}
    return render_template('clients/clients_edit.html', **context)

@client.route("/deleteclient/<id>")
def clientdelete(id):
    client_delete(id)
    return redirect(request.referrer)
