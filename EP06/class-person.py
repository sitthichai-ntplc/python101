#################################################class Person#####################################################
class Person:                                                           
                                                                        
    def __init__(self, first_name, last_name):                           # attribute ของ class Person
        self.first_name = first_name
        self.last_name = last_name 

    def say_hello(self):                                                 # method ทักทาย
        self.word = 'สวัสดีครับ(ค่ะ) ผม(ดิฉัน) '
        return self.word
    
    def get_full_name(self):                                             # method บอกชื่อ นามสกุล
        return f'{self.first_name} {self.last_name} '

    def my_card(self):                                                   # method ยื่นนามบัตร
        return 'นี่นามบัตรผม(ดิฉัน) ยินดีที่ได้รู้จักครับ(ค่ะ)'  

#####################################คลาส Employee สืบทอดคุณสมบัติจากคลาส Person######################################
class Employee(Person):                                                 
    def __init__(self, first_name, last_name, employee_id,salary):   # attribute ของ class Employee สืบทอดคลาส (Inheritance) จาก class Person
        super().__init__(first_name, last_name)
        self.employee_id = employee_id                               
        self.salary = salary
        
    def get_employee_id(self):                                          # method คืนค่า บัตรพนักงาน
        return self.employee_id
    
    def get_saraly(self):                                               # method คืนค่า เงินเดือนพนักงาน
        return self.salary

    def get_bonus(self):                                                # method คืนค่า เงินโบนัส
        return self.salary*2.3

print('##################################### obj person1 class Person  ##################################\n')
person1 = Person('วสิทธิ์','อนุโม')    
print('\n')
print(person1.say_hello())
print(person1.get_full_name())
print(person1.my_card())
print('\n\n')

print('######################### obj emp1  class Employee สืบทอดจาก class Person #######################\n')
emp1 = Employee('ดนู','มีน้ำใจ','nt12345789',23000)
print(emp1.get_full_name()) # แสดงชื่อพนักงาน
print('เลขบัตรพนักงาน :',emp1.get_employee_id()) # แสดงเลขบัตรพนักงาน
print('เงินเดือน :',f'{emp1.get_saraly():,.2f}') # แสดงเงินเดือนพนักงาน
print('เงินโบนัส :',f'{emp1.get_bonus():.2f}') # แสดงเงินโบนัสพนักงาน
print('\n\n')

print('######################### obj emp2  class Employee สืบทอดจาก class Person #######################\n')
emp2 = Employee('นพ','ใจงาม','nt12345999',32000)
print(emp2.get_full_name()) # แสดงชื่อพนักงาน
print('เลขบัตรพนักงาน :',emp2.get_employee_id()) # แสดงเลขบัตรพนักงาน
print('เงินเดือน :',f'{emp2.get_saraly():,.2f}') # แสดงเงินเดือนพนักงาน
print('เงินโบนัส :',f'{emp2.get_bonus():.2f}') # แสดงเงินโบนัสพนักงาน
print('\n\n')

print('######################### obj emp3  class Employee สืบทอดจาก class Person #######################\n')
emp3 = Employee('พิสุทธิ์','มีเงิน','nt12344599',82000)
print(emp2.get_full_name()) # แสดงชื่อพนักงาน
print('เลขบัตรพนักงาน :',emp2.get_employee_id()) # แสดงเลขบัตรพนักงาน
print('เงินเดือน :',f'{emp3.get_saraly():,.2f}') # แสดงเงินเดือนพนักงาน
print('เงินโบนัส :',f'{emp3.get_bonus():,.2f}') # แสดงเงินโบนัสพนักงาน
print('\n\n')
print('#################################################################################################\n')