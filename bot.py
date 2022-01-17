from dotenv import load_dotenv  
import os
load_dotenv()

secret_code = os.getenv('BOTSECURETOKEN');
chat_id_env = os.getenv('CHATID');

basicLink = "https://api.telegram.org/bot<token>/METHOD_NAME"

getUpdateLink = "https://api.telegram.org/" + secret_code + "/getUpdates";


sendMessageLink = "https://api.telegram.org/" + secret_code+ "/sendMessage\?chat_id\="  + chat_id_env +"\&text=<enter_text>"
