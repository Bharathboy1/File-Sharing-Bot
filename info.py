import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

DATABASE_URI = environ.get('DATABASE_URI', "mongodb://rename:rename@ac-x0xofim-shard-00-00.wzkakkz.mongodb.net:27017,ac-x0xofim-shard-00-01.wzkakkz.mongodb.net:27017,ac-x0xofim-shard-00-02.wzkakkz.mongodb.net:27017/?ssl=true&replicaSet=atlas-ar97qb-shard-0&authSource=admin&retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "bharath")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'filestore')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '634637418').split()]
