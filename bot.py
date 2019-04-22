import requests
import misc
import json


token = misc.token
# https://api.telegram.org/bot817698525:AAG8dyUH78Vs9ljyxa9F1lAhJ3wJeVlpw64/sendmessage?chat_id=416920488&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id': chat_id, 'text': message_text}

    return message

def send_message(chat_id,text='Wait a second, please ...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)



def main():
    #d = get_updates()

    # with open('updates.json','w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['text']
    #if 'к'
    send_message(chat_id, ' What do you want?')






if __name__ == '__main__':
    main()