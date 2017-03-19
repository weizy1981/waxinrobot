'''
Created on Mar 19, 2017

@author: weizhenyuan
'''
import itchat
import time
import re
from itchat.content import *
import urllib, urllib2
import json
from pip._vendor.requests.models import Response

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.get_contact()
    itchat.send_msg(msg['RecommendInfo']['UserName'], 'Nice to meet you!')
    
    
@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    info = msg['Text'].encode('UTF-8')
    wechatUserid = msg['FromUserName']
    url = 'http://www.tuling123.com/openapi/api'
    data = {u"key" : "3290214d04154ea199a56e95c7dc8aae", "info" : info, u"loc" : "", "userid" : ""}
    data = urllib.urlencode(data)
    url2 = urllib2.Request(url, data)
    response = urllib2.urlopen(url2)
    apicontent = response.read()
    s = json.loads(apicontent, encoding='utf-8')
    print 's====', s['text']
    print 's====', s['code']
    #print 'msg====', msg['FromUserName']
    #itchat.send(msg=s['text'], toUserName=wechatUserid)
    
    if s['code'] == 100000 :
        itchat.send(msg=s['text'], toUserName=wechatUserid)

@itchat.msg_register('Text', isGroupChat = True)
def text_reply(msg):
    info = msg['Content']
    wechatUserid = msg['FromUserName']
    #SfromNickName = msg['ActualNickName']
    '''myNickName = '@Kevin'
    #isAt = False
    isAt = msg['isAt']
    if isAt :
        info = info.replace(myNickName, '')'''
    info = info.encode('UTF-8')
    #print info
    
    url = 'http://www.tuling123.com/openapi/api'
    data = {u"key" : "3290214d04154ea199a56e95c7dc8aae", "info" : info, u"loc" : "", "userid" : ""}
    data = urllib.urlencode(data)
    url2 = urllib2.Request(url, data)
    response = urllib2.urlopen(url2)
    apicontent = response.read()
    s = json.loads(apicontent, encoding='utf-8')
    print 's====', s['text']
    print 's====', s['code']

    if s['code'] == 100000 :
        #print s['text']
        itchat.send(msg=s['text'], toUserName=wechatUserid)
           
#itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.auto_login(hotReload=True)
#itchat.login()
itchat.run(debug = False)