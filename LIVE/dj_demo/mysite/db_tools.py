from pymongo import MongoClient

client = MongoClient()

db = client.CC_Table
inv_index = db.inv_index
code_base = db.code_base

def insertCodeIntoDatabase(code, comment):
    insert_value = {
        "code": code,
        "comment": comment,
        }
    
    code_base.insert_one(insert_value)

def insertWordIntoDatabase(word):
    
def findFromDatabase():
    
    
    
