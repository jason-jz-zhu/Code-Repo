


import unittest
from dataclasses import dataclass

TRANSFER_EXP_MS = 24 * 60 * 60 * 1000  # 86400000

@dataclass
class TransferS:
    source: str
    target: str
    amount: int
    expired_at: int
    status: str



class TransferStatus:
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    EXPIRED = "Expired"
    FAILED = "Failed"


class bank_system:

    def __init__(self):
        """init"""
        self.balances = {}
        self.transcations = {}
        self.transfer_id = 1
        self.activities = {}

    def check_amount(self, amount):
        try:
            amount = int(amount)
            if amount < 0:
                return None
            return amount
        except (ValueError, TypeError):
            return None

    def create_account(self, timestamp, account_id):
        if account_id in self.balances:
            return "false"
        self.balances[account_id] = 0
        self.activities[account_id] = 0
        return "true"
    
    def deposit(self, timestamp, account_id, amount):
        """
        goal:
        Args:

        Return:
        """
        if account_id not in self.balances:
            return ""
        amount = self.check_amount(amount)
        if amount is None:
            return ""

        self.balances[account_id] += amount
        self.activities[account_id] += amount
        return str(self.balances[account_id])
    
    def pay(self, timestamp, account_id, amount):
        """
        goal:
        Args:

        Return:
        """
        if account_id not in self.balances:
            return ""
        amount = self.check_amount(amount)
        if amount is None:
            return ""
        if self.balances[account_id] < amount:
            return ""
        self.balances[account_id] -= amount
        self.activities[account_id] += amount
        return str(self.balances[account_id])
    
    def transfer(self, timestamp, source_id, target_id, amount):
        """
        goal:
        Args:

        Return:
        """
        amount = self.check_amount(amount)
        if amount is None:
            return ""
        if source_id == target_id:
            return ""
        if source_id not in self.balances or target_id not in self.balances:
            return ""
        if self.balances[source_id] < amount:
            return ""
        
        id = f"transfer{self.transfer_id}"
        self.transfer_id += 1
        self.balances[source_id] -= amount
        self.activities[source_id] += amount
        self.transcations[id] = TransferS(
            source=source_id,
            target=target_id,
            amount=amount,
            expired_at=int(timestamp) + TRANSFER_EXP_MS,
            status=TransferStatus.PENDING
        )
        

        return id
    

    def accept_transfer(self, timestamp, account_id, transfer_id):
        """
        goal:
        Args:

        Return:
        """
        if transfer_id not in self.transcations:
            return "false"
        transfer = self.transcations[transfer_id]
        if transfer.target != account_id:
            return "false"
        if transfer.status == TransferStatus.ACCEPTED:
            return "false"
        if int(timestamp) > transfer.expired_at:
            self.balances[transfer.source] += transfer.amount  # refund
            self.activities[transfer.source] -= transfer.amount
            transfer.status = TransferStatus.EXPIRED
            return "false"
        
        self.balances[account_id] += transfer.amount
        self.activities[account_id] += transfer.amount
        transfer.status = TransferStatus.ACCEPTED
        return "true"
    
    def top_activity(self, timestamp, n):
        n = int(n)

        sorted_activity = sorted(self.activities.items(), key=lambda x: (-x[1], x[0]))
        print(sorted_activity)
        result = " ".join([f"{id}({am})," for id, am in sorted_activity[:n]])
        return result[:-1]




class test_bank_system(unittest.TestCase):
    def setUp(self) -> None:
        self.bs = bank_system()

    def test_level1(self):
        self.assertEqual(self.bs.create_account("1", "account1"), "true")
        self.assertEqual(self.bs.create_account("2", "account1"), "false")
        self.assertEqual(self.bs.create_account("3", "account2"), "true")
        self.assertEqual(self.bs.deposit("4", "non-existing", ""), "")
        self.assertEqual(self.bs.deposit("5", "account1", "2700"), "2700")
        self.assertEqual(self.bs.pay("6", "non-existing", "2700"), "")
        self.assertEqual(self.bs.pay("7", "account1", "2701"), "")
        self.assertEqual(self.bs.pay("8", "account1", "200"), "2500")

        self.assertEqual(self.bs.pay("9", "account1", "abs"), "")
        self.assertEqual(self.bs.pay("9", "account1", "-100"), "")


    def test_level2(self):
        self.assertEqual(self.bs.create_account("1", "account1"), "true")
        self.assertEqual(self.bs.create_account("2", "account2"), "true")
        self.assertEqual(self.bs.deposit("4", "account1", "2000"), "2000")
        self.assertEqual(self.bs.deposit("5", "account2", "3000"), "3000")
        self.assertEqual(self.bs.transfer("6", "account1", "account2", "5000"), "")
        self.assertEqual(self.bs.transfer("7", "account1", "account2", "1000"), "transfer1")

        self.assertEqual(self.bs.accept_transfer("20", "account1", "transfer1"), "false")
        self.assertEqual(self.bs.accept_transfer("21", "non-existing", "transfer1"), "false")
        self.assertEqual(self.bs.accept_transfer("22", "account1", "transfer2"), "false")
        self.assertEqual(self.bs.accept_transfer("25", "account2", "transfer1"), "true")
        self.assertEqual(self.bs.accept_transfer("30", "account2", "transfer1"), "false")

        self.assertEqual(self.bs.transfer("40", "account1", "account2", "1000"), "transfer2")
        
    # test top_activity 
    def test_top_level3(self):
        self.assertEqual(self.bs.create_account("1", "account1"), "true")
        self.assertEqual(self.bs.create_account("2", "account2"), "true")
        self.assertEqual(self.bs.create_account("3", "account3"), "true")
        self.assertEqual(self.bs.deposit("3", "account1", "2000"), "2000")
        self.assertEqual(self.bs.deposit("4", "account2", "3000"), "3000")
        self.assertEqual(self.bs.deposit("5", "account3", "4000"), "4000")
        self.assertEqual(self.bs.top_activity("7", "3"), "account3(4000), account2(3000), account1(2000)")
        self.assertEqual(self.bs.pay("8", "account1", "1500"), "500")
        self.assertEqual(self.bs.pay("9", "account2", "250"), "2750")
        self.assertEqual(self.bs.deposit("10", "account3", "250"), "4250")
        self.assertEqual(self.bs.top_activity("11", "3"), "account3(4250), account1(3500), account2(3250)")






if __name__ == "__main__":
    unittest.main()