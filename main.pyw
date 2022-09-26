from LightController import LightController
from Light import Light

def main():
    URL = 'http://192.168.0.77'
    lc = LightController(Light(URL + '/desklight', 'Desk Light'), Light(URL + '/worklight', 'Work Light'))
    lc.run()

if __name__ == '__main__':
    main()