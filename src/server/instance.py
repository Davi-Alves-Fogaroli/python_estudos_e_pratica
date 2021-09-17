from flask import Flask
from flask_restplus import Api #This lib helps to developopr API rest, because it has features taht flask doesn't have.

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version = "1.0",
            title = "First Api Ever",
            description = "A the chose one, the first hollow in the cursed lands",
            doc = "/docs"
                        )

    def run(self,): #method responsible for starting ther server
        self.app.run(
            debug = True #only in develop, when we go to production remove debug=True 
        )           

server = Server()    