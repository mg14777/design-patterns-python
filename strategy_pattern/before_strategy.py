from enum import Enum

'''
Issues with this code:
	* Order should be about who is ordering what. Adding the shipper violates Single Responsibility.
	* Shipping cost is open for modification since adding a new shipper requires changing the
	  shipping cost class (if/elif) instead of just adding new code. Violates OCP.
'''


class Shipper(Enum):
	FEDEX  = 0
	UPS    = 1
	POSTAL = 2


class Order(object):
	def __init__(self, shipper):
		self._shipper = shipper

	@property
	def shipper(self):
		return self._shipper
	

class ShippingCost(object):
	def shipping_cost(self, order):
		if order.shipper == Shipper.FEDEX:
			return self._fedex_cost(order)
		elif order.shipper == Shipper.UPS:
			return self._ups_cost(order)
		elif order.shipper == Shipper.POSTAL:
			return self._postal_cost(order)
		else:
			raise ValueError('Invalid Shipper {}'.format(order.shipper))

	def _fedex_cost(self, order):
		return 3.0

	def _ups_cost(self, order):
		return 4.0

	def _postal_cost(self, order):
		return 5.0

