from LightController import LightController
from Light import Light

def main():
    URL = 'http://192.168.0.5'
    lc = LightController(Light(URL + '/desklight', 'Desk Light'), Light(URL + '/worklight', 'Work Light'), Light(URL + '/light3', 'Light 3'), Light(URL + '/light4', 'Light 4'))
    lc.run()

if __name__ == '__main__':
    main()