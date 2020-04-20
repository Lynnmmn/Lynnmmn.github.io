#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Ty"
# Date: 2020-03-05

import requests
import os
import multiprocessing
import re
import json

def w(i):
    """
    解析课程
    """
    url = "http://video.cdeledu.com/vapi/getVideoInfo?biz=cwh5.med&videoRefID=med66.h5.714998.{}&effectType=flash_h&userID=c1b4280661ab1d6da26e9dad9c3dacca".format(i)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload).json()
    print(response)
    if response['errorCode'] == None:
        name = response['result']['videoName'].replace('\u3000',' ')
        video_url = 'http://' + response['result']['videoPath']
        os.system('C:\\Users\\zh11\\Desktop\\By\\ffmpeg.exe -i "{}" -c copy "C:\\Users\\zh11\\Desktop\\By\\temp\\{}.mp4"'.format(video_url,str(i) + ' ' + name))

def s(i):
    headers = {
        'Cookie':'JSESSIONID=19321B3C78DA1D9C4E25CFAAEB2104CC; hd_uid=CjsAXl5gRlpYezQDBCkIAg==; bdp_uuid=24dd9b7b6b-833c3f6e-6386972a77; zg_did=%7B%22did%22%3A%20%22170a8121c833fe-04530acc1da122-4313f6b-15f900-170a8121c847ef%22%7D; trackerSdkVisitor_isNew=true; Hm_lvt_072191e710028974c49838d068b2a510=1583367724,1583371287,1583638665,1584836380; clientID=i5I6IEJ-pcUTuC6MmxoGpNlWXGeC0GqRFka0DHpXQuRhGtHOQmP3kpDoHaLRfjENjEC4-j68OeBv%0D%0AKI0oOu1Fi2LkrX9agNockzqVUK28Ga4%0D%0A; Hm_lvt_b3b7cb0242fd03cca92c6e073af8cf3d=1583369252,1584836389; Hm_lpvt_b3b7cb0242fd03cca92c6e073af8cf3d=1584836389; cdeluid=72674792; username=m9008_56968; lastloginuser=m9008_56968; SelCourse=a|; client_ucToken=72674792-41478de4bf3c113472a25e29a71c4ed5; sid=mql8clblh0dr1mgdu4ucrkd601; _pk_ref.elearning.med66.com.e5c9=%5B%22%22%2C%22%22%2C1584836423%2C%22http%3A%2F%2Fmember.med66.com%2F%2Fhome%2Findex.html%22%5D; _pk_ses.elearning.med66.com.e5c9=*; tgw_l7_route=c4883a4af225815904a914cd874c1f70; _pk_id.elearning.med66.com.e5c9=0fbb293e562384d6.1583369808.4.1584837703.1584836423.; zg_398ef39b99ae45a8b13223f21136d01b=%7B%22sid%22%3A%201584836379818%2C%22updated%22%3A%201584837702613%2C%22info%22%3A%201584836379824%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%7D; Hm_lpvt_072191e710028974c49838d068b2a510=1584837703; trackerSdkData={%22uid%22:%2272674792%22%2C%22platform_source%22:%22web%22%2C%22time%22:1584837702949%2C%22bdp_uuid%22:%2224dd9b7b6b-833c3f6e-6386972a77%22}'
    }
    code = requests.get('http://elearning.med66.com/xcware/video/h5video/videoPlay.shtm?cwareID=714396&videoID=1013',headers=headers).text
    p = re.compile("JSON\.parse\('(.*?)'\);")
    res = p.findall(code)
    print(res[0].replace('\\"','"'))
    res = json.loads(res[0].replace('\\"','"'))
    print(res['videoPath'])


if __name__ == '__main__':
    # l = [101,102,103,104,105,106,107,108]
    # 714998
    l = [1,101,102,201,202,205,203,204,301,302,303,304,401,402,501,601,701,801,802,901,1001,1002,1101,1102,1201,1301,1302]
    pool = multiprocessing.Pool(processes=3)
    pool.map(w,l)
    # s(1)