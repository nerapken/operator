from os import environ

auth = {'Authorization': 'Bearer' + environ['TOKEN']}
hostname = environ['HOSTNAME']
port = environ['PORT']
