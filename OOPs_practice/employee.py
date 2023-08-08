import csv


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def emp_details(self):
        data = []

        with open('employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

            print(data)


