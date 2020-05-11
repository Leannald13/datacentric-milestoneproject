import os
import flask.config
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
def home_page():
    return render_template("home.html", addboxset=mongo.db.addboxset.find())


@app.route('/add_boxset')
def add_boxset():
    return render_template("addseries.html",
                           addboxset=mongo.db.addboxset.find())


@app.route('/add_review/<boxset_id>')
def add_review(boxset_id):
    return render_template("addseriesreview.html", boxset_id=boxset_id)


@app.route('/all_boxsets')
def all_boxsets(offset=0, per_page=9):
    page, per_page, offset = get_page_args(page_parameter='page')
    total = mongo.db.addboxset.count()
    allboxsets = mongo.db.addboxset.find().sort(
        'boxset_title', pymongo.ASCENDING)
    pagination = Pagination(offset=offset, page=page, per_page=per_page,
                            total=total, css_framework='materialize')
    boxsets_per_page = 9
    num_pages = boxsets_per_page
    return render_template(
        'allseries.html',
        addboxset=mongo.db.addboxset.find().skip(offset).limit(9).sort(
            'boxset_title', pymongo.ASCENDING),
        page=page, per_page=per_page,
        pagination=pagination, allboxsets=allboxsets,
        boxsets_per_page=boxsets_per_page,
        num_pages=num_pages)


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


@app.route('/insert_review/<boxset_id>', methods=["GET", "POST"])
def insert_review(boxset_id):
    userreviews = mongo.db.userreviews
    review = {
        "review_rating": request.form.get("review_rating"),
        "review_message": request.form.get("review_message"),
        "boxset_id": boxset_id
    }
    userreviews.insert_one(review)
    return redirect(url_for('view_boxset', cards_id=boxset_id))


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
    return render_template('allseries.html', boxset=boxset)


@app.route('/view_boxset/<cards_id>', methods=["GET", "POST"])
def view_boxset(cards_id):
    addboxset = mongo.db.addboxset
    cards = addboxset.find_one({"_id": ObjectId(cards_id)})
    reviews = mongo.db.userreviews.find({"boxset_id": cards_id})
    print(reviews)
    return render_template('view.html', cards=cards, reviews=reviews)


@app.route('/search', methods=['GET'])
def search():
    search_bar = request.args.get('search_bar')
    print(search_bar)
    addboxset = list(mongo.db.addboxset.find(
        {"boxset_title": {"$regex": f'(?i).*{search_bar}.*'}}))
    print(addboxset)
    return render_template('search.html', results=addboxset)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)
