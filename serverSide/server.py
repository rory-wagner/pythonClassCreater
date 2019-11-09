from http.server import BaseHTTPRequestHandler, HTTPServer
import jsonToPython
import jsonToPyDict
import json

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("someone trying to get.")
        if self.path == "/files":
            #send the link to the file here.
            self.send200()
        else:
            self.send404()
        return

    def do_POST(self):
        if self.path == "/python":
            self.createPythonFile()
            self.send201()
        elif self.path == "/c++":
            self.createCppFile()
            self.send201()
        else:
            self.send404()
        return

    def send201(self):
        self.send_response(201)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def send200(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        return

    def send404(self):
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Not Found", "utf-8"))
        return

    def createPythonFile(self):
        jsonObject = jsonToPyDict.jsonToPyDict("object.json")
        jsonToPython.parseTheData(jsonObject)

    def createCppFile(self):

        return


def run():
    # this is the current computer address and port number:
    listen = ("127.0.0.1", 8080)
    server = HTTPServer(listen, MyRequestHandler)

    print("Listening...")

    server.serve_forever()

run()