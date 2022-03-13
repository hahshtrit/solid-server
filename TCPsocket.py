import socketserver
import sys


class MyTCPHandler(socketserver.BaseRequestHandler):
    clients = []

    def handle(self) -> None:
        received_data = self.request.recv(1024)
        client_id = self.client_address[0] + " :is sending data."  # +  self.client_address[1]
        newData = received_data
        # decoded = received_data.decode()

        sys.stdout.flush()
        sys.stderr.flush()

        lengthCalled = 0  # the parsed body content replaces this
        # lengthCalled = parse(newData).length # this will return the body of the content if it exist

        #
        """
        calculates the total bytes that you need to read from the body if it contains:
        """
        while lengthCalled > 0:
            data = self.request.recv(1024)
            newData = newData + data
            # print(len(data), " this is len of buffered data")
            lengthCalled -= len(data)
            sys.stdout.flush()
            sys.stderr.flush()
