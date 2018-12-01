import pymongo
myclient = pymongo.MongoClient()
mydb = myclient["twitter_mongo"]
mycol = mydb.user
mycol.drop()
print(myclient.list_database_names())

