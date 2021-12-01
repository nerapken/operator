from requests import get

class Pods:
    
    def __init__(self) -> None:
       self.header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjEwWHFpZGhxdmxpTEFONGVfUV9mYXd0WDVfNk1Ta1lnSGxES1pfNmlla1kifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJuZXJhcGtlbi10ZXN0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6Im5lcmFwa2VuLXVzZXItdG9rZW4tNXpmdGIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoibmVyYXBrZW4tdXNlciIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6ImZlOWExY2NjLTc3Y2ItNGViZS1hZjQ2LWEyZDE3ZTRjY2M4ZiIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpuZXJhcGtlbi10ZXN0Om5lcmFwa2VuLXVzZXIifQ.fMKK2B_7n-dvowoDziJbbza26geenVsJLxXSvJnwVtnsggmBErsuAH-2O3zfhhVmj2UYOnOt7gCMyQF-2qiiieKcIF5noSYVu0bVPNkjUeZGutmNHvALTiHjwDggb0yMgLu4f5Ewb7pVK9yODwaonLzgS1yAaVqGzr9tY_XOm-qbjMMQncc7Jn2CXvD0nDTo3tjyxmMOXbS3t5HFskkNi_B1gmfWkTE0ANw_XSq9gEUAUTuOsT5HIVKLwWNCx0fmdK8wyrWwCcQxJh9IPLt16GdoDUMZG098eLS4dVyvDKRv4TFx0T6X_uIXQcGXqro6lAcIzZTXVtRuJ3dnwXfODw'}
       self.cert = '/home/aji/ca-nerapken.pem'
       self.url = 'https://172.31.4.147:6443'
       self.userid = 'admin'
       self.ns_path = '/api/v1/namespaces/nerapken-test/pods'
    
    def pods_get(self):
        r = get(url=self.url+self.ns_path, headers=self.header, verify=self.cert)
        return r.json()

p = Pods()
print(p.pods_get())