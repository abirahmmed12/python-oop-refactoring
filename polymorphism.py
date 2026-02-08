class Payment:
    def process_payment(self,amount):
        print(f"processing Bkash payment of {amount} taka")


class Bkash(Payment):
    def process_payment(self, amount):
        print(f"Processing Bkash payment of {amount} taka. SMS notification sent!")

class Card(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of {amount}taka. 2% tax applied!")

payment_bkash=Bkash()
payment_card=Card()

payment_card.process_payment(500)
payment_bkash.process_payment(500)




