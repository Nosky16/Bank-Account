import math
# import numpy as np

class Student:
    """
    name -> str: name of the student including first and last name
    reg_no -> str: the student's registration number
    level -> int: the year of the student in the school
    department -> str: The department at which the student is enrolled in

    compute_cgpa() ->: Method for computing the student's CGPA. It has no parrameter
    getStudentCGPA() ->: A method that returns the student's CGPA

    """
    def __init__(self, name, reg_no, level, department):
        self.name = name
        self.reg_no = reg_no
        self.level = level
        self.department = department


    def compute_cgpa(self):
        CGPA = 0
        number_of_courses = int(input("How many courses do you have their results? "))
        for i in range(number_of_courses):
            grade = input(f"Enter your Grade in the {i+1}th course:  ")

            if grade.upper() == "E":
                CGPA +=1
            elif grade.upper() == "D":
                CGPA += 2
            
            elif grade.upper() == "C":
                CGPA += 3
            elif grade.upper() == "B":
                CGPA += 4
            elif grade.upper() == "A":
                CGPA += 5
        
        CGPA /= number_of_courses


        print(f"The final CGPA of {self.name} is {CGPA}")

        return CGPA
    
    def getStudentClassOfDegree(self):

        cgpa = self.compute_cgpa()
        classDegree = ""
        if cgpa < 1:
            classDegree = "University Attempted"
        elif cgpa < 2.5:
            classDegree = "Third Class"
        elif cgpa < 3.5:
            classDegree = "Second Class Lower"
        elif cgpa < 4.5:
            classDegree = "Second Class Upper"
        else:
            classDegree = "First Class"
        
        print(f"{self.name}, your class of degree is {classDegree} division!")

    
    def __str__(self):
        # return f"{self.name} {self.reg_no} {self.level} {self.department}"
        return f"{self.name} with registration number: {self.reg_no} in {self.level} level of the department of {self.department}"
        

            
student1 = Student("Emma Attama", "201900671", 500, "Medicine and Surgery")
student2 = Student("Mary Odo", "2018-20015", 400, "Accounting")
stds = [student1, student2]

students = [ ]

for student in stds:
    std = {}
    std['name'] = student.name
    std['regNo'] = student.reg_no
    std['level'] = student.level
    std['department'] = student.department

    students.append(std)

#print(students)


class Employee:
    """"
name -> str: name of the employee
position -> str: the position the employee heads
salary -> int: the amount the employee is been paid
    """

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def employee_raise(self):
        old_salary = self.salary
        salary = 0
        position = self.position
        
        if position.title() == "Junior Staff":
            salary = old_salary + old_salary*0.15
        elif position.title() == "Senior Staff":
            salary = old_salary + old_salary*0.25
        else:
           salary = old_salary + old_salary*0.30
        self.salary = salary

       # print(f"{self.name} your salary has been increased from {old_salary} to {salary}")

        # return salary
    
# staff = Employee('James Odo', 'Director', 500000.00)
# staff2 = Employee('Innocent Makata', 'Senior staff', 380000.00)
# staff3 = Employee('Mary Nelly', 'junior staff', 120000.00)

# staff.employee_raise()
# staff2.employee_raise()
# print(staff2.salary)
# staff3.employee_raise()
# staff2.employee_raise()
# print(staff2.salary)


       
# class Date:
#     """
#     day -> int: the number of days in a month
#     month -> int: number of months in a year
#     year -> int: 

#     """
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def leap_year(self, year):
#         if year % 4 == 0:
#             return True
#         else
       


# class Bank:
#     """
#     accout_number -> int: account number of the customer
#     balance -> int: total balance in the account number og the customer

#     """

#     def __init__(self, account_number, account_name, account_type, balance):
#         self.account_number = account_number
#         self.balance = balance
#         self.account_name = account_name
#         self.account_type = account_type

#     def get_account(self):
#         account = int(input("Enter your account number: "))
#         if account == self.account_number:
#             print(f"Your account detail is: {self.account_number}")
#         else:
#             print(f"No record found")

#     def add_account(self, account):
#         new_account = int(input("Enter account number: "))
#         if new_account != self.account_number:
#             new_account = self.account_number.append(account)
#         else:
#             print(f"Account already existed")

#     def total_balances(self):
#         print((self.balance))
#         for i in (self.balance):
#             total_bal = i + (self.balance)
#         print(f"Total balance is {total_bal}")
    

