class BaseDominos(object):
    '''A base class'''
    def __init__(self):
	
        self.pizza_size = dict(
			small=1,
			regular=2,
			large=4,
			default=1)

    def __repr__(self):
        return 'Dominos Pizza Inc.'


class Pizza(BaseDominos):
    '''This class takes size and quantity'''
    def __init__(self, size='default', quantity=1):
        super(Pizza, self).__init__()
        self.quantity = quantity
        self.size = size

    def get_bill(self):
        '''Final amount'''
        return 124*self.pizza_size[self.size]*self.quantity

