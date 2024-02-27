from smartcard.scard import *
from smartcard.util import toHexString
import time

class NFC_Reader:
    def __init__(self):
        self.hresult, self.hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
        if self.hresult != SCARD_S_SUCCESS:
            raise Exception('Failed to establish context:', SCardGetErrorMessage(self.hresult))

        self.hresult, self.readers = SCardListReaders(self.hcontext, [])
        if self.hresult != SCARD_S_SUCCESS:
            raise Exception('Failed to list readers:', SCardGetErrorMessage(self.hresult))
        if len(self.readers) == 0:
            raise Exception('No smart card readers found.')
        self.reader = self.readers[0]
        print("Found reader:", self.reader)
        
        try:
            self.hresult, self.hcard, self.dwActiveProtocol = SCardConnect(
                self.hcontext,
                self.reader,
                SCARD_SHARE_SHARED,
                SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)
            if self.hresult != SCARD_S_SUCCESS:
                raise Exception('Failed to connect to reader:', SCardGetErrorMessage(self.hresult))
        except Exception as e:
            print("Failed to connect to reader:", e)
            self.hcard = None

    def read_uid(self):
        if self.hcard is None:
            print("No card reader available.")
            return None
        
        command = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        try:
            response, value = self.send_command(command)
            uid = toHexString(response[:-2], format=0)
            return uid
        except Exception as e:
            print("Failed to read UID:", e)
            return None

    def send_command(self, command):
        hresult, response = SCardTransmit(self.hcard, self.dwActiveProtocol, command)
        if hresult != SCARD_S_SUCCESS:
            raise Exception('Failed to send command:', SCardGetErrorMessage(hresult))
        return response, toHexString(response, format=0)

if __name__ == '__main__':
    reader = NFC_Reader()
    uid = reader.read_uid()
    if uid:
        print("UID:", uid)
    else:
        print("No card detected.")
