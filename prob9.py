class Course:
    def __init__(self, id: int, name: str, instructor: str):
        self.id = id
        self.n = name
        self.inst = instructor
        self.students = []
        
    def add_student(self, student_id: int, first_name: str, last_name: str):
        tpl = (student_id, first_name, last_name)
        self.students.append(tpl)
        print(self.students)

    def remove_student(self, student_id: int):
        self.students = [s for s in self.students if s[0] != student_id]
        print(self.students)

    def get_student_count(self):
        print(len(self.students))

    def __str__(self):
        return f"\n{self.id} {self.n} {self.inst}"


kurs = Course(id=101, name="Python", instructor="Olimov Rustam")

kurs.add_student(1, "Ali", "Karimov")
kurs.add_student(2, "Vali", "Usmonov")

kurs.get_student_count()

kurs.remove_student(1)

print(kurs)