import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

from bson.objectid import ObjectId # Necessary to the edit_task function

if os.path.exists("env.py"):
    import env

# create instance of flask and assign it to "app"
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("connection_string") # Variabile situata in env.py/inserita nei setting di heroku

coll = PyMongo(app).db.myFirstDB # Variabile contenente l'unica collezione del database

# Order the collection in a list
coll_list = []
for dict in coll.find():
    for key, value in dict.items():
        if key != "_id":
            coll_list.append(key + " : " + str(value))

# landing page
@app.route('/') 
@app.route('/first_function')
def first_function():
    return render_template("index.html", output = coll_list)

if __name__ == '__main__':  
    app.run(host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", "5000")), debug=True) # Remove dubug=True before publishing



