# Desenvolvido por Kairo Trzeciak
# https://github.com/kairodev
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import SearchRequest
from telethon import functions, types
import dotenv
import os

class auth:

    def __init__(self, api_id, api_hash):

        with TelegramClient(StringSession(), api_id, api_hash) as client:
            session_string = client.session.save()
            os.environ['STRINGSESSION'] = str(session_string)
            dotenv.set_key(dotenv_file, "STRINGSESSION", os.environ["STRINGSESSION"])
            input("Configuration completed successfully, restart the application")

    def verifyEnv(api_id, api_hash):
        
        if len(api_id) <= 0:
            status_id = False
        else:
            status_id = True

        if len(api_hash) <= 0:
            status_hash = False
        else:
            status_hash = True

        if status_id == False and status_hash == False:
            print("You need to configure your API_ID and API_HASH in the .env first, this data can be found at https://my.telegram.org/")
            return False
        elif status_id == False and status_hash == True:
            print("You need to configure your API_ID in the .env first, this data can be found at https://my.telegram.org/")
            return False
        elif status_id == True and status_hash == False:
            print("You need to configure your API_HASH in the .env first, this data can be found at https://my.telegram.org/")
            return False
        else:
            return True




class app:

    def __init__(self, string_session, api_id, api_hash):

        query = input("Search: ")

        with TelegramClient(StringSession(string_session), api_id, api_hash) as client:
            result = client(functions.contacts.SearchRequest(
                q=query,
                limit=100
            ))

            while True:
                try:
                    for grupo in result.chats:
                        print(f'Grupo: {grupo.title} | Participantes: {grupo.participants_count} | @{grupo.username}')
                    break
                except:
                    print("Error")
                    break

            print("The results are few due to telegram not allowing a broad search through its API.")



if __name__ == '__main__':

    print("Starting...")

    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    string_session = os.getenv('STRINGSESSION')

    if auth.verifyEnv(api_id, api_hash) == True:

        if len(string_session) <= 0:
            auth(api_id, api_hash) 
        else:
            app(string_session, api_id, api_hash)
    