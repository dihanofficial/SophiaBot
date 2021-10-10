import io
import asyncio
import os
import requests

from SophiaBot import MONGO_DB_URI
from pymongo import MongoClient


client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["SophiaBot"]
