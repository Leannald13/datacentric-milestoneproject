
import os
import math
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'boxsetReviews'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@datacentriccluster-snqmw.mongodb.net/boxsetReviews?retryWrites=true&w=majority'

mongo = PyMongo(app)
    

@app.route('/')
def home_page():  
    return render_template("home.html", addboxset=mongo.db.addboxset.find())

@app.route('/add_boxset') 
def add_boxset():
    return render_template("addseries.html", addboxset=mongo.db.addboxset.find())

@app.route('/all_boxsets')
def all_boxsets():
    return render_template("allseries.html", addboxset=mongo.db.addboxset.find())


@app.route('/insert_boxset', methods=['POST'])
def insert_boxset():
    addboxset = mongo.db.addboxset
    boxset = {
        "boxset_image_url": request.form.get("boxset_image_url"),
        "boxset_title": request.form.get("boxset_title"),
        "boxset_seasons": request.form.get("boxset_seasons"),
        "boxset_starring": request.form.get("boxset_starring"),
        "boxset_rating": request.form.get("boxset_rating"),
        "boxset_summary": request.form.get("boxset_summary"),
    }
    addboxset.insert_one(boxset)  
    return redirect(url_for('all_boxsets'))

@app.route('/edit_boxset/<boxset_id>')
def edit_boxset(boxset_id):
    boxset = mongo.db.addboxset.find_one({"_id": ObjectId(boxset_id)})
    return render_template("editseries.html", boxset=boxset)


@app.route('/delete_boxset/<cards_id>')
def delete_boxset(cards_id):
    cards = mongo.db.addboxset.remove({'_id': ObjectId(cards_id)})
    return redirect(url_for('all_boxsets'))


@app.route('/update_boxset/<boxset_id>', methods=['POST'])
def update_boxset(boxset_id):
    addboxset = mongo.db.addboxset
    boxset = {
        "boxset_image_url": request.form.get("boxset_image_url"),
        "boxset_title": request.form.get("boxset_title"),
        "boxset_seasons": request.form.get("boxset_seasons"),
        "boxset_starring": request.form.get("boxset_starring"),
        "boxset_rating": request.form.get("boxset_rating"),
        "boxset_summary": request.form.get("boxset_summary"),
    }   
    mongo.db.addboxset.update({"_id": ObjectId(boxset_id)}, boxset) 
    return redirect(url_for('view_boxset', cards_id=boxset_id))
    # a GET request means we want to return the html page
    return render_template('allseries.html', boxset=boxset)


@app.route('/view_boxset/<cards_id>', methods=["GET", "POST"])
def view_boxset(cards_id):
    addboxset = mongo.db.addboxset
    cards = addboxset.find_one({"_id": ObjectId(cards_id)})
    return render_template('view.html', cards=cards)


if __name__ == "__main__":
        app.run(host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

    