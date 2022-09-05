from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.csqemc6.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech 
try:
    print(db.list_collection_names)
    print('--Pytech Collecton List--')
    print('[''students'']')
    print('End of program. Press any key to exit...')
except Exception:
    print('Unable to connect to server')

    