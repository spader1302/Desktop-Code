from Light import Light
from pystray import Menu, MenuItem as Item
from numpy import interp

class LightSwitch:
    def __init__(self, light : Light, default = False):
        self.light = light
        self.switch = Item(light.name, self.__onClicked, checked=self.__getChecked, default=default)
        self._dim_menu = Menu(self.__generateDimItems)
        self.dimmer = Item('Dim Value', self._dim_menu)

    DIM_STEP = 10

    def __getChecked(self, item : Item):
        return self.light.light_state['onState']

    def __onClicked(self):
        self.light.toggle()

    def __generateDimItems(self):
        for i in range(self.DIM_STEP, 101, self.DIM_STEP):            
            yield Item(str(i) + '%', dimActionCallable(self, i))

class dimActionCallable:
    def __init__(self, switch : LightSwitch, dimPercentage : int):
        self._dimValue = int(interp(dimPercentage, [0,100], [0,255]))
        self._switch = switch

    def __call__(self, *any):
        self._switch.light.dim(self._dimValue) 