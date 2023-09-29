import requests
import time

class TpLink:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        # URL tp-link
        # edit               |
        #                    V
        self.url= 'http://tplinkmodem.net'
        self.status = ''
    
    def getConectionStatus(self):
    
        # session init data
        payload = {
            'metod': 'do',
            'login': {
                'password': self.password,
                'username': self.user
            }
        }

        # session init
        with requests.Session() as s:
            p= s.post(self.url, data=payload)
            # Chek status init
            if p.status_code == 200:
                print('session granted')
                # get conection status
                conection_status = s.get(self.url + '/status/status_deviceinfo.htm')
                # write var in a txt file
                with open('TpLink.INC', 'w' ) as f:
                    if 'link up' in conection_status.text:
                        self.status == 'up'
                    elif 'link down' in conection_status.text:
                        self.status == 'dwn'
                    else:
                        print('Another error')
                    f.write(f'[Variables]\nTp-Link={self.status}')
                    
            else:
                print('Conection error')
# edit               |
#                    V
tpLink = TpLink('Tu_Usuario', 'Tu_Password')

while True:
    tpLink.getConectionStatus()
    time.sleep(5)

