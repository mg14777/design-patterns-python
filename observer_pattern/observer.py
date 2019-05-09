from abc import ABCMeta, abstractmethod

class AbsSubject(object):
	__metaclass__ = ABCMeta

	# keep track of currently registered observers
	_observers = set()

	def register(self, o):
		if not isinstance(o, AbsObserver):
			raise TypeError('Provided observer not derived from AbsObserver')
		self._observers.add(o)

	def unregister(self, o):
		if o in self._observers:
			self._observers.remove(o)

	def notify(self):
		for o in self._observers:
			o.update()

class CricketData(AbsSubject):

	def __init__(self):
		self.runs = 0
		self.wickets = 0
		self.overs = 0

	def update_data(self, runs = 0, wickets = 0, overs = 0):
		self.runs += runs
		self.wickets += wickets
		self.overs += overs
		self.notify()

class AbsObserver(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def update(self):
		return NotImplementedError('Method must be implemented in derived class')

class CurrentScoreDisplay(AbsObserver):

	def __init__(self, cricket_data):
		self.cricket_data = cricket_data

	def update(self):
		print('Current Score Display:')
		print('\tRuns:', self.cricket_data.runs)
		print('\tWickets:', self.cricket_data.wickets)
		print('\tOvers:', self.cricket_data.overs)
		print()

class AverageScoreDisplay(AbsObserver):

	def __init__(self, cricket_data):
		self.cricket_data = cricket_data

	def update(self):
		print('Average Score Display:')
		average_score = self.cricket_data.runs/self.cricket_data.overs
		print('\tAverage Score:', average_score)

if __name__ == '__main__':
	# subject
	cricket_data = CricketData()

	# observers
	current_score_display = CurrentScoreDisplay(cricket_data)

	# register observer with subject
	cricket_data.register(current_score_display)

	# update data
	# observers should be notified and will reflect their updated state
	cricket_data.update_data(runs=50, wickets=1, overs=5)

	# register another observer
	average_score_display = AverageScoreDisplay(cricket_data)
	cricket_data.register(average_score_display)

	# update data
	# this time both current score and average score will be displayed
	cricket_data.update_data(runs=75, wickets=2, overs=8)
