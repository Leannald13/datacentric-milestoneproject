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
    return render_template("home.html", addboxset=mongo.db.addboxset.find())


@app.route('/insert_boxset', methods=['POST'])
def insert_boxset():
    addboxset = mongo.db.addboxset
    starring = request.form.get("boxset_starring").splitlines()
    boxset = {
        "boxset_image": request.form.get("boxset_image"),
        "boxset_title": request.form.get("boxset_title"),
        "boxset_seasons": request.form.get("boxset_seasons"),
        "boxset_starring": starring,
        "boxset_rating": request.form.get("boxset_rating"),
        "boxset_summary": request.form.get("boxset_summary"),
    }
    addboxset.insert_one(boxset)
    return redirect(url_for('add_boxset'))


@app.route('/edit_boxset/<boxset_id>')
def edit_boxset(boxset_id):
    boxset = mongo.db.addboxset.find_one({"_id": ObjectId(boxset_id)})
    return render_template("editseries.html", boxset=boxset)


@app.route('/update_boxset/<boxset_id>', methods=['POST'])
def update_boxset(boxset_id):
    addboxset = mongo.db.addboxset
    starring = request.form.get("boxset_starring").splitlines()
    boxset = {
        "boxset_image": request.form.get("boxset_image"),
        "boxset_title": request.form.get("boxset_title"),
        "boxset_seasons": request.form.get("boxset_seasons"),
        "boxset_starring": starring,
        "boxset_rating": request.form.get("boxset_rating"),
        "boxset_summary": request.form.get("boxset_summary"),
    }
    mongo.db.addboxset.update({"_id": ObjectId(boxset_id)}, boxset)
    return redirect(url_for('add_boxset'))


@app.route('/view_boxset/<cards_id>', methods = ["GET", "POST"])
def view_boxset(cards_id):
    addboxset = mongo.db.addboxset
    cards = addboxset.find_one({"_id": ObjectId(cards_id)})
    
    boxset_reviews = mongo.db.review.find({}, {"boxset_id": cards_id})

    return render_template('view.html', cards=cards, reviews=boxset_reviews)


@app.route('/add_review/<boxset_id>', methods=["GET", "POST"])
def add_review(boxset_id):
    boxset = mongo.db.addboxset.find_one({"_id": ObjectId(boxset_id)})
    boxset_id = mongo.db.addboxset.find_one({"_id": ObjectId(boxset_id)})["_id"]
    if request.method == "POST":
        # a POST request means that we're being sent review data from a form
        review = {
            "review_rating": request.form.get("review_rating"),
            "review_message": request.form.get("review_message"),
        }
        mongo.db.addboxset.update_one({"_id": ObjectId(boxset_id)}, {"$push": {"boxset_reviews": review}})
        return redirect(url_for('view_boxset', cards_id=boxset_id))
    # a GET request means we want to return the html page
    return render_template('addreview.html', boxset=boxset)


@app.route('/edit_review/<boxset_id>/<review_id>', methods=["GET", "POST"])
def edit_review(boxset_id, review_id):
    boxset = mongo.db.addboxset.find_one({"_id": ObjectId(boxset_id)})
    review_array = mongo.db.addboxset.find_one({"_id": ObjectId(boxset_id)})["boxset_reviews"]
    review = ""
    for item in review_array:
        if int(review_array.index(item)) == int(review_id):
            review = item
    if request.method == "POST":
        form = {
            "review_rating": request.form.get("review_rating"),
            "review_message": request.form.get("review_message"),
        }
        mongo.db.addboxset.update_one({"_id": ObjectId(boxset_id)}, {"$push": {"boxset_reviews": form}})
        return redirect(url_for('view_boxset', cards_id=boxset_id))
    # GET request
    return render_template('editreview.html', boxset=boxset, review_id=review, review=review)



     


if __name__ == "__main__":
        app.run(host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
