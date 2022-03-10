import TCPsocket
import json

#need to add more parse for webbody and things
def split_request(request):
    first_new_line = request.find(parse.new_line)
    blank_line = request.find(parse.blank_line)

    request_line = request[:first_new_line]
    headersBytes = request[(first_new_line + len(parse.new_line)): blank_line]
    body = request[(blank_line + len(parse.blank_line)):]
    return [request_line, headersBytes, body]


def parse_request_line(request_line):
    return request_line.decode().split(' ')


def parse_headers(headers_raw):
    headers = {}
    linesString = headers_raw.decode().split(parse.new_line.decode())
    for line in linesString:
        splits = line.split(":")
        headers[splits[0].strip()] = splits[1].strip()
    return headers


class parse:
    new_line = b'\r\n'
    blank_line = b'\r\n\r\n'

    def __init__(self, request: bytes):
        [request_line, headersBytes, self.body] = split_request(request)
        [self.method, self.path, self.http_version] = parse_request_line(request_line)
        self.headers = parse_headers(headersBytes)

