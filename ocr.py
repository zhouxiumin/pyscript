import sys, urllib, urllib2, json
import base64
import StringIO

url = 'http://apis.baidu.com/apistore/idlocr/ocr'

data = {}
data['fromdevice'] = "pc"
data['clientip'] = "10.10.10.0"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"


file=open('09.jpg','rb')
image= file.read()
file.close()

data['image'] = base64.b64encode(image)
decoded_data = urllib.urlencode(data)

print data['image']

req = urllib2.Request(url, data = decoded_data)

req.add_header("Content-Type", "application/x-www-form-urlencoded")
req.add_header("apikey", "1888dbc6a83d914863a497db3966a542")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
        print(content)