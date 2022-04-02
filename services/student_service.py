from utils.util import ConnectionType
from db_handlers.mysql_handler import MySQLHandler
from db_handlers.mongodb_handler import MongoDBHandler

class StudentService:
    def __init__(self, connection_type: ConnectionType ) -> None:
        self.__connection_type  = connection_type
        self.db_handler =  MySQLHandler() if self.__connection_type == ConnectionType.MYSQL else MongoDBHandler()

    
    def get_student_info(self):
        student_details = self.db_handler.get_student_info()
        return student_details
    
    

