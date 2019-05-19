
class RemoteControl(object):
	''' Class representing a remote control acting as the invoker '''

	def __init__(self, command=None):
		self.command = command

	def set_command(self, command):
		self.command = command

	def press_button(self):
		self.command.execute()
		