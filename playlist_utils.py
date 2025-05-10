import re
import os
from datetime import timedelta
from googleapiclient.discovery import build

def parse_input(ids):
    pattern = re.compile(r"list=([a-zA-Z0-9_-]+)")

    for ID in ids:
        if ID is None:
            return None
        match=pattern.search(ID)

        if match:
            ID=match.group(1)
        else:
            print(match)
            print("Invalid URL\nTry Again!")
            return
    return ID

def get_playlist_data(ID):
    # API KEY
    YT_API_KEY = os.getenv("YT_KEY")
    yt = build("youtube", "v3", developerKey=YT_API_KEY)

    hours_pattern = re.compile(r"(\d+)H")
    minutes_pattern = re.compile(r"(\d+)M")
    seconds_pattern = re.compile(r"(\d+)S")

    totalSeconds = 0
    nextPageToken = None
    while True:
        pl_request = yt.playlistItems().list(part="contentDetails", playlistId=ID, maxResults=50, pageToken=nextPageToken)
        pl_response = pl_request.execute()

        # Different request/response to get the playlist title
        pl2_req = yt.playlists().list(part="snippet", id=ID)
        pl2_res = pl2_req.execute()
        pl_title = pl2_res["items"][0]["snippet"]["title"]

        vid_ids = []
        for item in pl_response["items"]:
            vid_ids.append(item['contentDetails']['videoId'])

        vid_requests = yt.videos().list(part="contentDetails", id=','.join(vid_ids))
        vid_response = vid_requests.execute()


        for item in vid_response['items']:
            duration = item['contentDetails']['duration']

            hours = hours_pattern.search(duration)
            minutes = minutes_pattern.search(duration)
            seconds = seconds_pattern.search(duration)

            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0
            seconds = int(seconds.group(1)) if seconds else 0

            video_seconds =  timedelta( hours = hours, minutes = minutes, seconds = seconds).total_seconds()
            totalSeconds += video_seconds

        nextPageToken = pl_response.get('nextPageToken')
        if not nextPageToken:
            break

    totalSeconds = int(totalSeconds)
    minutes, seconds = divmod(totalSeconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    return f"[{pl_title}] ~ {hours}:{minutes:02d}:{seconds:02d}"
