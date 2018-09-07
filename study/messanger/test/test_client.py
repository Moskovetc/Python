from socket import *
import json
import time


def parse_response(response):
    """
        Функция разбирает ответ от сервера по коду и выводит текст ответа
        >>> parse_response({'response': 200, 'time': 'Mon Dec 25 23:51:12 2017', 'alert': 'OK'})
        'OK'
    """
    if response['response'] == 200:
        return response['alert']


def client(ip_address, port):
    """
    Функция клиента, создает дескриптор подключения по ip  и  порту,
    при пустом вводе отправляет запрос presense серверу.
    Получает ответ от сервера и выводит текст alert 200.
    """
    current_time = time.ctime()
    message = Action()
    address = (ip_address, port)
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.connect(address)
        while True:
            msg = input('отправить presence сообщение ? ')
            if msg == 'quit':
                break
            if msg == 'yes':
                msg = json.dumps(message.presence(current_time, 'status', 'user', 'online'))
                client_socket.send(msg.encode('ascii'))     # Отправить!
                data = json.loads(client_socket.recv(1024).decode('ascii'))
                print('Ответ:', parse_response(data))


class Action:

    def presence(self, current_time, type_msg, user, status):
        message = {'action': 'presence',
                   'time': current_time,
                   'type': type_msg,
                   'user': {
                       'account_name': user,
                       'status': status
                       }
                   }
        return message

    def probe(self, current_time):
        message = {'action': 'probe',
                   'time': current_time}
        return message

    def msg(self, current_time, to_account, from_account, encoding, msg):
        message = {'action':'msg',
                   'time': current_time,
                   'to': to_account,
                   'from': from_account,
                   'encoding': encoding,
                   'message': msg}
        return message

    def quit(self):
        pass

    def authenticate(self):
        pass

    def join(self, current_time, chat_room):
        message = {'action': 'join',
                   'time': current_time,
                   'room': chat_room}
        return message

    def leave(self, current_time, chat_room):
        message = {'action': 'leave',
                   'time': current_time,
                   'room': chat_room}
        return message


if __name__ == '__main__':
    import doctest
    doctest.testmod()
