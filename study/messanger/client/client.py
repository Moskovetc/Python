import json
from socket import *
from modules.options import get_options
from logger.log_config import *


@log
def parse_response(response):
    log.debug('start function')
    if response['response'] == 200:
        log.info('Send message {}'.format(response['alert']))
        return response['alert']


@log
def client(ip_address, port):
    log.debug('start function')
    current_time = time.ctime()
    message = Action()
    address = (ip_address, int(port))
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.connect(address)
        while True:
            msg = input('отправить presence сообщение ? ')
            if msg == 'quit':
                break
            msg = json.dumps(message.presence(current_time, 'status', 'user', 'online'))
            client_socket.send(msg.encode('ascii'))
            data = json.loads(client_socket.recv(1024).decode('ascii'))
            print('Ответ:', parse_response(data))


class Action:

    @log
    def presence(self, current_time, type_msg, user, status):
        log.debug('start function')
        message = {'action': 'presence',
                   'time': current_time,
                   'type': type_msg,
                   'user': {
                       'account_name': user,
                       'status': status
                       }
                   }
        log.info('send presence message {}'.format(message))
        return message

    @log
    def probe(self, current_time):
        log.debug('start function')
        message = {'action': 'probe',
                   'time': current_time}
        log.info('send probe message {}'.format(message))
        return message

    @log
    def msg(self, current_time, to_account, from_account, encoding, msg):
        log.debug('start function')
        message = {'action':'msg',
                   'time': current_time,
                   'to': to_account,
                   'from': from_account,
                   'encoding': encoding,
                   'message': msg}
        log.info('send msg message {}'.format(message))
        return message

    @log
    def quit(self):
        pass

    @log
    def authenticate(self):
        pass

    @log
    def join(self, current_time, chat_room):
        log.debug('start function')
        message = {'action': 'join',
                   'time': current_time,
                   'room': chat_room}
        log.info('send join message {}'.format(message))
        return message

    @log
    def leave(self, current_time, chat_room):
        log.debug('start function')
        message = {'action': 'leave',
                   'time': current_time,
                   'room': chat_room}
        log.info('send leave message {}'.format(message))
        return message


if __name__ == "__main__":
    log = logger()
    ipv4_address, port = get_options(sys.argv)
    client(ipv4_address, port)
