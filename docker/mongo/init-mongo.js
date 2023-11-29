let dbName = 'database'
db = db.getSiblingDB(dbName)

db.createCollection('questions')
db.createCollection('graphs')