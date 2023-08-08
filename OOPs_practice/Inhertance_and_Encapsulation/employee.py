class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def emp_info(self):
        print(f'Employee name is {self.name} and his id is {self.emp_id}')


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def manager_info(self):
        print(f'Manager name is {self.name}, his id is {self.emp_id} and his department is {self.department}')


class Engineer(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def engineer_info(self):
        print(f'Name of the engineer is {self.name}, his id is {self.emp_id} and his specialization is '
              f'{self.specialization}')


e = Engineer('Danish', 1, 'Software Developer')
e.engineer_info()

e = Employee('Reza', 5)
e.emp_info()