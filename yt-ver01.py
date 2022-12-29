from googleapiclient.discovery import build

api_key = '<Enter_Your_Key_Here>'

youtube = build('youtube', 'v3', developerKey=api_key)

# Return basic YouTube statistics for a user name
request = youtube.channels().list(part='statistics', forUsername='schafer5')

response = request.execute()

print(response)
