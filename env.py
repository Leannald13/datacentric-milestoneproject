import os

os.environ["MONGO_DBNAME"] = "boxsetReviews" 
os.environ["MONGO_URI"] = "mongodb+srv://root:r00tUser@datacentriccluster-snqmw.mongodb.net/boxsetReviews?retryWrites=true&w=majority" 

from os import path
if path.exists("env.py"):
  import env 