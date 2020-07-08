import socketserver

class EchoHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print("connected from: ", self.client_address)
        while True:
            recv_data = self.request.recv(1024)
            if not recv_data:
                break
            self.request.sendall(recv_data)

        print("Disconnected from: ", self.client_address)


class Server(socketserver.ForkingTCPServer):
    max_children = 2000
    daemon_threads = True
    allow_reuse_address = True

with socketserver.ForkingTCPServer(("", 4424), EchoHandle) as server:
    server.serve_forever()


