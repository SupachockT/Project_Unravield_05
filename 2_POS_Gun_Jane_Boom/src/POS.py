import json
import sys
sys.path.append('C:\Users\yuuki\Documents\GitHub\Project_Unravield_05\Public')

#import Public.NFC_Reader
import NFC_Reader

#100฿ = 1pt

class POSSystem:
    def __init__(self):
        self.nfc_reader = NFCReader()
        
    def process_payment(self):
        try:
            # อ่านข้อมูลจาก NFC Reader
            nfc_data = self.nfc_reader.read_data()

            # ตรวจสอบข้อมูลการชำระเงิน
            if self.validate_payment_data(nfc_data):
                # ทำรายการ
                transaction_result = self.make_transaction(nfc_data)

                # อนุมัติการทำรายการ
                if transaction_result:
                    print("การทำรายการเสร็จสมบูรณ์")
                    self.generate_receipt(nfc_data)
                else:
                    print("การทำรายการไม่สำเร็จ")

        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {str(e)}")
            
    def validate_payment_data(self, nfc_data):
        # ตรวจสอบความถูกต้องของข้อมูลการชำระเงิน
        # สามารถเพิ่มเงื่อนไขตรวจสอบเพิ่มเติมได้ตามความต้องการ
        return True

    def make_transaction(self, nfc_data):
        # ทำรายการลดหรือเพิ่มจำนวนเงินตามข้อมูล NFC
        # สามารถเชื่อมต่อกับระบบบัญชีหรือบริการการชำระเงินอื่น ๆ ได้
        # สมมติว่าทำรายการเสร็จสมบูรณ์ทั้งหมด
        return True

    def generate_receipt(self, nfc_data):
        # สร้างใบเสร็จหรือยืนยันการชำระเงิน
        print(f"สร้างใบเสร็จสำหรับรายการชำระเงินของ {nfc_data['customer_name']}")
        

class NFCReader():
    def read_data():
        reader = NFC_Reader()
        uid = reader.read_uid()
        if uid:
            print("UID:", uid)
        else:
            print("No card detected.")
    
    
