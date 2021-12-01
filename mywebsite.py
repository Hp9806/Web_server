from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html
<head>
<title>Mywebsite</title>
</head>
<body>
<h1>Top five programming language :</h1>
<h2>Javascript</h2>
<h2>Java</h2>
<h2>Ruby</h2>
<h2>Python</h2>
<h2>C++</h2>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8080)
httpd = HTTPServer(server_address,myhandler)
print("my server is running...")
httpd.serve_forever()
