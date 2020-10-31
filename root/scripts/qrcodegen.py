import qrcode
from PIL import Image
import io
import requests
import base64
import os
import json
f = open("/root/rube-files/message.txt", "r")

img = qrcode.make(f.read())
os.remove("/root/rube-files/message.txt")

print(type(img))
print(img.size)
img.save('qrcode.png')
imgurl = ""
with open("qrcode.png", "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key":"f048206a78bff2540368b9376f2c7fb3",
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)
    j = json.loads(res.text)
    u = j['data']
    imgurl = u['url']
    print(imgurl)
binurl = "https://api.jsonbin.io/v3/b/5f9dc3253269193b17bfec93"
headers = {"Content-Type": "application/json",
           "X-Master-Key": ""}
data = {"imageurl": imgurl}
req = requests.put(url, json=data, headers=headers)
print(req.text)
