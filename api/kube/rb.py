from requests import get, post
from envi import auth, hostname, port, cert

class RoleBinding:
    def __init__(self, userid):
        self.url = hostname + port
        self.rb_path = '/apis/rbac.authorization.k8s.io/v1/namespaces/'+ userid + '/rolebindings'
        self.userid = userid
    
    def rb_show(self):
        r = get(url=self.url+self.rb_path, headers=auth, verify=cert)
        return(r.json())
    
    def rb_create(self):
        rbname = self.userid + "-role-binding"
        data = {"kind": "RoleBinding", "apiVersion": "rbac.authorization.k8s.io/v1", "metadata": { "name": rbname }, "roleRef": { "apiGroup": "rbac.authorization.k8s.io", "kind": "Role","namespace": self.userid, "name": self.userid + "-role-pods-creator" }, "subjects": [ { "kind": "ServiceAccount", "name": self.userid, "namespace": self.userid } ] }
        r = post(url=self.url+self.rb_path, json=data, headers=auth, verify=cert)
        return(r.json())