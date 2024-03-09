import json
import sys
sys.path.append("..\\..\\Public\\")

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
        if not isinstance(nfc_data, dict):
            raise ValueError("Invalid NFC data format. Expected dictionary.")

        required_fields = ["amount", "card_number", "expiration_date", "transaction_id"]

        for field in required_fields:
            if field not in nfc_data:
                raise ValueError(f"Missing required field: {field}")

        # สามารถเพิ่มเงื่อนไขตรวจสอบเพิ่มเติมได้ตามความต้องการ
        # เช่น ตรวจสอบรูปแบบของข้อมูล, การตรวจสอบหลายเงื่อนไข, หรือการตรวจสอบรายละเอียดการบัตรเครดิต

        # ตัวอย่างเงื่อนไขตรวจสอบ expiration_date
        expiration_date = nfc_data.get("expiration_date")
        if not expiration_date or not isinstance(expiration_date, str) or len(expiration_date) != 5:
            raise ValueError("Invalid expiration date format. Use MM/YY.")

        # ตัวอย่างเงื่อนไขตรวจสอบ card_number
        card_number = nfc_data.get("card_number")
        if not card_number or not isinstance(card_number, str) or len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Invalid card number format. Use a 16-digit numeric value.")

        # ตัวอย่างเงื่อนไขตรวจสอบ amount
        amount = nfc_data.get("amount")
        if not amount or not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid amount. Amount should be a positive numeric value.")

        # ตรวจสอบเสร็จสิ้น รับรองว่าข้อมูลถูกต้อง
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
   
    
