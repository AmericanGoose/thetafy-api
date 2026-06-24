import yt_dlp
from typing import List, Union

def DownloadMusic(UrlList: Union[List[str], str]) -> List[str]:
    audio_urls = []

    if type(UrlList) != list:
        return "required list"

    # THE FIX: We disguise the scraper as an Android device to bypass the YouTube Bot Block
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'extractor_args': {'youtube': ['player_client=android']} 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for i in UrlList:
            try:
                # We are switching back to YouTube search (ytsearch1)
                info = ydl.extract_info(f"ytsearch1:{i}", download=False)
                if 'entries' in info and len(info['entries']) > 0:
                    url = info['entries'][0]['url']
                    audio_urls.append(url)
            except Exception as e:
                print(f"Failed to scrape: {e}")
                
    return audio_urls
