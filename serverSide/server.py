from http.server import BaseHTTPRequestHandler, HTTPServer



class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        
        return


    def do_POST(self):

        return

def run():
    # this is the current computer address and port number:
    listen = ("127.0.0.1", 8080)
    server = HTTPServer(listen, MyRequestHandler)

    print("Listening...")

    server.serve_forever()

run()