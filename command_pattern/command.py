from abc import ABCMeta

'''
Command Pattern:
	The command pattern encapsulates a request as an object, thereby letting us parameterize
	other objects with different requests, queue or log requests, and support undoable operations.

Example borrowed from geeksforgeeks
https://www.geeksforgeeks.org/command-pattern/
'''

class Command(object):
	''' Interface to create new concrete commands and execute them '''
	__metaclass__ = ABCMeta

	def __init__(self, receiver):
		self.receiver = receiver

	def execute(self):
		raise NotImplementedError('Implement method in concrete command')


class LightsOnCommand(Command):
	''' Represents concrete command class that
		uses receiver object (lights) to turn lights on
	'''
	def __init__(self, lights):
		self.lights = lights

	def execute(self):
		self.lights.on()


class StereoOnCommand(Command):
	''' Concrete command to turn stereo on '''

	def __init__(self, stereo):
		self.stereo = stereo

	def execute(self):
		self.stereo.on()


class StereoPlayMusicCommand(Command):
	''' Concrete command to play music from CD '''

	def __init__(self, stereo):
		self.stereo = stereo

	def execute(self):
		self.stereo.on()
		self.stereo.set_cd()
		self.stereo.play()
