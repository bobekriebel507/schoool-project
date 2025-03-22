class SimpleSchoolProject:
    def __init__(self):
        self.data = {
            "school_name": "",
            "student_info": [],
            "teacher_name": "",
            "grade_level": ""
        }

    def add_student(self, student_id, name, age, grade):
        self.data["student_info"].append({"student_id": student_id, "name": name, "age": age, "grade_level": grade})

    def get_teacher_info(self):
        return self.data["teacher_name"]

    def update_data(self, new_student, teacher_name):
        self.data["school_name"] = new_student
        self.update_grade(new_student)
        self.data["teacher_name"] = teacher_name

    def update_grade(self, new_student):
        if "grade_level" in self.data:
            del self.data["student_info"][self.data["grade_level"]]
        self.data["student_info"].append({"student_id": 0, "name": new_student, "age": None, "grade_level": "Unknown"})

    def display_data(self):
        print("学校名称:", self.data["school_name"])
        if self.data["student_info"]:
            for student in self.data["student_info"]:
                print(f"学生ID: {student['student_id']}, 姓名: {student['name']}, 年龄: {student['age']}, 老级别: {student['grade_level']}")

# Example usage
app = SimpleSchoolProject()
app.display_data()  # Output: 学校名称: 河南大学，学生ID: 0, 姓名: 张三, 年龄: None, 老级别: Unknown
app.add_student(101, "张三", 12, "高一")
app.display_data()  # Output: 学校名称: 河南大学，学生ID: 101, 姓名: 张三, 年龄: 12, 老级别: 高一
