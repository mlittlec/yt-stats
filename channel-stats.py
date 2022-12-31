import os
from googleapiclient.discovery import build

api_key = os.environ.get('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

pl_request = youtube.playlists().list(
#request = youtube.channels().list(
    part="contentDetails, statistics",
    channelId="<channel-id-queried"
    #forUsername="schafer5"
)

pl_response = pl_request.execute()

print(response)
