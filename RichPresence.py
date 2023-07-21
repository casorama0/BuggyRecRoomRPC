from recnetlogin import RecNetLogin # I can not stress this enough! This program will not work if you do not have RecNetLogin in the same directory as the program files. MAKE SURE TO PUT THEM IN THE SAME DIRECTORY!!
from pypresence import Presence
import json
import requests
import time
import math
import threading

initialized = False

while not initialized:

    try: 
        with open('accountInfo.json', 'r') as openfile:
            data = json.load(openfile)
    except:
      username = input("Please enter your username: \n")

      try:
        userID = requests.get(f"https://accounts.rec.net/account?username={username}").json()["accountId"]
      except:
        print("Invalid username provided")
        exit()

      data = {"userID": userID}
      data = json.dumps(data)

      with open('accountInfo.json', 'w') as outfile:
        outfile.write(data)
      print("New user data has been written")
    else:
      initialized = True
      print("User file found and loaded")
      user = data["userID"]



rnl = RecNetLogin()
def generate_token():
    global token
    token = None
    expiry = time.time() + 3600
    while not token or time.time() > expiry:
        expiry = time.time()
        token = rnl.get_token(include_bearer = True)
        print("Token refreshed")

thread = threading.Thread(target=generate_token)
thread.start()
thread.join()




client_id = "1124780603200508014"
RPC = Presence(client_id)
RPC.connect()

currentRoom = ""

class Matchmaking:
    def __init__(self, isOn, isF, isP, n, rId, rIT, iip):
        self.isOnline = isOn
        self.isFull = isF
        self.isPrivate = isP
        self.name = n
        self.roomId = rId
        self.roomInstanceType = rIT 
        self.isInProgress = iip

class Room:
    def __init__(self, roomName, roomImage):
        self.name = roomName
        self.image = roomImage

while True:
    try:
        mmdata = requests.get(f"https://match.rec.net/player?id={user}", headers={"Authorization": token}).json()[0]
        instdata = mmdata["roomInstance"]
        mm = Matchmaking(mmdata["isOnline"], instdata["isFull"], instdata["isPrivate"], instdata["name"], instdata["roomId"], instdata["roomInstanceType"], instdata["isInProgress"])
    except:
        raise SystemExit("Failed to gather instance data. Are you logged in to Rec Room?")



    if mm.isPrivate:
        priv = " [PRIVATE]"
    else:
        priv = ""

    if mm.isInProgress:
        isprogress = " [IN PROGRESS]"
    else:
        isprogress = ""

    
        
        
    try:
        requests.get(f"https://rooms.rec.net/rooms/{mm.roomId}").json()["RoomId"]
    except:
        if mm.roomInstanceType == 2:
            rd = Room(mm.name, "a7c4mxpejlasupag1mkdne875.jpg?cropSquare=True")
        else:
            rd = Room("Private Room", "DefaultProfileImage?cropSquare=True")
    else:
        roomData = requests.get(f"https://rooms.rec.net/rooms/{mm.roomId}").json()
        rd = Room(roomData["Name"], roomData["ImageName"])

    
    if currentRoom != rd.name:
        timeOfChange = math.floor(time.time())
        currentRoom = rd.name
    else:
        pass

    
    try:
        RPC.update(state=f"Playing {rd.name}{priv}{isprogress}", large_image=f"https://img.rec.net/{rd.image}", start=timeOfChange)
    except:
        raise SystemExit("Presence update failed. Is Discord still open?")
    else:
        print(f"Updated presence. Room: {rd.name}")


    time.sleep(10)
    
