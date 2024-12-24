from pymongo import MongoClient
connection_string = "mongodb+srv://sharmaajay:Qf7LUqn4Z6vmnNa9@farmerproject.mgwfz.mongodb.net/?retryWrites=true&w=majority&appName=farmerproject"
client = MongoClient(connection_string)
database = client['Farmer']
collection = database['FarmerData']
documents = collection.find()  #select * from table;
for document in documents:
    print(document)
print("thank you")