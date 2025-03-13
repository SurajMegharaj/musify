from fastapi import HTTPException
from databases_services.connect_mongodb import MongoDB

class UploadSongService:
    def __init__(self):
        self.mongo_db = MongoDB()

    def upload_song(self, song_data):
        try:
            song_id = self.mongo_db.insert_song(song_data)
            return {"status": "success", "song_id": song_id}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
