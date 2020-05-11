import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

from bson.objectid import ObjectId # Necessary to the edit_task function

if os.path.exists("env.py"):
    import env

# create instance of flask and assign it to "app"
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI") # Variabile ambientale importata con l'ambaradam, è importante sostituire <password> con password e cluster0 con il nome del database

only_collection = PyMongo(app).db.myFirstDB # Variabile contenente l'unica collezione del database

# Collezione convertita in lista (si può fare meglio)
collection_list = []
coll = only_collection.find()
for i in coll:
    collection_list.append(i)


# landing page
@app.route('/') 
@app.route('/first_function')
def first_function():
    return render_template("index.html", output = collection_list)

if __name__ == '__main__':  
    app.run(host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", "5000")), debug=True) # Rimuovere dubug=True prima di pubblicare


