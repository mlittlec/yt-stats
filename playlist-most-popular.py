
import os
from googleapiclient.discovery import build

api_key = os.environ.get('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = '<channel-id-queried>'

videos = []

nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
    #request = youtube.channels().list(
        part="contentDetails",
        playlistId=playlist_id,
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
        part="statistics", 
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    # Note: The YouTube API limits the # of responses to 50 for each request, so Playlists longer than this will return the 
    # first 50 videos only

    for item in vid_response['items']:
        vid_views = item['statistics']['viewCount']

        vid_id = item['id']
        yt_link = f'https://youtu.be/{vid_id}'

        videos.append(
            {
                'views': int(vid_views),
                'url': yt_link
            }
        )

        # print(item)
        # print(duration)
        # print(hours, minutes, seconds)
        # print(video_seconds)
        # print()
    
    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

videos.sort(key=lambda vid: vid['views'], reverse=True)

for video in videos:
    print(video['url']. video['views'])

print(len(videos))