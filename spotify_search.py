import spotipy,json
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'a25f4d59e37d49029f5113908d583c27'
client_secret = '617fc5c8f0634a26a34bcfc956a25921'

# If you have any questions about client_id and client_secret, welcome to ask Telegram: @ai_junior

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def SearchFromSpotify(track_name,limit):
    results = sp.search(q=track_name, type='track', limit=limit)
    track_urls = [item["external_urls"]["spotify"] for item in results["tracks"]["items"]]
    return track_urls
