from flask import Flask, request
from kube.ns import Namespace as ns
#from kube.rb import RoleBinding as rb
#from kube.sa import ServiceAccount as sa
#from kube.pods import Pods as pods

class Wrapper:
    def __init__(self):
        pass
    
    def n_create(self):
        data = request.get_json()
        n = ns(data.get("userid"))
        return n.ns_create()
    
class Api:
    def __init__(self):
        pass

    app = Flask(__name__)

    @app.route('/api/v1/init', methods=['POST'])
    def init():
        w = Wrapper()
        return w.n_create()
    
    app.run(host="0.0.0.0")

a = Api()
a()
