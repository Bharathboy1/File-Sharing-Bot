import re
from os import environ

DATABASE_URI = environ.get('DATABASE_URI', "mongodb://rename:rename@ac-x0xofim-shard-00-00.wzkakkz.mongodb.net:27017,ac-x0xofim-shard-00-01.wzkakkz.mongodb.net:27017,ac-x0xofim-shard-00-02.wzkakkz.mongodb.net:27017/?ssl=true&replicaSet=atlas-ar97qb-shard-0&authSource=admin&retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "bharath")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'filestore')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '634637418').split()]
