#Light Control
from Light import Light
from LightSwitch import LightSwitch

#SysTray Icon
from pystray import Menu, MenuItem, Icon
from PIL import Image

#Threading
from threading import Thread
from time import sleep

class LightController:

    SEPARATOR = MenuItem('- - - -', None)

    def __init__(self, defaultLight : Light, *lights : Light):
        self._lights = tuple(self.__generateLightSequence(defaultLight, *lights))
        for light in self._lights:
            light.getStateInfo()
        self._lightSwitches = tuple(self.__generateLightSwitches())
        self._menu = Menu(self.__generateMenuItems)
        self._icon = Icon('Light Control', icon=Image.open('icon.png'), menu=self._menu)

    def run(self):
        Thread(target=self._icon.run).start()
        Thread(target=self.__getLightStates).start()        

    def __getLightStates(self):
        while True:
            for light in self._lights:
                light.getStateInfo()
            sleep(5)

    def __generateLightSequence(self, defaultLight : Light, *lights : Light):
        yield defaultLight
        for light in lights:
            yield light

    def __generateLightSwitches(self):
        setDefault = True
        for light in self._lights:            
            yield LightSwitch(light, default=setDefault)
            setDefault = False

    def __generateMenuItems(self):
        count = 0
        for switch in self._lightSwitches:
            yield switch.switch
            yield switch.dimmer
            if count < len(self._lightSwitches) - 1:
                yield self.SEPARATOR
            count +=1