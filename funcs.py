import yt_dlp
from typing import List, Union

def DownloadMusic(UrlList: Union[List[str], str]) -> List[str]:
    audio_urls = []

    if type(UrlList) != list:
        return "required list"

    # Settings for the downloader to only grab audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for i in UrlList:
            try:
                # We use the Spotify URL/ID to search YouTube for the exact audio track
                info = ydl.extract_info(f"ytsearch1:{i} audio", download=False)
                if 'entries' in info and len(info['entries']) > 0:
                    # Grab the direct audio stream link
                    url = info['entries'][0]['url']
                    audio_urls.append(url)
            except Exception as e:
                print(f"Failed to scrape: {e}")
                
    return audio_urls
