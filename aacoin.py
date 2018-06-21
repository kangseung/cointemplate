# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import urllib
import hashlib
import hmac
import base64
import datetime
import requests 
import json
import traceback
import time
from copy import *

# 常量定义
TIMEOUT = 5
API_HOST = ""
LANG = 'en-GB'
ACCESS_KEY=''
SECRET_KEY=''
DEFAULT_GET_HEADERS = {
    "Content-type": "application/x-www-form-urlencoded",
    'Accept': 'application/json',
    'Accept-Language': LANG,
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
}

DEFAULT_POST_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Language': LANG,
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'    
}

hosturl="https://%s"%API_HOST

def httpPost(url,resource,params):
     headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "charset":"UTF-8",
            "Content-Length":"116",
            "Chunked":"false"
     }
     temp_params = urllib.parse.urlencode(params)
     print ("------------------------------")
     print ("temp_params:      %s"%temp_params)
     print ("------------------------------")
     response=requests.post(hosturl+resource,params)
     return response.text

def createSign(params, secretKey):
    """生成签名"""
    params = sorted(params.items(), key=lambda d:d[0], reverse=False)
#    params.append(('secret_key', secretKey))
    message = urllib.parse.urlencode(params)

    #message = bytes(message,encoding='utf-8')
    #secret = bytes(secretKey,encoding='utf-8')
    print ("------------------------------")
    print ("message:      %s"%message)
    print ("------------------------------")

    signature = hmac.new(secretKey.encode('utf8'),msg=message.encode('utf8'),digestmod=hashlib.sha256).hexdigest().lower()
    
    print ("------------------------------")
    print ("signature:      %s"%signature)
    print ("------------------------------")


    return signature
    
#----------------------------------------------------------------------
def preparePost(path,params):
    params ={}
    params['accessKey'] = ACCESS_KEY
    params['sign'] = createSign(params,SECRET_KEY)
    return httpPost(API_HOST,path,params)