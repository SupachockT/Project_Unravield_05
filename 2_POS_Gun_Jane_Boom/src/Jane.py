import json
import sys
from NFC_Reader import NFC_Reader

# 100฿ = 1pt
POINTS_PER_100_BAHT = 1

class POSSystem:
    def __init__(self):
        self.nfc_reader = NFC_Reader()
        self.money_amount = 0
        self.total = 0
        self.points = 0
        
    def process_payment(self, total):
        self.total = total  # กำหนดยอดรวมที่ต้องจ่าย
        try:
            # อ่านข้อมูลจาก NFC Reader
            nfc_data = self.nfc_reader.read_uid()

            # ตรวจสอบข้อมูลการชำระเงิน
            if self.validate_payment_data(nfc_data):
                # ทำรายการ
                transaction_result = self.make_transaction()

                # อนุมัติการทำรายการ
                if transaction_result:
                    print("การทำรายการเสร็จสมบูรณ์")
                    self.generate_receipt(nfc_data)
                    # คำนวณและเก็บ points
                    self.calculate_and_store_points()
                else:
                    print("การทำรายการไม่สำเร็จ")

        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {str(e)}")

    def validate_payment_data(self, nfc_data):
        if 'money' in nfc_data:
            self.money_amount = nfc_data['money']
            print(f"จำนวนเงินในบัตร: {self.money_amount} บาท")
            return True
        else:
            print("ข้อมูลการชำระเงินไม่ถูกต้อง")
            return False

    def make_transaction(self):
        if self.money_amount >= self.total:
            return True
        else:
            print("เงินในบัตรไม่เพียงพอ")
            return False

    def generate_receipt(self, nfc_data):
    # Extract customer information from NFC data
        customer_name = nfc_data.get('customer_name', 'Unknown Customer')
        transaction_details = {
        'total_amount': self.total,
        'paid_amount': self.money_amount,
        'change': self.money_amount - self.total
    }
        # Generate receipt content
        receipt_content = f"--- Receipt ---\n"
        receipt_content += f"Customer: {customer_name}\n"
        receipt_content += f"Total Amount: {transaction_details['total_amount']} Baht\n"
        receipt_content += f"Paid Amount: {transaction_details['paid_amount']} Baht\n"
        receipt_content += f"Change: {transaction_details['change']} Baht\n"
        receipt_content += f"Thank you for your purchase!"

        print(receipt_content)

def calculate_and_store_points(self):
    # Calculate points based on the money spent
    earned_points = self.money_amount // 100 * POINTS_PER_100_BAHT
    self.points += earned_points
    
    # Print the earned points and total points
    print(f"You have earned {earned_points} points.")
    print(f"Total points: {self.points}")



# สร้างอ็อบเจ็ต POS
pos_system = POSSystem()

# ทดสอบการทำรายการ
total_to_pay = 800  # กำหนดยอดรวมที่ต้องจ่าย
pos_system.process_payment(total_to_pay)
