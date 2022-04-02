import pymongo
from pymongo import MongoClient
import pandas as pd
import json

from bson import json_util, ObjectId
import json
 

class MongoDBHandler:
    def __init__(self) -> None:
        self.__client = pymongo.MongoClient("mongodb+srv://admin:<password>@cluster0.tsqtv.mongodb.net/studentmark?retryWrites=true&w=majority")
        

    def parse_json(self,data):
        return json.loads(json_util.dumps(data))

    def get_student_info(self):
        try:
            db = self.__client["studentmark"]
            result = db.studentsinfo.find({})
            result = self.parse_json(list(result))
            return list(result)
        except Exception as ex:
            print(ex)
        finally:
            pass
           # self.__client.close()