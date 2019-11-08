from http.server import BaseHTTPRequestHandler, HTTPServer
import parseTheJSON
import jsonToPyDict

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.createPythonFile()
        return

    def do_GET(self):
        if self.path == "/files":
            pass
        else:
            self.send404()
        return

    def do_POST(self):
        if self.path == "/files":
            self.createPythonFile()
            self.send200()
        else:
            self.send404()
        return

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
        parseTheJSON.parseTheData(jsonObject)


def run():
    # this is the current computer address and port number:
    listen = ("127.0.0.1", 8080)
    server = HTTPServer(listen, MyRequestHandler)

    print("Listening...")

    server.serve_forever()

run()