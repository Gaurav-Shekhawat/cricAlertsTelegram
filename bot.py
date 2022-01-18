from urllib import response
from dotenv import load_dotenv  
import requests
import os
import time
load_dotenv()

secret_code = os.getenv('BOTSECURETOKEN');
chat_id_env = os.getenv('CHATID');

basicLink = "https://api.telegram.org/bot<token>/METHOD_NAME"

getUpdateLink = "https://api.telegram.org/bot" + secret_code + "/getUpdates";


starttime = time.time()

lastmessage = ""

response = {};

while True:
    from app import getText
    finalOutput = getText()
    print("lastmessage= " + lastmessage)
    print("finalOUtput= " + finalOutput)
    sendMessageLink = "https://api.telegram.org/bot" + str(secret_code)+ "/sendMessage?chat_id="  + str(chat_id_env) +"&text=" + str(finalOutput)

    if lastmessage != finalOutput:
        response = requests.get(sendMessageLink)
        lastmessage = finalOutput
    time.sleep(2.0 - ((time.time() - starttime) % 2.0))


print(responsefinalest.json())