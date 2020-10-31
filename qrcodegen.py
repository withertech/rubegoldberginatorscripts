import qrcode
from PIL import Image
import io
import requests
import base64
import os
import json
f = open("/root/message.txt", "r")

img = qrcode.make(f.read())
os.remove("/root/message.txt")

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
    print(u['url'])
binurl = "https://api.jsonbin.io/v3/b/5f9dc3253269193b17bfec93
payload = {
	"Content-Type": "application/json"
	"X-Master-key":
}
