import sys
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs, unquote

sys.path.append("..\\..\\Public\\")

import JSON_Function as j
from FTPClient import FTPClient

ftp_client = FTPClient("127.0.0.1", user="admin", passwd="")


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        # navigate user ไปสู่ success.html
        if self.path == "/success.html":
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

        # รับ UID มาใช้ในการอัพเดทฐานข้อมูล
        elif self.path.startswith("/?uid="):
            query_components = parse_qs(urlparse(self.path).query)
            uid = query_components.get("uid", [""])[0]
            decoded_uid = unquote(uid)
            self.update_users(decoded_uid)
            self.send_response(302)
            self.send_header("Location", "/success.html")
            self.end_headers()
            return

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def update_users(self, uid):
        ftp_client.download_file("nisit.json")
        all_nisit_data = j.load_data("nisit.json")

        print("UID:", uid)

        # Check if the UID exists in the data
        if uid in all_nisit_data:
            # Update the isVerify field to True
            all_nisit_data[uid]["isVerify"] = True
            # Save the updated data back to the file
            j.update_data("nisit.json", all_nisit_data)
            ftp_client.upload_file("nisit.json")
            print("isVerify updated to True for UID:", uid)
        else:
            print("UID not found in the data")


def run_server():
    PORT = 80
    Handler = MyHttpRequestHandler
    with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
