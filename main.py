
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Student Model
class Student(BaseModel):
    name: str
    age: int


# Student Data
students = [
    {"id": 1, "name": "Mg Mg", "age": 20},
    {"id": 2, "name": "Aung Aung", "age": 21},
    {"id": 3, "name": "Hla Hla", "age": 19},
    {"id": 4, "name": "Su Su", "age": 20},
    {"id": 5, "name": "Kyaw Kyaw", "age": 22},
    {"id": 6, "name": "Hla Win", "age": 20},
    {"id": 7, "name": "Mya Mya", "age": 19},
    {"id": 8, "name": "Aye Aye", "age": 21},
    {"id": 9, "name": "Tun Tun", "age": 22},
    {"id": 10, "name": "Thant Zin", "age": 20},
    {"id": 11, "name": "Min Min", "age": 21},
    {"id": 12, "name": "Su Mon", "age": 19},
    {"id": 13, "name": "Kyaw Zin", "age": 23},
    {"id": 14, "name": "Htet Htet", "age": 20},
    {"id": 15, "name": "Nay Chi", "age": 22},
    {"id": 16, "name": "Aung Min", "age": 21},
    {"id": 17, "name": "Ei Ei", "age": 19},
    {"id": 18, "name": "Zaw Zaw", "age": 22},
    {"id": 19, "name": "Hnin Hnin", "age": 20},
    {"id": 20, "name": "Pyae Phyo", "age": 23},
    {"id": 21, "name": "Moe Moe", "age": 21},
    {"id": 22, "name": "Thet Thet", "age": 20},
    {"id": 23, "name": "Sai Sai", "age": 22},
    {"id": 24, "name": "Nandar", "age": 19},
    {"id": 25, "name": "Wai Yan", "age": 21},
    {"id": 26, "name": "Aung Ko", "age": 23},
    {"id": 27, "name": "Phyu Phyu", "age": 20},
    {"id": 28, "name": "Kyaw Myo", "age": 22},
    {"id": 29, "name": "May Thu", "age": 19},
    {"id": 30, "name": "Htet Aung", "age": 21},
    {"id": 31, "name": "Myo Min", "age": 20},
    {"id": 32, "name": "Thiri", "age": 22},
    {"id": 33, "name": "Aung Thu", "age": 23},
    {"id": 34, "name": "Su Wai", "age": 19},
    {"id": 35, "name": "Zin Mar", "age": 21},
    {"id": 36, "name": "Hla Myint", "age": 20},
    {"id": 37, "name": "May Zin", "age": 22},
    {"id": 38, "name": "Ko Ko", "age": 19},
    {"id": 39, "name": "Yamin", "age": 21},
    {"id": 40, "name": "Aung Htet", "age": 23},
    {"id": 41, "name": "Nyein Chan", "age": 20},
    {"id": 42, "name": "Khin Khin", "age": 22},
    {"id": 43, "name": "Myo Thant", "age": 19},
    {"id": 44, "name": "Thazin", "age": 21},
    {"id": 45, "name": "Pyae Sone", "age": 23},
    {"id": 46, "name": "Aye Thandar", "age": 20},
    {"id": 47, "name": "Min Khant", "age": 22},
    {"id": 48, "name": "Ei Phyu", "age": 19},
    {"id": 49, "name": "Kaung Myat", "age": 21},
    {"id": 50, "name": "Phyo Lin", "age": 20},
]


# Home Route
@app.get("/")
def home():
    return {"message": "My Student Server is Running!"}


# Get All Students
@app.get("/students")
def get_students():
    return students


# Add Student
@app.post("/students", status_code=201)
def add_student(student: Student):
    new_id = max((s["id"] for s in students), default=0) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "age": student.age
    }

    students.append(new_student)

    return new_student


# Edit Student
@app.put("/students/{student_id}")
def edit_student(student_id: int, student: Student):
    for s in students:
        if s["id"] == student_id:
            s["name"] = student.name
            s["age"] = student.age

            return s

    return {"message": "Student Not Found"}

# Get Single Student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student Not Found"}
