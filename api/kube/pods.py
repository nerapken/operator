from requests import get
from envi import auth, hostname, port, cert
class Pods:
    
    def __init__(self):
        self.url = hostname + port
        self.userid = 'admin'
        self.ns_path = '/api/v1/namespaces/nerapken-test/pods'
    
    def pods_get(self):
        r = get(url=self.url+self.ns_path, headers=auth, verify=cert)
        return r.json()

p = Pods()
print(p.pods_get())