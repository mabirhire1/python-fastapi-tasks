class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.average = self.calculate_average()
        self.grade = self.assign_grade()

    def calculate_average(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def assign_grade(self):
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        return f"Name: {self.name}\nAverage: {self.average:.2f}\nGrade: {self.grade}\nScores: {self.scores}\n"
