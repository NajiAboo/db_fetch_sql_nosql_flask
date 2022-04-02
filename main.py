from flask import Flask, request, jsonify
from services.student_service import StudentService
from utils.util import ConnectionType


app = Flask(__name__)


def build_student_service(connectionType:ConnectionType) -> StudentService:
    st_service = StudentService(connectionType)
    return st_service



@app.route("/sql/students", methods=["GET"])
def get_student_details():
    student_service = build_student_service(connectionType=ConnectionType.MYSQL)
    students = student_service.get_student_info()
    return jsonify(students)    


@app.route("/nosql/students", methods=["GET"])
def get_no_sql_student_details():
    student_service = build_student_service(connectionType=ConnectionType.NOSQL)
    students = student_service.get_student_info()
    print(students)
    return jsonify(students)


if __name__ == "__main__":
    app.run()

