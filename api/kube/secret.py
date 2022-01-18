from requests import get
#from envi import auth, hostname, port, cert
from os import environ

auth = {'Authorization': 'Bearer ' + environ['TOKEN']}
hostname = environ['HOSTNAME']
port = environ['PORT']
cert = environ['CERT']

class Secret:
   def __init__(self, userid, token):
      self.url = hostname+ ':' + port
      self.userid = userid
      self.sec_path = '/api/v1/namespaces/' + userid + '/secrets/' + token

      
   def sec_show(self):
      r = get(url=self.url+self.sec_path, headers=auth, verify=cert)
      return(r.json()['data']['token'])
   
