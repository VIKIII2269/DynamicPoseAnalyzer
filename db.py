from pymongo import MongoClient

client = MongoClient('localhost', 27017)


db = client.pose_estimation_db


pose_results_collection = db.pose_results
