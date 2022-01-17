from requests import get, post
from envi import auth, hostname, port, cert

class Role:
    def __init__(self, userid):
        self.r_path = '/apis/rbac.authorization.k8s.io/v1/namespaces/'+userid+'/roles'
        self.userid = userid
        self.url = hostname + port
    
    def r_show(self):
        r = get(url=self.url+self.r_path, headers=auth, verify=cert)
        return(r.json())
    
    def ro_create(self):
        rname = self.userid + "-role-pods-creator"
        data = {"kind": "Role", "apiVersion": "rbac.authorization.k8s.io/v1", "metadata": { "name": rname, "namespace": self.userid }, "rules": [{"apiGroups": [""],"resources": ["pods"],"verbs": ["patch","get","watch","list","create"]}]}
        r = post(url=self.url+self.r_path, json=data, headers=auth, verify=cert)
        return(r.json())
