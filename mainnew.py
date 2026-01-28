import json
import random
import string
from pathlib import Path


class Student:
    database = "data.json"
    data = []

    # Load data safely
    if Path(database).exists():
        try:
            with open(database, "r") as fs:
                data = json.load(fs)
        except json.JSONDecodeError:
            data = []

    @staticmethod
    def save():
        with open(Student.database, "w") as fs:
            json.dump(Student.data, fs, indent=4)

    @staticmethod
    def generate_registration():
        chars = (
            random.choices(string.ascii_letters, k=3)
            + random.choices(string.digits, k=3)
            + random.choices("!@#$%^&*", k=3)
        )
        random.shuffle(chars)
        return "".join(chars)

    @classmethod
    def create(cls, name, branch, year, roll_no, email):
        student = {
            "name": name,
            "branch": branch,
            "year": year,
            "roll_no": roll_no,
            "email_id": email,
            "registration_number": cls.generate_registration()
        }
        cls.data.append(student)
        cls.save()
        return student

    @classmethod
    def find_by_reg(cls, regnum):
        return next(
            (student for student in cls.data
             if student.get("registration_number") == regnum),
            None
        )

    @classmethod
    def update(cls, regnum, field, value):
        student = cls.find_by_reg(regnum)
        if not student:
            return False
        student[field] = value
        cls.save()
        return True

    @classmethod
    def delete(cls, regnum):
        student = cls.find_by_reg(regnum)
        if not student:
            return False
        cls.data.remove(student)
        cls.save()
        return True
