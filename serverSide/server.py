from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import jsonToPython
import jsonToPyDict
import json

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Content-Length")
        self.end_headers()
        return

    def do_GET(self):
        print("someone trying to get.")
        if self.path == "/files":
            #send the link to the file here.
            self.send200()
        else:
            self.send404()
        return

    def do_POST(self):
        print("someone trying to post.")
        data = self.getProperFormOfData()
        if self.path == "/python":
            self.createPythonFile(data)
            self.send201()
        elif self.path == "/c++":
            self.createCppFile(data)
            self.send201()
        else:
            self.send404()
        return

    def send201(self):
        self.send_response(201)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def send200(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        return

    def send404(self):
        self.send_response(404)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Not Found", "utf-8"))
        return

    def getProperFormOfData(self):
        print(self.headers)
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode("utf-8")
        print(body)
        parsedBody = parse_qs(body)
        print("Parsed Body:", parsedBody)
        data = parsedBody["jsonData"][0]
        print("Final form of data:", data)
        fout = open("other.json", 'w')
        fout.write(data)
        print(type(data))
        data = dict(data)
        print(data)
        return data

    def createPythonFile(self, data):
        jsonToPython.parseTheData(data)
        return

    def createCppFile(self, data):

        return


def run():
    # this is the current computer address and port number:
    listen = ("127.0.0.1", 8080)
    server = HTTPServer(listen, MyRequestHandler)

    print("Listening...")

    server.serve_forever()

run()