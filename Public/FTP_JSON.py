import os

from FTPClient import FTPClient
import JSON_Function as j

fileName = "nisit.json"
fileName2 = "topup_logs.json"
ftp_client = FTPClient("127.0.0.1", user="admin", passwd="")


def is_uid_exists(nisit_data, uid):
    return uid in nisit_data


def is_uid_verify(nisit_data, uid):
    if uid in nisit_data:
        return nisit_data[uid]["isVerify"]
    else:
        return False


def load_return_json():
    ftp_client.download_file(fileName)
    data = j.load_data(fileName)
    return data


def send_json_back_ftp(all_data):
    j.update_data(fileName, all_data)
    ftp_client.upload_file(fileName)
    os.remove(fileName)


def update_topup_logs(uid, timestamp, message):
    ftp_client.download_file(fileName2)
    logs = j.load_data(fileName2)
    if uid in logs:
        logs[uid].append({"timestamp": timestamp, "message": message})
    else:
        logs[uid] = [{"timestamp": timestamp, "message": message}]
    j.update_data(fileName2, logs)
    ftp_client.upload_file(fileName2)
    os.remove(fileName2)


def update_redemption_logs(uid, timestamp, message):
    ftp_client.download_file("redemption_logs.json")
    logs = j.load_data("redemption_logs.json")
    if uid in logs:
        logs[uid].append({"timestamp": timestamp, "message": message})
    else:
        logs[uid] = [{"timestamp": timestamp, "message": message}]
    j.update_data("redemption_logs.json", logs)
    ftp_client.upload_file("redemption_logs.json")
    os.remove("redemption_logs.json")
