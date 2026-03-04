class Expense:
    def __init__(self, expenseid, description, totalamount, paidby, participants):
        self.expenseid = expenseid
        self.description = description
        self.totalamount = totalamount
        self.paidby = paidby
        self.participants = participants

    def get_share_per_person(self):
        # Equal split: total amount divided equally among all participants
        number_of_participants = len(self.participants)
        if number_of_participants == 0:
            return 0
        share = self.totalamount / number_of_participants
        return share

    def __str__(self):
        payer_name = self.paidby.name
        return f"{self.description} - {self.totalamount} paid by {payer_name}"
