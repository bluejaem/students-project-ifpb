import os
import pickle
from datetime import datetime
from student import Student

class StudentService:
    DATA_FILE = "students.pkl"
    LOG_FILE = "operations.log"

    def __init__(self):
        self.students = self._load_data()

    def _load_data(self) -> list:
        if not os.path.exists(self.DATA_FILE):
            return []
        try:
            with open(self.DATA_FILE, "rb") as file:
                return pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _save_data(self):
        with open(self.DATA_FILE, "wb") as file:
            pickle.dump(self.students, file)

    def _log_operation(self, action: str, student_id: int, student_name: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Student {action}: {student_id} - {student_name}\n"
        with open(self.LOG_FILE, "a", encoding="utf-8") as file:
            file.write(log_entry)

    def get_next_id(self) -> int:
        if not self.students:
            return 1
        return max(s.id for s in self.students) + 1

    def register_student(self, name: str, house: str) -> Student:
        student_id = self.get_next_id()
        student = Student(student_id, name, house)
        self.students.append(student)
        self._save_data()
        self._log_operation("registered", student.id, student.name)
        return student

    def remove_student(self, student_id: int) -> bool:
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                self._save_data()
                self._log_operation("removed", student.id, student.name)
                return True
        return False

    def list_all(self) -> list:
        return self.students

    def find_by_id(self, student_id: int) -> Student | None:
        for student in self.students:
            if student.id == student_id:
                return student
        return None