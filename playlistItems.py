import os
import re
from googleapiclient.discovery import build

api_key = os.environ.get('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

pl_request = youtube.playlistItems().list(
#request = youtube.channels().list(
    part="contentDetails",
    playlistId="<channel-id-queried>"
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

# Define a Regular Expression to parse the Duration field from the YT API responses.
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

# Note: The YouTube API limits the # of responses to 50 for each request, so Playlists longer than this will return the 
# first 50 videos only

for item in vid_response['items']:
    duration = item['contentDetails']['duration']

    hours = hours_pattern.search(duration)
    minutes = minutes_pattern.search(duration)
    seconds = seconds_pattern.search(duration)

    print(item)
    print(duration)
    print(hours, minutes, seconds)
    print()
