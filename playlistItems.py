import os
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

for item in pl_response['items']:
    vid_id = item['contentDetails']['videoId']
    print(vid_id)
    print()
