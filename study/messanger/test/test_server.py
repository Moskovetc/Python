from socket import *
import time
import select
import json
import unittest

def server_init(ip_address, port, count_conn, time_out):
    """
    Инициализация сервера, возвращает дескриптор подключения
    """
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((ip_address, port))
    server_socket.listen(count_conn)
    server_socket.settimeout(time_out)
    return server_socket


def alert(code, current_time):
    codes = {100: 'notification',
             101: 'major notification',
             200: 'OK',
             201: 'object created',
             202: 'accepted'}
    message = {'response': code,
               'time': current_time,
               'alert': codes[code]}
    return message


def error(code, current_time):
    codes = {400: 'wrong request/JSON-object',
             401: 'not authorized',
             402: 'wrong login/password',
             403: 'user is locked',
             404: 'user not found',
             409: 'login already authorized',
             410: 'user offline',
             500: 'server failure'}
    message = {'response': code,
               'time': current_time,
               'error': codes[code]}
    return message


def read(r_clients, all_clients):
    '''
    read requests from clients
    '''
    responses = {}
    for sock in r_clients:
        try:
            data = json.loads(sock.recv(1024).decode('ascii'))
            responses[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    return responses


def send(requests, w_clients, all_clients):
    '''
    Send message to clients
    '''
    for sock in w_clients:
        if sock in requests:
            try:
                response = json.dumps(parse_request(requests[sock]))
                sock.send(response.encode('ascii'))
            except:  # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


def parse_request(request):
    """
    Разбирает запрос и возвращает ответ
    """
    if request['action'] == 'presence':
        return alert(200, time.ctime())


def server_start():
    clients = []
    server_socket = server_init('', 4040, 50, 0.2)
    while True:
        try:
            client, address = server_socket.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение от {}".format(str(address)))
            clients.append(client)
        finally:
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read(r, clients)  # Сохраним запросы клиентов
            send(requests, w, clients)  # Выполним отправку ответов клиентам


class TestSplitFunction(unittest.TestCase):

    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def testsimplestring(self):
        msg = alert(200, 'Tue Dec 26 00:37:31 2017')
        self.assertEqual(msg, {'response': 200, 'time': 'Tue Dec 26 00:37:31 2017', 'alert': 'OK'})
        msg = error(400, 'Tue Dec 26 00:37:31 2017')
        self.assertEqual(msg, {'response': 400, 'time': 'Tue Dec 26 00:37:31 2017',
                               'error': 'wrong request/JSON-object'})
        self.assertEqual(parse_request({'action': 'presence', 'time': time.ctime(), 'type': 'status',
                       'user': {'account_name': 'user', 'status': 'online'}}), {'response': 200,
                                                                               'time': time.ctime(), 'alert': 'OK'})

    def testtypeconvert(self):
        msg = alert(200, 'Tue Dec 26 00:37:31 2017')
        self.assertEqual(msg, {'response': 200, 'time': 'Tue Dec 26 00:37:31 2017', 'alert': 'OK'})
        msg = error(400, 'Tue Dec 26 00:37:31 2017')
        self.assertEqual(msg, {'response': 400, 'time': 'Tue Dec 26 00:37:31 2017',
                               'error': 'wrong request/JSON-object'})
    def testdelimiter(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    unittest.main()
