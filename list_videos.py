import subprocess
import os

# import urllib.request as urlreq
import urllib
import urlparse
# import urllib.parse as urlparse
import json

playlistIds = []
titles = []

def getPlaylistId():
    data = {}
    data['maxResults'] = '50'
    # data['channelId'] = 'UCsooa4yRKGN_zEE8iknghZA' # Put the channelId of channel you want to Sync to.
    data['part'] = 'snippet'
    # data['key'] =   'AIzaSyAngcF6oKnyEbhk3KyL9Wz1OhSi28JjbzE'
    data['key'] = 'AIzaSyCOTXM-Rfhbtym9Ikxp6g4cr0ixlv6IAaY'
    data['playlistId'] = 'PLJicmE8fK0EiFRt1Hm5a_7SJFaikIFW30'
    requestValues = urllib.urlencode(data)
    # request = "https://www.googleapis.com/youtube/v3/playlists?" + requestValues
    # string = urlreq.urlopen(request).read().decode('utf-8')
    request = "https://www.googleapis.com/youtube/v3/playlistItems?" + requestValues
    string = urllib.urlopen(request).read().decode('utf-8')
    # items = json.loads(string)['items']
    json_data = json.loads(string)
    # url_prefix = json.loads(string)['thumbnails']['default']['url']
    with open('url_file.txt', 'w') as f:
        url_list = []
        for items in json_data['items']:
            temp = 'https://youtube.com/watch?v={}&list={}'.format(items['snippet']['thumbnails']['default']['url'].split('/')[4],data['playlistId'])
            f.write(temp)
            url_list.append('https://youtube.com/watch?v={}&list={}'.format(items['snippet']['thumbnails']['default']['url'],data['playlistId']))
            f.write('\n')
            # f.write
    # exact_url_prefix = json_data['items'][2]['snippet']['thumbnails']['default']['url'].split('/')[4]
    # video_url ='?v={}&list={}'.format(exact_url_prefix, data['playlistId'])
    # print video_url
    import codecs
    with codecs.open('videos3.txt','w', 'utf-8') as f:
        f.write(string)

    # for item in items:
    #     playlistIds.append(item['id'])
    #     titles.append(item['snippet']['title'])

# def download():
#     for ids,title in zip(playlistIds,titles):
#             url = "https://www.youtube.com/playlist?list=" + ids
#             if not os.path.exists(title):
#                 os.makedirs(title)
#             os.chdir("./" + title)
#             url_down = "youtube-dl -o '%(title)s' " + url
#             subprocess.call(url_down, shell=True)
#             os.chdir("..")

if __name__ == '__main__':
    getPlaylistId()
    # download()