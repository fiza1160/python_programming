import asyncio


class Server:

    def __init__(self, host, port):
        self.storage = {}
        self.host = host
        self.port = port

    async def start(self):
        serv = await asyncio.start_server(self.server, self.host, self.port)
        await serv.serve_forever()

    async def server(self, reader, writer):
        while True:
            request = await reader.read(1000)
            if not request:
                break

            request = request.decode()
            if not self.is_request_valid(request):
                response = 'error\nwrong command\n\n'
            else:
                response = self.get_response(request, self.storage)

            writer.write(response.encode('utf8'))
            await writer.drain()
        writer.close()

    @staticmethod
    def is_request_valid(request):
        if request.startswith('put') or request.startswith('get'):
            return True
        return False

    def get_response(self, request, storage):
        data_request = self.pars_request(request)
        if data_request[0] == 'get':
            response = self.get(data_request, storage)
        elif data_request[0] == 'put':
            response = self.put(data_request, storage)
        return response

    @staticmethod
    def pars_request(request):
        return request.rstrip().split()

    @staticmethod
    def get(data_request, storage):
        key = data_request[1]
        if key == '*':
            response = 'ok'
            for key, value in storage.items():
                for item in value:
                    response += '\n{key} {value} {timestamp}'.format(key=key, value=item[0], timestamp=item[1])
            response += '\n\n'
        else:
            response = 'ok'
            if key in storage:
                value = storage[key]
                for item in value:
                    response += '\n{key} {value} {timestamp}'.format(key=key, value=item[0], timestamp=item[1])
            response += '\n\n'
        return response

    @staticmethod
    def put(data_request, storage):
        try:
            key, val1, val2 = data_request[1], float(data_request[2]), int(float(data_request[3]))
            if key not in storage:
                storage[key] = []

            list_of_values = storage[key]
            if (val1, val2) not in list_of_values:
                storage[key].append((val1, val2))
        except (IndexError, ValueError):
            return 'error\nwrong command\n\n'
        return 'ok\n\n'


def run_server(host, port):
    server = Server(host, port)
    asyncio.run(server.start())

# run_server('127.0.0.1', 10001)
