from requests import get, post


class RoleBinding:
    def __init__(self, userid):
        self.rb_path = '/apis/rbac.authorization.k8s.io/v1/namespaces/'+ userid + '/rolebindings'
        self.header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjEwWHFpZGhxdmxpTEFONGVfUV9mYXd0WDVfNk1Ta1lnSGxES1pfNmlla1kifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6Im5lcmFwa2VuLW9wZXJhdG9yLXRva2VuLWtjaGYyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6Im5lcmFwa2VuLW9wZXJhdG9yIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiZDM3MjAxY2QtNTQ0ZC00Y2M0LTk4NGQtNDc1OWE4Y2JhMzgyIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6bmVyYXBrZW4tb3BlcmF0b3IifQ.dfH6avQuan2tEAvdDhOOEEy6DotMHhquDHCENgIOQNMqy_O9USqNAU7Wec0SOWl4xQ4xzkba25aME4tPkHPo4fvKQk38ddeSTrchlK0welqovDHkqtuhagOkQSH4dyCaHtZ7tITjMgRaEaa43ZtjMOwFaPcIbKjL3uIxoOSgAmXW-zL1_tO7L7MbKoC1XiG3jsyvI1lCQpewnVWHL6rzay-rMO65dV4pcXLECRdWb-RoZFodxG0ZriXmLUMukfykAEV6vmxqioMxSjYx7CbngYABi7eO6tY1C2mSygMljEtnAGQmHhsfmTZNeTGEFjuacoYZ9bJA_0jyTimqvAAR_g'}
        self.cert = '/opt/api/ca-nerapken.pem'
        self.userid = userid
        self.url = 'https://172.31.4.147:6443'
    
    def rb_show(self):
        r = get(url=self.url+self.rb_path, headers=self.header, verify=self.cert)
        return(r.json())
    
    def rb_create(self):
        rbname = self.userid + "-role-binding"
        data = {"kind": "RoleBinding", "apiVersion": "rbac.authorization.k8s.io/v1", "metadata": { "name": rbname }, "roleRef": { "apiGroup": "rbac.authorization.k8s.io", "kind": "Role","namespace": self.userid, "name": self.userid + "-role-pods-creator" }, "subjects": [ { "kind": "ServiceAccount", "name": self.userid, "namespace": self.userid } ] }
        r = post(url=self.url+self.rb_path, json=data, headers=self.header, verify=self.cert)
        return(r.json())