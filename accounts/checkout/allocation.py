from decimal import Decimal as D


class Allocations(object):
    '''
    When used with goods, only needs 'code' and 'amount'. Buy different
    products and spend an amount x of funds.
    With assets it needs: exchange, amount. Buy amounts of the asset in
    different exchanges. 
    '''
    def __init__(self):
        self._allocations = {}

    def add(self, code, amount):
        if self.contains(code):
            self._allocations[code] += amount
        else:
            self._allocations[code] = amount

    def remove(self, code):
        if self.contains(code):
            del self._allocations[code]

    @property
    def total(self):
        total = D('0.00')
        for allocation in self._allocations.values():
            total += allocation
        return total

    def contains(self, code):
        return code in self._allocations

    def __len__(self):
        return len(self._allocations)

    def items(self):
        return self._allocations.items()
