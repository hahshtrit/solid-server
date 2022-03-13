import TCPsocket
import json


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

    """
    parseWebKit: takes in the headers from the parse class, and parses the multiform data
                 to find the WebKit id that is sent in the headers
    
    """

    def parseWebKit(self):
        dict = self.headers
        if "Content-Length" in dict:
            type = (dict["Content-Type"])
            if 'multipart/form-data;' in type:
                type2 = type.split("boundary=")
                webStuff = (type2[1])
                webStuff = '--' + webStuff
                return webStuff
        return None

    """
    ParseWebBody: calls the parseWebkit function, and splits the body of the request from the webkit
                  and separates out each section. This is generic so you can use the function and 
                  parse more data in a similar syntax that is being used. It adds all the data in a dictionary
                  and returns it. This only works if the data contains a webkit which is common when sent a post 
                  request.
    """

    def parseWebBody(self):
        webKit = self.parseWebKit()
        semi_delimiter = b'\r\n'
        delimiter = b'\r\n\r\n'

        statements = {}

        if webKit:
            data2 = self.body.split(webKit.encode())

            for i in range(len(data2)):
                if 'Content-Disposition: form-data; name="xsrf_token"'.encode() in data2[i]:
                    current = data2[i]
                    index = current.find(delimiter)
                    header = current[:index]
                    headerIndex = header.find(semi_delimiter)
                    header = header[headerIndex:]
                    content = current[index + len(delimiter):]
                    contentIndex = content.rfind(b'\r\n')
                    content = content[:contentIndex]
                    statements['token'] = content
                    if len(content) == 0:
                        statements['token'] = b'invalid token accessed'

                if 'Content-Disposition: form-data; name="comment"'.encode() in data2[i]:
                    current = data2[i]
                    index = current.find(delimiter)
                    header = current[:index]
                    headerIndex = header.find(semi_delimiter)
                    header = header[headerIndex:]
                    content = current[index + len(delimiter):]
                    contentIndex = content.rfind(b'\r\n')
                    content = content[:contentIndex]
                    statements['comment'] = content

                if 'Content-Disposition: form-data; name="upload"'.encode() in data2[i]:
                    current = data2[i]
                    index = current.find(delimiter)
                    header = current[:index]
                    headerIndex = header.find(semi_delimiter)
                    header = header[headerIndex:]
                    header = header.split(b';')

                    parse1 = (header[2].split(semi_delimiter))

                    fileNameIndex = parse1[0].find(b'=')
                    fileName = ((parse1[0])[fileNameIndex + len(b'='):]).decode()
                    fileName = fileName.replace("/", "")

                    contentTypeIndex = parse1[1].find(b': ')
                    contentType = ((parse1[1])[contentTypeIndex + len(b': '):]).decode()

                    content = current[index + len(delimiter):]
                    contentIndex = content.rfind(semi_delimiter)
                    content = content[:contentIndex]

                    if "image/jpeg" in contentType:
                        if len(content) > 0:
                            statements['bytes'] = content
                            statements['filename'] = fileName
                            statements['contentType'] = contentType

        return statements
