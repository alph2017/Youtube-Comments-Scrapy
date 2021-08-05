from googleapiclient.discovery import build

import os
import pandas as pd


# update the proxy settings
# os.environ['HTTP_PROXY'] = 'my_proxy_id:proxy_port'
# os.environ['HTTPS_PROXY'] = 'my_proxy_id:proxy_port'
# os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10024'
# os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10024'


api_key = ''
video_id=""

youtube = build('youtube', 'v3', developerKey=api_key)
youtubeHeader=["authorDisplayName","textDisplay","likeCount","publishedAt","totalReplyCount","是否是二级评论","是谁的二级评论"]
youtubeList=[]
youtubeList.append(youtubeHeader)

def GetAllComments(nextPageToken):
    request=None
    if(len(nextPageToken)==0):
        request = youtube.commentThreads().list(
            part="snippet",
            maxResults=100,
            videoId=video_id,
            textFormat="plainText",
            order="time",
        ) #按照热门评论搜索
    else:
        request = youtube.commentThreads().list(
            part="snippet",
            maxResults=100,
            videoId=video_id,
            textFormat="plainText",
            order="time",
            pageToken=nextPageToken
        ) #按照热门评论搜索

    response = request.execute()
    # print(response)
    for data in response["items"]:
        user=data["snippet"]["topLevelComment"]["snippet"]
        authorDisplayName=user["authorDisplayName"]
        textDisplay=user["textDisplay"]
        likeCount=user["likeCount"]
        publishedAt=user["publishedAt"]
        totalReplyCount=data["snippet"]["totalReplyCount"]
        youtubeList.append([authorDisplayName,textDisplay,likeCount,publishedAt,totalReplyCount,"0","0"])
        # print(youtubeList)
        if(totalReplyCount>0):
            GetAllReplies(parentId=data["id"],parentName=authorDisplayName,nPageToken="")

    if ("nextPageToken" in response):
        nextPageToken = response["nextPageToken"]
        GetAllComments(nextPageToken)



def GetAllReplies(parentId,parentName,nPageToken):
    # print("GetAllReplies")
    request=None
    if(len(nPageToken)==0):
        request = youtube.comments().list(
            part="snippet",
            maxResults=100,
            parentId=parentId,
            textFormat="plainText",
        )
    else:
        request = youtube.comments().list(
            part="snippet",
            maxResults=100,
            parentId=parentId,
            textFormat="plainText",
            pageToken=nPageToken
        )
    response = request.execute()
    # print(response)
    for data in response["items"]:
        user = data["snippet"]
        authorDisplayName = user["authorDisplayName"]
        textDisplay = user["textDisplay"]
        likeCount = user["likeCount"]
        publishedAt = user["publishedAt"]
        youtubeList.append([authorDisplayName, textDisplay, likeCount, publishedAt, "0", "是", parentName])


    if ("nextPageToken" in response):
        nextPageToken = response["nextPageToken"]
        GetAllReplies(parentId,parentName,nextPageToken)


GetAllComments('')

res=pd.DataFrame(columns=youtubeHeader,data=youtubeList)

res.to_csv('youtube2.csv',encoding="utf_8_sig")








