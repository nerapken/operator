# RBAC Operator
this project created for RBAC operator on kubernetes, when you want add user on kubernetes with permission, you can use this.

## How to start
1. create docker network
```
docker network create --subnet 192.168.5.0/24 default-2
```
2. install docker compose for linux
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
3. Clone code from repo 
```
gh repo clone nerapken/operator
```
4. Customize docker-compose.yml with your kubernetes cluster
```
cd operator

# use text editor like vim or nano
vim docker-compose.yml

# need to change to your env
- environment:
   - TOKEN=eytttyyyyzzxxxexample
   - HOSTNAME=https://operator-api.example.com
   - PORT=6443
   - CERT=/opt/ca-nerapken-example.pem
```

5. build and run docker
```
docker-compose up --build -d
```

## Api Documentation
use `/api/v1/init` for POST method with data:

```
{
   'userid': 'username'
}
```
you can change `username` with username which you want create 

response will be user token which can be used for authorize kubernetes from API
![](https://github.com/nerapken/operator/blob/main/src/sample-api.gif?raw=true)

