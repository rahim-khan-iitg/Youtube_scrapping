from googleapiclient.discovery import build
api_key="AIzaSyDxQkZ1ik7V9uMZ4QaH3GQFcnIlySU2BBI"
youtube=build('youtube','v3',developerKey=api_key)
def get_video_id(link:str)->str:
    i=link.find("watch?v=")
    link=link[i:]
    return link[8:]
def get_data_1(videoid:str,pagetoken=None):
    request=youtube.commentThreads().list(part='snippet',videoId=videoid,maxResults=100,pageToken=pagetoken,textFormat='plainText')
    response=request.execute()
    return response

def process_response(response:dict)->tuple:
    items=response['items']
    
    data=[]
    for i in items:
        data.append((i['snippet']['topLevelComment']['snippet']['authorDisplayName'],i['snippet']['topLevelComment']['snippet']['textDisplay']))
    try:
       next_token=response['nextPageToken']
    except:
        return
    return(next_token,data)

def get_data(video_link:str,ans:list,pagetoken=None):
    try:
        videoid=get_video_id(video_link)
        res=get_data_1(videoid,pagetoken)
        data=process_response(res)
        pagetoken=data[0]
        for comment in data[1]:
            if len(ans)>1000: return
            ans.append((comment[0],comment[1]))
        get_data(video_link,ans,pagetoken)
    except Exception as e:
        return

# ans=[]
# link="https://www.youtube.com/watch?v=RGKi6LSPDLU"
# get_data(link,ans)
# for com in ans:
#     print(com)
