from pymongo import MongoClient
from . import config

client = MongoClient(
    config.MONGODB_HOST,
    config.MONGODB_PORT,
    username=config.MONGODB_USERNAME,
    password=config.MONGODB_PASSWORD,
)

mongodb = client.brownies