# bank1 = Bank(2060493211, 493.23)
# bank2 = Bank(1110792290, 49583.43)


class Time:

    def __init__(self, day, hour, minutes, seconds):
        self.day = day
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def ___str___(self):
        return f"{self.day}: {self.hour}: {self.minutes}: {self.seconds}"
    
    def addition_of_time(self,time):

        h1 = self.hour
        m1 = self.minutes
        s1 = self.seconds
        d1 = self.day

        h2 = time.hour
        m2 = time.minutes
        s2 = time.seconds
        d2 = self.day

        s = s1 + s2

        if s >= 60:
            s -= 60
            m1 += 1

        m = m1+m2
        if m >= 60:
            m -= 60
            h1 += 1

        h = h1 + h2

        if h >= 24:
            h -= 24
            d1 += 1

        d = d1 + d2
        if d >= 30:
            d -= 30

        if s <10:
            s = '0'+str(s)
        if m<10:
            m = '0'+str(m)
        if h < 10: 
            h = '0' + str(h)
        if d < 10:
            d = '0' +str(d)
        
        return f'{d}:{h}:{m}:{s}'
    
    def time_subtraction(self, time):
    
        h1 = self.hour
        m1 = self.minutes
        s1 = self.seconds
        d1 = self.day

        h2 = time.hour
        m2 = time.minutes
        s2 = time.seconds
        d2 = time.day

        d = d1 - d2

        if d >= 30:
            d -= 30
            h1 += 1

        h = h1-h2
        if h >= 24:
            h -= 24
            m1 += 1

        m = m1 - m2

        if m >= 60:
            m -= 60
            s1 += 1

        s = s1 - s2
        if s >= 60:
            s -= 60

        if s <10:
            s = '0'+str(s)
        if m<10:
            m = '0'+str(m)
        if h < 10: 
            h = '0' + str(h)
            d1 -= 1


        return f'{d}:{h}:{h}:{s}'
    
        
        
    
t1 = Time(5, 3, 34, 45)
t2 = Time(7, 4, 54, 55)

t = t1.addition_of_time(t2)
t1 = t2.time_subtraction(t1)

print(t,t1)



class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f"{self.day:02d}:{self.month:02d}:{self.year:04d}"
    
    def leap_year(self):
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def days_in_month(self):
        if self.month == 2:
            return 29 if self.leap_year() else 28
        if self.month in [4, 6, 9, 11]:
            return 30
        else:
            return 31
    
    def days_1(self):
        total_days = self.day
        for m in range(1, self.month):
            present_date = Date(1, m, self.year)
            total_days += present_date.days_in_month()
        total_days += (self.year - 1) * 365
        total_days += (self.year - 1) // 4
        total_days -= (self.year - 1) // 100
        total_days += (self.year - 1) // 400
        return total_days
    
    def days_difference(self, other_date):
        days1 = self.days_1()
        days2 = other_date.days_1()
        return abs(days2 - days1)


date1 = Date(21, 7, 2024)
date2 = Date(1, 2, 2024)

# print(f"Date 1: {date1}")
# print(f"Date 2: {date2}")
# print(f"Difference in days: {date1.days_difference(date2)}")

# import pandas

# our_list = ['KC', 'Liz', 'Sade', 'John', 'Victor', 'Zoba', 'Donald']

# our_scores = [100, 90, 80, 70, 60, 50, 40]


# our_df = pd.DataFrame({'Name': our_list, 'Score': our_scores})
# print(our_df)

class Date:

    def __init__(self, year, month, day, hour, minutes, seconds):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    
    def __str__(self):
        return f"{self.year:04d}:{self.month:02d}:{self.day:04d}, {self.hour:02d}:{self.minutes:02d}:{self.seconds:02d}"
    
    def leap_year(self):
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def days_in_month(self):
        if self.month == 2:
            return 29 if self.leap_year() else 28
        if self.month in [4, 6, 9, 11]:
            return 30
        else:
            return 31
    
    def days_1(self):
        total_days = self.day
        for m in range(1, self.month):
            present_date = Date(1, m, self.year)
            total_days += present_date.days_in_month()
        total_days += (self.year - 1) * 365
        total_days += (self.year - 1) // 4
        total_days -= (self.year - 1) // 100
        total_days += (self.year - 1) // 400
        return total_days
    
    def days_difference(self, other_date):
        days1 = self.days_1()
        days2 = other_date.days_1()
        return abs(days2 - days1)
    
    
    
