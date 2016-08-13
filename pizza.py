class BaseDominos:
    '''A base class'''
    def __repr__(self):
        return 'Dominos Pizza Inc.'


class Pizza(BaseDominos):
    '''This class takes size and quantity'''
    def __init__(self, size='xyz', quantity=1):
	self.quantity = quantity
	if size == 'small':
		self.size = 1
	elif size == 'regular':
		self.size = 2
	elif size == 'large':
		self.size = 4
	elif size == 'default':
		self.size = 1

    def get_bill(self):
        '''Final amount'''
        return 124*self.size*self.quantity

