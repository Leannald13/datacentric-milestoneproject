import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'boxsetReviews'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@datacentriccluster-snqmw.mongodb.net/boxsetReviews?retryWrites=true&w=majority'

mongo = PyMongo(app)
    

@app.route('/')
def index():
    return render_template("base.html", review=mongo.db.review.find())


if __name__ == '__main__':
    app.run(host='0.0.0.0',
        port=5000,
        debug=True)