date1 = Date(2024, 3, 14, 11, 32, 45)
date2 = Date(2023, 4, 13, 7, 15, 54)

# print(f"Date 1: {date1}")
# print(f"Date 2: {date2}")
# print(f"Difference in days: {date1.days_difference(date2)}, {date1.time_subtraction(date2)}")

    
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack != []:
            return self.stack.pop()
        else:
            return None
        
stack = Stack()
# stack.push("Ben")
# stack.push("Rita")
# stack.push("Jude")
print(stack.pop())



import datetime

class Account:
    def __init__(self, account_number, customer):

        self.account_number = account_number
        self.customer = customer
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Credit", amount))
        self.__save_transactions()
        # return Transaction("Credit", amount)
       

    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(Transaction("Debit", amount))
            self.__save_transactions()
            # return Transaction("Debit", amount)
        else:
            return ValueError("You have insufficient Balance!")
        
    def get_balance(self):
        return Transaction("Blanace", self.balance)

    def get_transaction(self):
        with open("0060493211.txt", "r") as trx:
            trans = trx.readlines()
            for t in trans:
                print(t)
        
            # for transaction in self.transactions:
            #     trx.read(f"{transaction}")

    def __save_transactions(self):
        with open(f"{self.account_number}.txt", "a") as trs:
            for transaction in self.transactions:
                trs.write(f"\n{transaction}")



class SavingsAccount:
    def __init__(self, account_number, customer, interest_rate):
        super().__init__(account_number, customer)
        self.interst_rate = interest_rate

    def get_balance(self):
        self.balance *= self.interst_rate
        return Transaction("balance" , self.balance)
    
class CheckAccount(Account):
    def ___ini___(self, account_number, customer, overdraft_limit):
        super().___ini___(account_number, customer)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit < amount:
            raise ValueError("Insufficient Balance")
        else:
            self.balance -= amount

class Customer:
    def __init__(self, account_name, phone_number, email, address):
        self.account_name = account_name
        self.phone_number = phone_number
        self.email = email
        self.accounts =[]

    def add_account(self, account):
        self.accounts.append(account)


class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount =amount
        self.datetime = datetime.datetime.now()



    def __str__(self):
        return f'{self.datetime} Transaction type: {self.transaction_type}: {self.amount}'
    



customer1 = Customer("Ugwu Chika", "081-248-191-38", "docrihan@gmail.com", "Ikeja Mall")
customer2 = Customer("Mich Sidi", "081-210-597-14", "coscomek@gmail.com", "Kwuchiyako extention")
account1 = Account("0060493211", customer1)
acct1 = Account("8121059714", customer2)
# account1 = Account()
customer1.add_account(account1)
account1.deposit(40000)
account1.withdraw(5000)
account1.deposit(35000)
account1.deposit(5000)
acct1.deposit(300000)
account1.withdraw(3000)
# acct = Account
#print(account1.get_transaction())
# account1.save_transactions()
# account1.get_transaction()



        
    

# list1 = ["Zik", "Kay", "Ben", "Oramz", "Smart"]

# dict1 = {}
# #print(dict(enumerate(list1)))


# class List:
#     def __init__(self, my_list):
#         self.my_list = my_list
#         self.lists = []
#         self.my_dict = {}


# def list_to_dict(my_list):
    
#     my_dict = {}
#     return my_dict(dict(enumerate(my_list)))
# my_list = ["Zik", "Kay", "Ben", "Oramz", "Smart"]
# my_dict = list_to_dict(my_list)

# def list_to_dict(input_list):
#     my_dict = {}
#     for i, lst in enumerate(input_list):
#         my_dict[i] = lst
#     return my_dict
# list_to_dict("Kay")

def list_to_dict(list1):
    return {key: lst for key, lst in enumerate(list1)}

my_list = ["Zik", "Kay", "Ben", "Oramz", "Smart"]
my_dict = list_to_dict(my_list)

# print(my_dict)


def create_dictionary(keys, values):
    return dict(zip(keys, values))

def find_key_with_max_value(dictionary):
    return max(dictionary, key=dictionary.get)

def average_values(dictionary):
    return sum(dictionary.values()) / len(dictionary)


keys = ["Zik", "Kay", "Ben", "Oramz", "Smart"]
values = [10, 80, 30, 49, 50]

dictionary = create_dictionary(keys, values)
key_with_max_value = find_key_with_max_value(dictionary)
average_value = average_values(dictionary)

print(dictionary)
print(key_with_max_value)
print(average_value)


        
