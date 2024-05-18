class Item:
    def __init__(self, code, name, quantity, unit_price,
                 discount_name, discount_amount):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.discount_name = discount_name
        self.discount_amount = discount_amount
    
    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'quantity': str(self.quantity),
            'unit_price': str(self.unit_price),
            'discount_name': self.discount_name,
            'discounnt_amount': str(self.discount_amount)
        }