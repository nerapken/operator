from requests import get, post
from envi import auth, hostname, port, cert

class Namespace:
    
    def __init__(self, userid):
       self.userid = userid
       self.url = hostname + port
       self.ns_path = '/api/v1/namespaces/'
       self.data = {'kind': 'Namespace', 'apiVersion': 'v1', 'metadata': {'name': self.userid}}


    def ns_get(self):
        r = get(url=self.url+self.ns_path, headers=auth, verify=cert)
        return r.json()

    def ns_create(self):
        r = post(url=self.url+self.ns_path, headers=auth, json=self.data, verify=cert)
        return r.json()
