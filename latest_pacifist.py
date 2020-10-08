import requests
import webbrowser
import time

api_key = 'Get API at console.developers.google.com and go to Credentials'
channel_id = 'UCkH00DEvivJzUfQk2KVsA4A' # T-West's channel ID
playlist_id = 'UUkH00DEvivJzUfQk2KVsA4A' # latest uploads in the channel
playlist_url = 'https://www.googleapis.com/youtube/v3/playlistItems?'

def check_latest_video():

	curl = (playlist_url + f'playlistId={playlist_id}&key={api_key}' 
    		'&part=snippet&fields=items(snippet(title, resourceId))'
    		'&maxResults=1') # only fetch the title and videoId info

	channel = requests.get(curl)
	response = channel.json()
	info = response['items'][0]['snippet']
	title = info['title'].lower()

	phrase1 = "aoe2: is it possible to win the"
	phrase2 = "without killing enemy units"
	# search for a specific phrase(s) in the video title
	if (phrase1 in title) or (phrase2 in title):
		watch_url = 'https://www.youtube.com/watch?v='
		vid_id = info['resourceId']['videoId']
		video_url = watch_url + vid_id
		webbrowser.open(video_url)
		return True

print("Status: Checking...\n")
while True:
	if not check_latest_video():
		time.sleep(10)
		continue
	else:
		break