
class Lights(object):
	''' Class representing lights and being used as receiver object '''
	def on(self):
		print('Lights on')

	def off(self):
		print('Lights off')


class Stereo(object):
	''' Class representing stereo and being used as receiver object '''
	def on(self):
		print('Stereo turned on')

	def set_cd(self):
		print('Inserting CD in stereo')

	def play(self):
		print('Playing music...')

	def off(self):
		print('Stereo turned off')
		