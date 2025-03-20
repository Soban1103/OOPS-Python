class Employee:

    # Constructor is a type of dunder or special method (__var_name__ are basic dunder/special methods)
    def __init__(self):
        self.id = 123
        print("Hello from constructor")
        self.salary = 50000
        self.designation = "Data Analyst and Machine Learning Engineer"

    def make_presentations(self, topic):
        print("Made presentation on the report of the topic ", topic) 

# Object / Instance of the class
soban = Employee()
print(soban.salary)
print(soban.designation)

# # Surpise 
# print(soban.__getattribute__('designation'))

soban.make_presentations("Data Science")