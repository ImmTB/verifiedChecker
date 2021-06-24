'python PY/thing.py'
import ctypes, requests
from threading import Thread
userid = input("Player's UserId: ")
userid = int(userid)
assetid = 102611803
r = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/items/asset/{assetid}').json()['data']
if r:
  print("Verified")
  verified = True
else:
  print("Not Verified")
  verified = False