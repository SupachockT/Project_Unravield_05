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

    def read_uid(self):
        self.nfc_reader = NFC_Reader()
        return self.nfc_reader.read_uid()

    def process_payment(self, total):
        self.total = total  # กำหนดยอดรวมที่ต้องจ่าย
        receipt = None
        points = None
        try:
            nfc_data = self.nfc_reader.read_uid()

            # ตรวจสอบข้อมูลการชำระเงิน
            if self.validate_payment_data(nfc_data):
                transaction_result = self.make_transaction()

                # อนุมัติการทำรายการ
                if transaction_result:
                    receipt = self.generate_receipt(nfc_data)
                    # คำนวณและเก็บ points
                    point = self.calculate_and_store_points()
                else:
                    return None

        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {str(e)}")

        return receipt, points

    def validate_payment_data(self, nfc_data):
        if "money" in nfc_data:
            self.money_amount = nfc_data["money"]
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

    def generate_receipt(self, uid, total, nisit_code, fname, lname, timedate):
        customer_name = fname + " " + lname + " " + nisit_code
        transaction_details = {
            "total_amount": total,
        }
        receive_points = self.calculate_points(total)
        # Generate receipt content
        receipt_content = f"--- Receipt ---\n"
        receipt_content += f"Customer: {customer_name}\n"
        receipt_content += f"Total Amount: {transaction_details['total_amount']} Baht\n"
        receipt_content += f"received points: {receive_points} \n"
        receipt_content += f"time stamps: {timedate} \n"
        receipt_content += f"Thank you for your purchase!"

        return receipt_content

    def set_money_and_points(self, nfc_data):
        if "money" in nfc_data:
            self.money_amount = nfc_data["money"]
            print(f"Money in card: {self.money_amount} Baht")
        if "points" in nfc_data:
            self.points = nfc_data["points"]
            print(f"Points in card: {self.points}")

    def calculate_points(self, money):
        # Calculate points based on the money spent
        earned_points = money // 100 * POINTS_PER_100_BAHT
        return earned_points


# สร้างอ็อบเจ็ต POS
# pos_system = POSSystem()

# ทดสอบการทำรายการ
# total_to_pay = 800  # กำหนดยอดรวมที่ต้องจ่าย
# pos_system.process_payment(total_to_pay)
