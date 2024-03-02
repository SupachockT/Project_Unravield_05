from ftplib import FTP


class FTPClient:
    def __init__(self, host, user="", passwd=""):
        self.ftp = FTP(host)
        self.ftp.login(user=user, passwd=passwd)

    def List(self):
        self.ftp.retrlines("LIST")

    def upload_file(self, filename):
        self.ftp.storbinary("STOR " + filename, open(filename, "rb"))

    def download_file(self, filename):
        localfile = open(filename, "wb")
        self.ftp.retrbinary("RETR " + filename, localfile.write, 1024)
        localfile.close()

    def create_directory(self, directory_name):
        self.ftp.mkd(directory_name)

    def delete_directory(self, directory_name):
        self.ftp.rmd(directory_name)

    def change_directory(self, directory_name):
        try:
            self.ftp.cwd(directory_name)
            print("Changed directory to:", directory_name)
        except Exception as e:
            print("Failed to change directory:", e)

    def look_directory(self):
        print("Current directory:", self.ftp.pwd())

    def directory_exists(self, directory_name):
        try:
            self.ftp.cwd(directory_name)
            return True
        except:
            self.ftp.mkd(directory_name)
            return False
