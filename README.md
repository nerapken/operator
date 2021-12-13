# Kube Operator
   berfungsi untuk mengoperasikan kubernetes melalui api, saat ini tersedia rbac management

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

4. build and run docker
```
cd operator
docker-compose up --build -d
```
