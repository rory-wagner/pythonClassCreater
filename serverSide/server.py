from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import jsonToCpp
import jsonToPython
import jsonToPyDict
import json
import os

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
        if self.path == "/python":
            #send the link to the file here.
            self.send200()
            self.sendBackFile("python")
            self.end_headers()
        elif self.path == "/c++":
            self.send200()
            self.sendBackFile("c++")
            self.end_headers()
        else:
            self.send404()
        return

    def do_POST(self):
        print("someone trying to post.")
        data, className, fileName = self.getProperFormOfData()
        if self.path == "/python" or self.path.startswith("/python/"):
            self.createPythonFile(data, className, fileName)
            self.send201()
            self.end_headers()
        elif self.path == "/c++" or self.path.startswith("/python/"):
            self.createCppFile(data, className, fileName)
            self.send201()
            self.end_headers()
        else:
            self.send404()
        return

    def send201(self):
        self.send_response(201)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "text/html")

    def send200(self):
        print("I am sending 200")
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "text/html")
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
        fileName = parsedBody["fileName"][0]
        className = parsedBody["className"][0]
        print(fileName)
        print(className)

        print(type(data))
        data = json.loads(data)
        print("Final form of data:", data)
        return data, className, fileName

    def createPythonFile(self, data, className, fileName):
        if className == "null" and fileName == "null":
            jsonToPython.parseTheData(data)
        else:
            jsonToPython.parseTheData(data, className, fileName)
        return

    def createCppFile(self, data, className, fileName):
        if className == "null" and fileName == "null":
            jsonToCpp.parseTheData(data)
        else:
            jsonToCpp.parseTheData(data, className, fileName)
        return

    def sendBackFile(self, languageName):
        parts = self.path.split("/")
        retrieveFileName = parts[2]

        if languageName == "python":

            filename = os.path.abspath(retrieveFileName)
            print(filename, type(filename))
            self.wfile.write(bytes(json.dumps(filename), "utf-8"))
        # reply_body = 'Saved "%s"\n' % filename
        # self.wfile.write(reply_body.encode('utf-8'))
        return


def run():
    # this is the current computer address and port number:
    listen = ("127.0.0.1", 8080)
    server = HTTPServer(listen, MyRequestHandler)

    print("Listening...")

    server.serve_forever()

run()

