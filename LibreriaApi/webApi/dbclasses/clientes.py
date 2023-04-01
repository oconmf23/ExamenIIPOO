import pymongo
import os

from webApi.dbclasses.dbmongo import DbMongo

class ClientesCollection:

    def __init__(self):
        self.client, self.db = DbMongo.getDB()
        self.collection = "webApi_cliente"
    
    def getOne(self, id):
        collection = self.db[self.collection]
        return collection.find_one({"id_card": id})