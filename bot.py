import requests
import misc
from yobit import getFullTrack
from yobit import getTrack
from yobit import waitTrack
from time import sleep


token = misc.token
# https://api.telegram.org/bot817698525:AAG8dyUH78Vs9ljyxa9F1lAhJ3wJeVlpw64/sendmessage?chat_id=416920488&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'

global recent_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    # Отвечать только на новые сообщения
    # Получаем update_id , каждого обновления
    # Записывать переменную, а затем сравнивать с update_id последнего элемента а
    # в списке results

    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id, 'text': message_text}

        return message

    return None

def send_message(chat_id,text='Wait a second, please ...'):
    print(text)
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)



def main():

    while True:
        answer = get_message()

        if answer != None:

            chat_id = answer['chat_id']
            text = answer['text']
            if text == '/help':
                send_message(chat_id,"Чтобы узнать статус своей посылки введите:\n1) /track tracknumber - данная команда выводит последнее изменение в статусе посылки.\n2) /fulltrack tracknumber - данная команда выводит полный статус посылки.\n")
            else:
                text = text.strip()
                spaceNum = text.count(' ')

                if spaceNum == 0 or spaceNum > 1:
                    send_message(chat_id,"Введите команду вместе с трек номером в формате: /command LP00125462391048")
                else:
                    text = text.split()
                    command = text[0]
                    trackNum = text[1]

                    print("Команда: ",text[0],text[1])

                    if len(trackNum) >= 13:
                        if command == '/track':
                            send_message(chat_id, waitTrack(trackNum))
                            send_message(chat_id, getTrack(trackNum))
                        elif command == '/fulltrack':
                            send_message(chat_id, waitTrack(trackNum))
                            send_message(chat_id, getFullTrack(trackNum))
                        else:
                            send_message(chat_id,'Команда введена неправильно!!')
                    else:
                        send_message(chat_id, 'Длина трек номера должна быть не меньше 13 символов!')


        else:
            continue

        sleep(2)



if __name__ == '__main__':
    main()