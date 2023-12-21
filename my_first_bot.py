import config
import requests
import time


offset = -2
counter = 0
chat_id: int


while counter < config.MAX_COUNTER:
    print('attempt =', counter)
    updates = requests.get(f'{config.API_URL}{config.BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{config.API_URL}{config.BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={config.TEXT}')
    time.sleep(1)
    counter += 1
print('!!!!!!!!!!!!!!!!!!!!!!!!!!')