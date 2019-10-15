
class DataItem(object):
    def __init__(self, share_id, currency_date, dividend_amount):
        self.share_id = share_id
        self.currency_date = currency_date
        self.dividend_amount = dividend_amount

class DataItemTaxPaid(DataItem):
    def __init__(self, share_id, currency_date, dividend_amount, tax_paid):
        super().__init__(share_id, currency_date, dividend_amount)
        self.tax_paid = tax_paid

class DataItemTaxDue(DataItem):
    def __init__(self, share_id, currency_date, dividend_amount, currency_rate):
        super().__init__(share_id, currency_date, dividend_amount)
        self.currency_rate = currency_rate

    def get_tax_due(self):
        return self.dividend_amount * 0.19 * self.currency_rate

    def __repr__(self):
        return f"Id {self.share_id} rate = {self.currency_rate} due amount = {self.get_tax_due()}"

    def __str__(self):
        return f"To ja {self.share_id} senior radio anchor"
