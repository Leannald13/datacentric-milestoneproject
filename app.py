import os
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
def index():
    return render_template("index.html", review=mongo.db.review.find())

@app.route('/add_new') 
def add_new():
    return render_template("typeofshow.html", genre=mongo.db.genre.find())


@app.route('/add_boxset') 
def add_boxset():
    return render_template("addseries.html", addboxset=mongo.db.addboxset.find())

@app.route('/add_user') 
def add_user():
    return render_template("userinfo.html", user=mongo.db.user.find())

@app.route('/home_page') 
def home_page():
    return render_template("home.html", homepage=mongo.db.homepage.find())


@app.route('/insert_boxset', methods=['POST'])
def insert_boxset():
    addboxset = mongo.db.addboxset
    addboxset.insert_one(request.form.to_dict())
    return redirect(url_for('add_boxset'))


@app.route('/view_boxset/<cards_id>')
def view_boxset(cards_id):
    homepage = mongo.db.homepage
    cards = homepage.find_one({"_id": ObjectId(cards_id)})
    return render_template('view.html', cards=cards)


    """
@app.route('/add_review/<cards_id>', methods = ["GET", "POST"])
def add_review(cards_id):
    review = mongo.db.review
    cards = review.find_one({"_id": ObjectId(cards_id)})
    return render_template('addreview.html', cards=cards)
    """ 

    
@app.route('/add_review/<cards_id>', methods=["POST"])
def add_review(cards_id):
    cards = mongo.db.review
    mongo.db.review.update({"_id": ObjectId(cards_id)}), 

    if request.method == "POST":

        { 
        'review_rating': request.form.get('review_rating'),
        'review_message': request.form.get('review_message')

        }

    cards.insert_one(request.form.to_dict())

    return render_template('addreview.html', cards=cards)
     


if __name__ == '__main__':
    app.run(host='0.0.0.0',
        port=5000,
        debug=True)
