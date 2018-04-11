#!/usr/bin/env python
#-*- coding:utf-8 -*-
import  requests
import  urllib
import lxml


# for i in  range(10):
#     name = str(i+1)+''+arr[i]['name']+'.mp3'
    # link = arr[i]['mp3Url']
    # urllib.urlretrieve(link, '网易云音乐' + name)
    # print (name + '完成')


if __name__ == '__main__':
        r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')
        arr = r.json()['result']['tracks']
        # print r.json()['result']
        print  len(arr)
        for json in arr:
            # print  'name:'+arr[i]['name']
            # print i
            name = json['name']
            arr1 =  json['artists']
            link =  arr1[0]['picUrl']
            # print link
            # print name
            urllib.urlretrieve(link, '%s.jpg' % name )
            # print ('完成')
        # pass



