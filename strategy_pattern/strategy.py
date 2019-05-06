from enum import Enum
from abc import ABCMeta, abstractmethod

'''
Strategy Pattern:
Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.

Context:
Provides a service by delegating some computation to interchangeable components that
implement alternative algorithms. In our case its ShippingCost since it returns the
shipping cost by delegating the calculation to different strategies.

Strategy:
The interface common to the components that implement the different algorithms.
In our example, this role is played by an abstract class called AbsStrategy.

Concrete Strategy:
One of the concrete subclasses of Strategy.
FedexStrategy, PostalStrategy and UPSStrategy are the three concrete strategies implemented.

Note: Instead of having the abstract strategy class and concrete classes we can also turn the
      concrete classes into individual functions since functions are first class objects in Python.
'''

class Shipper(Enum):
	FEDEX  = 0
	UPS    = 1
	POSTAL = 2


class Order(object):
	pass


class ShippingCost(object):

	def __init__(self, calculation_strategy):
		self.calculation_strategy = calculation_strategy

	def shipping_cost(self, order):
		return self.calculation_strategy.calculate(order)


class AbsCost(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def calculate(self, order):
		''' Calculate shipping cost '''
		return NotImplementedError('abstract method needs to be implemented in the child class')


class FedexCost(AbsCost):
	def calculate(self, order):
		return 3.0


class UpsCost(AbsCost):
	def calculate(self, order):
		return 4.0


class PostalCost(AbsCost):
	def calculate(self, order):
		return 5.0


if __name__ == '__main__':
	o = Order()

	fedex = FedexCost()
	cost_calculator = ShippingCost(fedex)
	print('Fedex Cost:', cost_calculator.shipping_cost(o))

	ups = UpsCost()
	cost_calculator = ShippingCost(ups)
	print('Ups Cost:', cost_calculator.shipping_cost(o))

	postal = PostalCost()
	cost_calculator = ShippingCost(postal)
	print('Postal Cost:', cost_calculator.shipping_cost(o))
