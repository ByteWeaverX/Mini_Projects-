from user import User
from expense import Expense


class ExpenseManager:
    def __init__(self):
        self.users = {}  # userid -> User object
        self.expenses = []  # list of Expense objects
        self.balances = {}  # userid -> balance

    def add_user(self, userid, name):
        # Create a User and store by userid
        user = User(userid, name)
        self.users[userid] = user
        self.balances[userid] = 0
        return user

    def add_expense(self, expenseid, description, totalamount, paidby_userid, participant_userids):
        # Validate: paidby must be a valid user
        if paidby_userid not in self.users:
            raise ValueError(f"User {paidby_userid} does not exist")
        
        # Validate: all participants must be valid users
        for userid in participant_userids:
            if userid not in self.users:
                raise ValueError(f"Participant {userid} does not exist")
        
        # Create lists for paidby and participants
        paidby_user = self.users[paidby_userid]
        participants = []
        for userid in participant_userids:
            participants.append(self.users[userid])
        
        # Create and store the expense
        expense = Expense(expenseid, description, totalamount, paidby_user, participants)
        self.expenses.append(expense)
        
        # Update balances
        self.calculate_balances()
        
        return expense

    def calculate_balances(self):
        # Reset all balances to 0
        for userid in self.users:
            self.balances[userid] = 0
        
        # For each expense, update balances
        for expense in self.expenses:
            # Payer adds the full amount to their balance (they paid it)
            payer_userid = expense.paidby.userid
            self.balances[payer_userid] = self.balances[payer_userid] + expense.totalamount
            
            # Each participant subtracts their share
            share_per_person = expense.get_share_per_person()
            for participant in expense.participants:
                participant_userid = participant.userid
                self.balances[participant_userid] = self.balances[participant_userid] - share_per_person

    def show_expenses(self):
        # Display all expenses
        print("\n========== EXPENSES ==========")
        if len(self.expenses) == 0:
            print("No expenses recorded.")
            return
        
        for expense in self.expenses:
            print(f"[{expense.expenseid}] {expense}")

    def show_balances(self):
        # Display calculated balances (debug view)
        print("\n========== RAW BALANCES ==========")
        for userid in self.users:
            user = self.users[userid]
            balance = self.balances[userid]
            print(f"{user.name}: {balance}")

    def show_who_owes_whom(self):
        # Display settlement: who owes whom and how much
        print("\n========== SETTLEMENT ==========")
        
        # Find who is owed money and who owes money
        creditors = []  # (userid, name, amount owed to them)
        debtors = []    # (userid, name, amount they owe)
        
        for userid in self.users:
            user = self.users[userid]
            balance = self.balances[userid]
            if balance > 0:
                creditors.append((userid, user.name, balance))
            elif balance < 0:
                debtors.append((userid, user.name, abs(balance)))
        
        # Match debtors with creditors
        if len(creditors) == 0 and len(debtors) == 0:
            print("All balances are settled!")
            return
        
        # Simple approach: for each debtor, pay off creditors in order
        debtor_idx = 0
        creditor_idx = 0
        
        while debtor_idx < len(debtors) and creditor_idx < len(creditors):
            debtor_userid, debtor_name, debtor_amount = debtors[debtor_idx]
            creditor_userid, creditor_name, creditor_amount = creditors[creditor_idx]
            
            # Amount that debtor owes to this creditor
            settlement_amount = min(debtor_amount, creditor_amount)
            
            print(f"{debtor_name} owes {creditor_name} {settlement_amount}")
            
            # Reduce amounts
            debtors[debtor_idx] = (debtor_userid, debtor_name, debtor_amount - settlement_amount)
            creditors[creditor_idx] = (creditor_userid, creditor_name, creditor_amount - settlement_amount)
            
            # Move to next debtor or creditor if current is settled
            if debtors[debtor_idx][2] == 0:
                debtor_idx += 1
            if creditors[creditor_idx][2] == 0:
                creditor_idx += 1
