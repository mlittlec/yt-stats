

import os
import re
from datetime import timedelta
from googleapiclient.discovery import build

api_key = os.environ.get('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

# Define a Regular Expression to parse the Duration field from the YT API responses.
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

total_seconds = 0

nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
    #request = youtube.channels().list(
        part="contentDetails",
        playlistId="<channel-id-queried>",
        maxResults=50,
        pageToken=nextPageToken
        #forUsername="schafer5"
    )

    pl_response = pl_request.execute()

    # print(pl_response) # Print out the first 5 records returned
    vid_ids = [] # Make a List to hold Video ID details (to reduce API calls)
    for item in pl_response['items']:
        vid_ids.append(vid_id = item['contentDetails']['videoId'])
        # print(vid_id)
        # print()

    print(','.join(vid_ids)) # Confirm the List returns a Comma separated list of the Video IDs - comment once script is live

    vid_request = youtube.videos().list(
        part="contentDetails", 
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()



    # Note: The YouTube API limits the # of responses to 50 for each request, so Playlists longer than this will return the 
    # first 50 videos only

    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) # these values apply something called a ternary conditional statement (see below) 
        minutes = int(minutes.group(1)) if minutes else 0 # this ensures the value doesn't return an error by replacing a NULL value with zero
        seconds = int(seconds.group(1))

        video_seconds = timedelta(
                hours = hours,
                minutes = minutes,
                seconds = seconds
        ).total_seconds()

        total_seconds += video_seconds

        print(item)
        print(duration)
        print(hours, minutes, seconds)
        print(video_seconds)
        print()
    
    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

print(total_seconds)

total_seconds = int(total_seconds)

# Use divmod() to calculate the total no. of minutes and assign this to 'minutes' and place the remainder in 'seconds'
minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)

print(f'{hours}:{minutes}:{seconds}')
 