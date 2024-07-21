class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.average = sum(scores) / len(scores)

def get_student_data():
    num_students = int(input("Enter the number of students: "))
    students = []
    
    for _ in range(num_students):
        name = input("Enter the student's name: ")
        scores = list(map(int, input("Enter the student's scores separated by spaces: ").split()))
        student = Student(name, scores)
        students.append(student)
    
    return students

def calculate_ranks(students):
    sorted_students = sorted(students, key=lambda s: s.average, reverse=True)
    for rank, student in enumerate(sorted_students, start=1):
        student.rank = rank

def print_student_data(students):
    print("\nStudent Rankings:")
    for student in students:
        print(f"Rank: {student.rank}, Name: {student.name}, Average: {student.average:.2f}")

def main():
    students = get_student_data()
    calculate_ranks(students)
    print_student_data(students)

if __name__ == "__main__":
    main()
