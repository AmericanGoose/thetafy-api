from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from spotify_search import SearchFromSpotify
from funcs import DownloadMusic

app = FastAPI()

# --- THE FIX: This allows your Thetafy UI to fetch data from this API ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from anywhere (like your Netlify site)
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.get("/download-music/")
async def download_music(track_name: str = Query(..., title="Track Name", description="Name of the track to search"),
                         limit: int = Query(..., title="Limit", description="Limit the number of search results")):
    try:
        track_urls = SearchFromSpotify(track_name, limit)
        audio_urls = DownloadMusic(track_urls)

        return {"downloaded_audio_urls": audio_urls}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")