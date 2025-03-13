from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from creator_services.upload_song import UploadSongService

upload_router = APIRouter()

class UploadSongModel(BaseModel):
    user_name: str
    song_name: str
    artists: str
    playlist: str
    icon: str
    song_link: str

upload_service = UploadSongService()

@upload_router.post('/upload_song')
def upload_song(upload_details: UploadSongModel):
    try:
        # Call the service to upload the song
        upload_details = dict(upload_details)
        response = upload_service.upload_song(upload_details)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
