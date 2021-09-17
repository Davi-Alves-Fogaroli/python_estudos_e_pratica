from src.server.instance import server

#"Werkzeug==0.16.0" version compatible whitbecause it has "flask_restplus"

#import controllers.___ Every time you create a new controller, include it in the main file where the application is starting
from src.controllers.books import *

server.run()#start server