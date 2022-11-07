from googleapiclient.discovery import build
import numpy as np

# import logging

# logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)
API_KEY = 'AIzaSyBgO8HDVuQJD1iMaYJojImRWfL4CT6YRiQ'
youtube = build('youtube', 'v3', developerKey = API_KEY)

list_check_snippet_video = ['channelId', 'channelTitle', 'title', 'publishedAt','description','thumbnails','tags','categoryId'] 
list_check_statistics_video = ['viewCount', 'likeCount','commentCount']

def fill_key(list_key_check = list(), dict_check = dict()):
    list_key_current = list(dict_check.keys())
    for i in list_key_check:
        if i not in list_key_current:
            dict_check[i] = np.nan
    return dict_check

def subcribers_a_channel(youtube, channel_id):
    request = youtube.channels().list(
        part = 'statistics',
        id = channel_id
    )
    response = request.execute()
    return response['items'][0]['statistics']['subscriberCount']

def get_video_info(youtube, video_id, list_check_snippet_video,list_check_statistics_video):
    
    request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id= video_id)
        
    response = request.execute()
    video = response['items'][0]
    video_snippet = fill_key(list_check_snippet_video, video['snippet'])
    video_statistics = fill_key(list_check_statistics_video, video['statistics'])
    video_channelId = video_snippet['channelId']
    video_info = dict(
        video_channelId = video_snippet['channelId'],
        video_channelTitle = video_snippet['channelTitle'],
        video_channelSubscriber = subcribers_a_channel(youtube, video_channelId),
        video_id =  video['id'],
        video_title = video_snippet['title'],
        video_publishedAt = video_snippet['publishedAt'],
        video_description = video_snippet['description'],
        video_thumbnails = video_snippet['thumbnails']['default']['url'],
        video_tags = video_snippet['tags'],
        video_categoryId = video_snippet['categoryId'],
        video_viewCount = video_statistics['viewCount'],
        video_likeCount = video_statistics['likeCount'],
        video_commentCount = video_statistics['commentCount'],
        video_duration = video['contentDetails']['duration'],
    )
   
    return video_info
  
# print(type(get_video_info(youtube,'rH8P_JavvXQ',list_check_snippet_video,list_check_statistics_video)))
