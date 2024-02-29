import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        if self.path == '/':
            self.path = '/link.html'
        elif self.path == '/update_users':
            self.update_users()
            self.path = '/success.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def update_users(self):
        try:
            with open("Users.txt", "a") as users_file:
                with open("SentEmailToUser.txt", "r") as sent_email_file:
                    lines = sent_email_file.readlines()
                    receivers = lines[0].strip().split(";")[-1]
                    users_file.write(receivers + "\n")
        except Exception as e:
            print("Error writing to Users.txt:", str(e))

def run_server():
    PORT = 80
    Handler = MyHttpRequestHandler
    #IP server
    with socketserver.TCPServer(('00.00.00.00', PORT), Handler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
