from pymongo import MongoClient
con = MongoClient('mongodb://localhost:27017/')
db = con['crud'] # connects to "crud" database
col = db['intern'] # uses the "data" collection
print("connect") # just confirms connection
#install - pymongo, pip install pymongo