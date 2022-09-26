import pystray
from PIL import Image
import requests

import Light

LIGHT_CONTROL_URL = 'http://192.168.0.77'

def main():
    desklight = Light(LIGHT_CONTROL_URL + '/desk')
    worklight = Light(LIGHT_CONTROL_URL + '/workdesk')

    desklight_item = pystray.MenuItem('Desk Light', onClickedDesk, default=True, checked=getDeskState)
    worklight_item = pystray.MenuItem('Work Light', worklight.toggle)

    menu = pystray.Menu(desklight_item, worklight_item)

    image = Image.open('icon.png')

    icon = pystray.Icon(
    'Light Control',
    icon=image, menu=menu)  #create_image(64, 64, 'black', 'white'), menu=menu)

    icon.run()

if __name__ == '__main__':
    main()