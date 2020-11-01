import requests
import json
import subprocess
from discord_webhook import DiscordWebhook

url = 'https://api.jsonbin.io/b/5f9dc3253269193b17bfec93/latest'
headers = {'secret-key': '$2b$10$ihoA/Dnxdha4mErdATrtQe8HF5nPG44ZKDL2ZVheKgbHeL9aW./QG'}

req = requests.get(url, headers=headers)
t = req.text
y = json.loads(t)

response = requests.get(y['imageurl'])

file = open("image.png", "wb")
file.write(response.content)
file.close()
result = subprocess.run(['qrscanner',"image.png" ], stdout=subprocess.PIPE)
webhook = DiscordWebhook(url='', content=result.stdout.decode('utf-8'))
webhook.execute()





