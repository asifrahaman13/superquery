from sqlmodel import SQLModel, Field, create_engine, Session, select

class EmployeeSalary(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    salary: float

class StudentsMarks(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    subject: str
    marks: int

# Connect to the SQLite database
sqlite_file_name = "db/example.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

# Create tables
SQLModel.metadata.create_all(engine)

# Insert sample data
employees = [
    EmployeeSalary(name='Alice', salary=70000),
    EmployeeSalary(name='Bob', salary=60000),
    EmployeeSalary(name='Charlie', salary=80000)
]

students = [
    StudentsMarks(name='David', subject='Math', marks=85),
    StudentsMarks(name='Eva', subject='Science', marks=90),
    StudentsMarks(name='Frank', subject='History', marks=78)
]

with Session(engine) as session:
    session.add_all(employees)
    session.add_all(students)
    session.commit()

# Query and print data
with Session(engine) as session:
    employee_salaries = session.exec(select(EmployeeSalary)).all()
    student_marks = session.exec(select(StudentsMarks)).all()

    print("Employee Salary Table:")
    for employee in employee_salaries:
        print(employee)

    print("\nStudents Marks Table:")
    for student in student_marks:
        print(student)
