import requests
from time import sleep

class Light():
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.light_state = {'onState': False, 'pwmValue': 255}
        self._http_headers = {'Content-type':'application/x-www-form-urlencoded'}
        self._http_data = {'state':'off', 'pwmValue':255}        

    def getStateInfo(self):
        response = requests.get(self.url)
        self.__decodeJsonStateInfo(response)

    def dim(self, value):
        self._http_data['pwmValue'] = value
        self.__post()

    def on(self):
        self._http_data['state'] = 'on'
        self.__post()

    def off(self):
        self._http_data['state'] = 'off'
        self.__post()
    
    def toggle(self):
        if self.light_state['onState']:
            self.off()
        else:
            self.on()

    def getState(self):
        return

    def __post(self):
        response = requests.post(self.url, headers = self._http_headers, data = self._http_data)
        while response.status_code != 200:
            sleep(2)
            self.__post()
        self.__decodeJsonStateInfo(response)
    
    def __decodeJsonStateInfo(self, response : requests.Response):
        if response.json()['state'] == 'on':
            self.light_state['onState'] = True
        elif response.json()['state'] == 'off':
            self.light_state['onState'] = False
        
        self.light_state['pwmValue'] = response.json()['pwmValue']