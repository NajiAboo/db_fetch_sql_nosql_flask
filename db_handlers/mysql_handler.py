import json
import mysql.connector as connection
import pandas as pd



class MySQLHandler:
    host ="localhost"
    password ="Password"
    user="root"
    database = "Students"

    def __init__(self) -> None:
        self.connection = connection.connect(host=self.host, database=self.database, password=self.password, user=self.user)
    
    def get_student_info(self) -> json:
        try:
            query = 'select * from student_marks_csv;'
            results = pd.read_sql(query,self.connection)
            
            print(results)
            return results.to_json(orient="records")
        except Exception as ex:
            print(ex)
        finally:
            self.connection.close()
    