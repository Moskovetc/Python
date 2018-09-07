import json
import select
from socket import *
from logger.log_config import *
from modules.options import get_options


@log
def server_init(ip_address, port, count_conn, time_out):
    log.debug('start function')
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((ip_address, port))
    server_socket.listen(count_conn)
    server_socket.settimeout(time_out)
    log.info('Server socket start')
    return server_socket


@log
def alert(code, current_time):
    log.debug('start function')
    codes = {100: 'notification',
             101: 'major notification',
             200: 'OK',
             201: 'object created',
             202: 'accepted'}
    message = {'response': code,
               'time': current_time,
               'alert': codes[code]}
    log.info('send alert message {}'.format(message))
    return message


@log
def error(code, current_time):
    log.debug('start function')
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
    log.info('send error message {}'.format(message))
    return message


@log
def read(r_clients, all_clients):
    log.debug('start function')
    responses = {}
    for sock in r_clients:
        try:
            data = json.loads(sock.recv(1024).decode('ascii'))
            responses[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    log.info('Read responses from clients {}'.format(responses))
    return responses


@log
def send(requests, w_clients, all_clients):
    log.debug('start function')
    for sock in w_clients:
        if sock in requests:
            try:
                response = json.dumps(parse_request(requests[sock]))
                sock.send(response.encode('ascii'))
            except:
                log.info('client {} {} was disconnected'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


@log
def parse_request(request):
    log.debug('start function')
    if request['action'] == 'presence':
        log.info('send alert message {}'.format(alert(200, time.ctime())))
        return alert(200, time.ctime())


@log
def server_start(ipv4_address, port):
    log.debug('start function')
    clients = []
    server_socket = server_init(ipv4_address, port, 50, 0.2)
    print('Сервер запущен, ip {} port {}'.format(ipv4_address,port))
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


if __name__ == "__main__":
    log = logger()
    ipv4_address, port = get_options(sys.argv)
    server_start(ipv4_address, port)
