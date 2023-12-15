from bottle import route, post, run, template, redirect, request
import database

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    items = database.get_pat()
    return template("list.tpl", health_analysis=items)

@route("/add")
def get_add():
    return template("add_pat.tpl")

@post("/add")
def post_add():
    description = request.forms.get("description")
    print("description = ", [description])
    database.add_pat(description)
    redirect("/list")    

@route("/update/<id>")
def get_update(id):
    items = database.get_pat(id)
    return template("update_pat.tpl", item=items[0])

@post("/update")
def post_update():
    description = request.forms.get("description")
    id = request.forms.get("id")
    print("/update",[id,description])
    database.update_pat(id, description)
    redirect("/list")    

@route("/delete/<id>")
def get_delete(id):
    database.delete_pat(id)
    redirect("/list")


run(host='localhost', port=8080)