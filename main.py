# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.upload import upload_router 



app = FastAPI(
    title="Music and Video Streaming App", 
    description="API for a music and video streaming service", 
    version="1.0.0"
)

# 3. Middleware configuration
# Allow CORS (Cross-Origin Resource Sharing) for specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Register routers for different APIs
app.include_router(upload_router, prefix="", tags=["upload_song"])

# 5. Root route (optional)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Music and Video Streaming App"}

# 6. Run the app (optional for Uvicorn-based deployment)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

