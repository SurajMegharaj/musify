from pymongo import MongoClient


class MongoDB:
    def __init__(self, uri="mongodb://root:example@localhost:27017", db_name="music_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]


    def insert_song(self, song_data):
        try:
            songs_collection = self.db['songs']  
            result = songs_collection.insert_one(song_data)
            return str(result.inserted_id)
        except Exception as e:
            raise Exception(f"Error inserting song: {str(e)}")
