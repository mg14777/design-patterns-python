from receiver import Lights, Stereo
from invoker import RemoteControl
from command import LightsOnCommand, StereoOnCommand, StereoPlayMusicCommand


lights = Lights()
stereo = Stereo()

lights_on = LightsOnCommand(lights)
stereo_on = StereoOnCommand(stereo)
stereo_play = StereoPlayMusicCommand(stereo)

remote = RemoteControl(lights_on)
print('Turning lights on...')
remote.press_button()

remote.set_command(stereo_on)
print('Turning stereo on...')
remote.press_button()

remote.set_command(stereo_play)
print('Playing stereo...')
remote.press_button()
