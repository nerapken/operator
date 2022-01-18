from requests import get, post
#from envi import auth, hostname, port, cert
from os import environ

auth = {'Authorization': 'Bearer ' + environ['TOKEN']}
hostname = environ['HOSTNAME']
port = environ['PORT']
cert = environ['CERT']

class ServiceAccount:
   def __init__(self, userid):
      self.userid = userid
      self.sa_path = '/api/v1/namespaces/' + userid + '/serviceaccounts/'
      self.sa_user_path = '/api/v1/namespaces/' + userid + '/serviceaccounts/' + userid
      self.url = hostname+ ':' + port
      
   def sa_show(self):
      r = get(url=self.url+self.sa_path, headers=auth, verify=cert)
      return(r.json())
   
   def sa_create(self):
      data = {'kind': 'ServiceAccount', 'apiVersion': 'v1', 'metadata': {'name': self.userid}}
      r = post(url=self.url + self.sa_path, headers=auth, json=data, verify=cert)
      return(r.json())
   
   def get_secret_name(self):
      r = get(url=self.url+self.sa_user_path, headers=auth, verify=cert)
      return(r.json()['secrets'][0]['name'])
