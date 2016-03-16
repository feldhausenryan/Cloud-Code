

from pymongo import MongoClient

client = MongoClient()

db = client.CC_Table
test = db.test_table

random_insert = {
	"_id": 1,
	"name": "TEST_VALUE",
	"value": "TEST_VALUE_2",
	}

output = test.insert_one(random_insert).inserted_id

print output
