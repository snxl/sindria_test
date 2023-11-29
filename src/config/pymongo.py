from os import environ

from pymongo import MongoClient

MONGO_URI = environ.get('MONGO_URI')
DATABASE_NAME = environ.get('DATABASE_NAME')

client = MongoClient(MONGO_URI)
mongodb = client[DATABASE_NAME]
