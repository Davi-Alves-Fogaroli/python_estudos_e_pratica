from flask import Flask
from flask_restplus import Api, Resoucer

from src.server.instance import server

app, api = server.app, server.api #search from server, our api and app

books_db = [ #local data
    {"id": 0, "tittle": "Art of War"},
    {"id": 1, "tittle": "How to bake bread"}
]

@api.route("/books")
class Book_list(Resoucer): #Resoucer responsible for all resources, get, post, delete, put
    def get(self, ): #mesmo nome do methodo http que vou usar para esta rota
        return books_db #It will only return a list of local data. We normally ask the database, but in this script we're just going to use local data 


