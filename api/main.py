from flask import Flask, request
from kube.ns import Namespace as ns
from kube.rb import RoleBinding as rb
from kube.sa import ServiceAccount as sva
from kube.role import Role as ro
#from kube.pods import Pods as pods

class Wrapper:
    def __init__(self, data):
        self.data = data
        self.userid = data.get("userid")
        pass
    
    def n_create(self):
        #data = request.get_json()
        n = ns(self.userid)
        return n.ns_create()

    def sa_create(self):
        #data = request.get_json()
        sa = sva(self.userid)
        return sa.sa_create()
    
    def r_create(self):
        #data = request.get_json()
        rl = ro(self.userid)
        return rl.ro_create()

    def rb_create(self):
        #data = request.get_json()
        r = rb(self.userid) 
        return r.rb_create()

    def shoot(self):
        self.n_create()
        self.sa_create()
        self.r_create()
        self.rb_create()
        return "Shooted"

class Api:
    def __init__(self):
        pass

    app = Flask(__name__)

    @app.route('/api/v1/init', methods=['POST'])
    def user_init():
        data = request.get_json()
        w = Wrapper(data)
        return w.shoot()
    
    app.run(host="0.0.0.0")

a = Api()
a()
