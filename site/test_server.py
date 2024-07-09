from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, directory="dist", **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path += "index"
        if "." not in self.path:
            self.path += ".html"

        SimpleHTTPRequestHandler.do_GET(self)

with HTTPServer(("", 8000), MyHandler) as server:
    server.serve_forever()
