from pymongo import MongoClient
import account


def start_work_data_base(artists):
    cluster = MongoClient(InfoConnection)  # for new network change info_connection
    db = cluster["TEST-BACKEND"]
    collection = db["collection-test"]
    collection.insert_many(artists)  # add artists to db
    print("Info installed in DataBase,press any key and start print from database")
    input()
    artists_db = collection.find()
    for artist in artists_db:
        print(artist)
