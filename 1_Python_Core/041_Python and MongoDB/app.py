from flask import Flask, render_template
import os
import pymongo

MONGODB_URI = 'mongodb+srv://himanshu_flask:flask12345@cluster0.4c5adr8.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(MONGODB_URI)

# creating database
db = client.masterdexter
# db = client['masterdexter']

# creating student collection and insert values
# db.students.insert_one({'name':'Pushparaj', 'city':'Indore', 'age':21})

# inserting multiple documents into a collection

# student = [
#     {'name':'Rohit', 'city':'Indore', 'age':21},
#     {'name':'Nandini', 'city':'Bhopal', 'age':21, "PG":"Master of Science"},
#     {'name':'Sachin', 'city':'Goa', 'age':21},
# ]

# for s in student:
#     db.students.insert_one(s)

# CRUD - Create Read Update Delete
# Read - find

# result = db.students.find_one()
# print(result)

# result = db.students.find_one({'name':'Rohit'})
# print(result)

# result = db.students.find()
# print(result)

# for r in result:
#     print(r)


# print(client.list_database_names())

# query and modifier and update

# query = {
#     'city':'Indore'
# }

# query = {
#     'age':21
# }
# new_value = {
#     '$set': { 'age': 36 }
# }

# student = db.students.find(query)
# for s in student:
#     print(s)

# db.students.update_one(query, new_value)

# for s in db.students.find():
#     print(s)


# # delete document
# query = {'name': 'Rohit'}

# db.students.delete_one(query)

# drop a collection

db.students.drop()

app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug = True,port=port)












# SQL              NoSQL
# Database        Database
# Tables          Collections
# Rows            Documents
# Columns         Fields