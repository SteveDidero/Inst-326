"""Classes representing a database of employees and managers in a company.

Copyright (C) 2023
Jordan Goodman, Trinity Hill, Spencer Morgan, Steve Tanekeu, Gene Yu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""
# INST326 section 0101
# Team: Pythonista

import re
BAD_VALUES = frozenset({None, ""})

class Employee():
    """Represents the personal information of an employee at a company.
    
    Primary author: Gene Yu
    
    Attributes:
        name (str): The employee's name.
        gender (str): Either "m"an, "w"oman, or "n"onbinary.
        dob (str): Date of birth.
        email (str): Email address.
        phone (str): Phone number.
        address (str): Home address.
        position (str): The employee's job.
        department (str): The employee's department.
        salary (int): Annual gross salary.
    """
    
    def __init__(self, employee, gender="", dob="", email="", phone=""
            , address="", position="", department="", salary=-1):
        """Initializes the employee's record.
        
        Primary author: Gene Yu
        
        Args:
            employee: Either a name (str) or an Employee object. The following
                args must be given if the employee arg is a name.
            gender: (str) Either "m"an, "w"oman, or "n"onbinary.
            dob: (str) Date of birth.
            email: (str) Email address.
            phone: (str) Phone number.
            address: (str) Home address.
            position: (str) The employee's job.
            department: (str) The employee's department.
            salary: (int) Annual gross salary.
        
        Side effects:
            Creates and modifies all attributes (name, gender, dob, email, phone
                , address, position, department, and salary).
        """
        if not isinstance(employee, (Employee, str)):
            raise TypeError("The employee arg should be an Employee or an int.")
        if isinstance(employee, str) and ({name, gender, dob, email, phone
                , address, position, department, salary} & BAD_VALUES):
            raise ValueError("If a name is given as the first arg then all"
                "attributes must be non-empty.")
        if isinstance(employee, Employee):
            self.name = employee.name
            self.gender = employee.gender
            self.dob = employee.dob
            self.email = employee.email
            self.phone = employee.phone
            self.address = employee.address
            self.position = employee.position
            self.department = employee.department
            self.salary = employee.salary
            return
        self.name = employee
        self.gender = gender
        self.dob = dob
        self.email = email
        self.phone = phone
        self.address = address
        self.position = position
        self.department = department
        self.salary = salary
    
    def __repr__(self):
        """Gives the formal representation of the Employee instance.
        
        Returns:
            (str): A string which when used as the arg for eval() reconstructs
                this Employee instance.
        """
        ordered_info = [
            self.name
            ,self.gender
            ,self.dob
            ,self.email
            ,self.phone
            ,self.address
            ,self.position
            ,self.department
            ,self.salary
        ]
        return "Employee(" + ",".join((repr(x) for x in ordered_info)) + ")"


class Company:
    """Represents the people in a company.
    
    Primary author: ?
    
    Attributes:
        employees_file (str): A path to the JSON which stores all Employee
            attributes.
        managers_file (str): A path to the JSON which stores the Manager ids
            and respective lists of their subordinates' ids.
        employees (dict of int:Employee): The employee IDs and the corresponding
            Employee objects. Includes Manager objects.
        managers (list of int): Employee IDs of the Manager objects according to
            the ids in the dictionary of employees.
    """
    
    def __init__(self, employees_file, managers_file):
        """Recreates the Company object from the files of employee and manager
        information.
        
        INCOMPLETE
        Primary author: ?
        
        Args:
            employees_file (str): A path to the JSON which stores all Employee
                objects.
            managers_file (str): A path to the JSON which stores the Manager ids
                and respective lists of their subordinates' ids.
        """
        self.employees_file = employees_file
        self.managers_file = managers_file
        self.employees = {}
        self.managers = []
        # INCOMPLETE: Must load and add information from the files to the
        # attributes.
    
    def add_employee(self, employee_id):
        """Adds an Employee to the dictionary of employees.
        
        Primary author: Spencer Morgan
        
        Args:
            employee_id (int): The ID of the employee.
            
        Side effects:
            displays the employee who was added to the database.
        """
        self.employee_id = employee_id

        name = input("Enter employee name: "),
        gender =  input("Enter employee gender: "),
        dob = input("Enter employee date of birth (mm/dd/yyyy): "),
        email =  input("Enter employee email address: "),
        phone_number = input("Enter employee phone number(xxx-xxx-xxxx): "),
        address = input("Enter employee address: "),
        position = input("Enter employee company position: "),
        department = input("Enter employee department: "),
        salary = input("Enter employee salary: ")
            
        self.employees[employee_id] = {"name": name,
                         "gender": gender,
                         "dob": dob,
                         "email": email,
                         "phone_number": phone_number,
                         "address": address,
                         "position": position,
                         "department": department,
                         "salary": salary
                         }
        
        print(f"{name} was added to employee database")
    
    def add_employees_from_file(self, file):
        """Add multiple Employees from a file using regex pattern for parsing the file.
        
        Primary author: Jordan Goodman
        
        Args:
            file (str): A path to the file to read.
            
        Side effects: Adds employee information to the employee dictionary.

        """
        with open(file, 'r') as f:
            employees_to_add = [employee for employee in f]
            pattern = re.compile(r'(\d+),[ ]?(\w+ \w+),[ ]?([A-Z]+),[ ]?(\d{2}\/\d{2}\/\d{4}),[ ]?(\w+@gmail\.com),[ ]?(\d{3}-\d{3}-\d{4}),[ ]?(\d+ \w+ \w+),[ ]?([\w\s]+),[ ]?([\w\s]+),[ ]?(\$[\d,]+)') 
        
        matches = re.search(pattern, employees_to_add) 
        for match in matches:            
                employee_id = match[0]
                name = match[1]
                gender = match[2]
                dob = match[3]
                email = match[4]
                phone_number = match[5]
                address = match[6]
                position = match[7]
                department = match[8]
                salary = match[9]
                self.employees[employee_id] = {"name": name, 
                                               "gender": gender, 
                                               "dob": dob, 
                                               "email": email, 
                                               "phone number": phone_number, 
                                               "address": address, 
                                               "position": position, 
                                               "department": department,
                                               "salary": salary}
        return self.employees
    
    def write_employees_json(self, file, employees, *, strict=True):
        """Writes the information of specified Employees to a file.
        
        Primary author: Gene Yu
        
        Args:
            file (str): A path to the JSON to write to.
            employees (iterable of int and Employee): Any combination of
                employee IDs and Employee objects in the employees dict.
            strict (bool, keyword-only): Whether the write should fail if the
                employees arg contains invalid elements.
        
        Returns:
            (int): A status code. Exactly one of the following (
                0: All employees specified were written to the file.
                1: A given Employee or ID did not match an ID in the employees
                    dict. Nothing was written.
                2: A given Employee or ID did not match an ID in the employees
                    dict. Matching employees were written to the file, while
                    non-matching elements were ignored.
            )
        
        Side effects:
            Overwrites the given file.
        """
        employees_set = set(employees)
        ids = {x for x in employees_set if isinstance(x, int)}
        non_ids_set = employees_set - ids
        objs = {x for x in non_ids_set if isinstance(x, Employee)}
        right_type = ids + objs
        mismatch = False
        if len(right_type) != len(employees_set):
            mismatch = True
        if strict and mismatch:
            return 1
        all_employee_ids = {v:k for k,v in self.employees.items()}
        matches = ({i for i in ids if i in self.employees}
            | {all_employee_ids[o] for o in obj if o in all_employee_ids})
        if len(matches) != len(right_type):
            mismatch = True
        if strict and mismatch:
            return 2
        if mismatch:
            return 1
        return 0
        
    def search_employees(self, search_criteria):
        """Searches for employees based on the given criteria.
        
        Primary author: Trinity Hill

        Args:
            search_criteria: Keyword arguments representing search criteria.

        Returns:
            list of Employee: A list of employees that match the search criteria.
        """
        matching_employees = []

        for employee_id, employee in self.employees.items():
            if all(getattr(employee, key) == value for key, value in search_criteria.items()):
                matching_employees.append(employee)

        return matching_employees

class Manager(Employee):
    """Represents an employee manager in a Company.
    
    Primary author: ?
    
    Attributes:
        subordinates (list of int): The employee IDs of the manager's
            subordinate Employees.
    """
    def add_manager(self):
        """
        check the self.info dictionary and if the position of an employee is manager,
        that person gets added to the manager dictionary else they add to the employees dictionary.

        """
        self.employees = {}
        self.managers = {}
        for p in self.info:
            if p["position"] == "manager":
                self.managers[p["name"]] = p
            else:
                self.employees[p["name"]] = p
        
    def assign_employee(self):
        """
        Cross check the department of each employment and manager and append the employee's name
        to the corresponding manager's employee key.
        """

        for p in self.managers:
            self.managers[p]["employees"] = []

        for em in self.employees:
            for i in self.managers:
                if em['department'] == self.managers[i]['department']:
                    self.managers[i]["employees"].append(em["name"])
        
        name = input('Give me a name: ')
    
        for i in self.managers:
            # for a in i: # This line is not needed
            if name in self.managers[i]["employees"]:
                print(f"{name} falls under {i}")
            else:
                None        



