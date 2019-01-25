import socket
import time


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    @staticmethod
    def _pars_response(data):
        list_data = data.rstrip().split(sep='\n')
        data_dict = {}
        if len(list_data) > 1:
            for line in list_data:
                if line == 'ok':
                    continue
                key, value = Client._pars_response_line(line)
                if key not in data_dict:
                    data_dict[key] = []
                data_dict[key].append(value)
        return data_dict

    @staticmethod
    def _pars_response_line(line):
        key, val1, val2 = line.split()
        value = (int(val2), float(val1))
        return key, value

    def put(self, key, value, timestamp):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            massage = 'put {key} {value} {timestamp}\n'.format(key=key, value=value, timestamp=timestamp)
            sock.sendall(massage.encode("utf8"))
            data = sock.recv(1024).decode("utf8")
            if 'ok' not in data:
                raise ClientError()

    def get(self, key):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            massage = 'get {key}\n'.format(key=key)
            sock.sendall(massage.encode("utf8"))
            data = sock.recv(1024).decode("utf8")
            if 'ok' not in data:
                raise ClientError()
            return self._pars_response(data)


class ClientError(socket.error):

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    client = Client("127.0.0.1", 10001)
    client.put("k1", 0.25, timestamp=1)
    client.put("k1", 2.156, timestamp=2)
