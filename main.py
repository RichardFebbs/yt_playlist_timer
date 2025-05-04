#!/usr/bin/env python3

from googleapiclient.discovery import build
from datetime import timedelta
import sys
import os
import re
# import json

def main():
    id=input("Enter a playlist ID or URL: ") if len(sys.argv) < 2 else sys.argv[1]
    pattern = re.compile(r"list=([a-zA-Z0-9_-]+)")
    match=pattern.search(id)

    if match:
        id=match.group(1)
    else:
        print("Invalid URL\nTry Again!")
        return

    # MY API KEY
    YT_API_KEY = os.getenv("YT_KEY")
    yt = build("youtube", "v3", developerKey=YT_API_KEY)

    hours_pattern = re.compile(r"(\d+)H")
    minutes_pattern = re.compile(r"(\d+)M")
    seconds_pattern = re.compile(r"(\d+)S")

    totalSeconds = 0
    nextPageToken = None
    while True:
        pl_request = yt.playlistItems().list(part="contentDetails", playlistId=id, maxResults=50, pageToken=nextPageToken)

        pl_response = pl_request.execute()

        vid_ids = []
        for item in pl_response["items"]:
            vid_ids.append(item['contentDetails']['videoId'])

        # print(','.join(vid_ids))
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
    
    print(f"{hours}:{minutes}:{seconds}")


        # json_data = json.dumps(pl_response, indent=4)
        # print(json_data)




if __name__ == "__main__":
    main()
