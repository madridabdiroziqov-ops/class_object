class Student:
    def __init__(self, id: int, first_name: str, last_name: str):
        self.id = id
        self.f_n = first_name
        self.l_n = last_name
        self.grades = []

    def get_full_name(self):
        return self.f_n, self.l_n
    
    def add_grade(self, grade: int):
        
        self.grades.append(grade)
        print(self.grades)

    def get_average(self):
        return sum(self.grades) / len(self.grades)
    
    def __str__(self) -> str:
        return f"\nID: {self.id}\nIsm: {self.f_n}\nFamiliya: {self.l_n}\nBahosi: {self.grades}"


S1 = Student(12, "ali", "karimov")
print(S1.get_full_name())
S1.add_grade(80)
S1.add_grade(90)
print(S1.get_average())
print(S1)