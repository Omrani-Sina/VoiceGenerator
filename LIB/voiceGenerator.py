#---------------<SINA OMRANI>-----------------
#----GitHub: https://github.com/Omrani-Sina---
#--------------Voice Generator----------------

import requests
from requests_oauthlib import OAuth1 
from urllib.request import urlopen
import json
from playsound import playsound
import urllib.request
#-------------Use library python-------------
       
def speak(text,model):
    url = "https://ttsmp3.com/makemp3_new.php"
    data_url ={"msg": text , "lang":model , "source": "ttsmp3"}
    status_post = requests.post(url,data_url)
    #-----------Send post requests-------------
    data = (status_post._content).decode("utf-8") 
    obj = json.loads(data)
    link = (str(obj['URL']))
    #--Separate the link from the rest of the information--
    mp3file = urlopen(link)
    with open('voice.mp3','wb') as output:
        output.write(mp3file.read())
    #---------Create file voice.mp3-----------
    playsound("voice.mp3",True)
    #------------Play voice.mp3---------------


#---END :)