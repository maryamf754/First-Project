class Student:
    def __init__(self,fname,lname,score):
        self.fname = fname
        self.lname = lname
        self.__score = score
    def fullname(self):
        return f'{self.fname} {self.lname}'    
    def email(self):
        return f'{self.fname}_{self.lname}@gmail.com'
    def get_score(self,username,password):
        if username == 'admin' and password == '123':
            return self.__score
        else:
           return 'Username or Password not valid!!!'
    def set_score(self,new_score):
        self.__score = new_score

    def __str__(self):
        return f'{self.fname} {self.lname}'
    def __add__(self, other):
        return self.__score + other.__score
    def __len__(self):
        return len(self.fname) + len(self.lname)


class Student_Python(Student):
   def fullname(self):
       return f'-{self.fname}\t{self.lname}'

print('**')
print("mmm")
print("888")
sp1 = Student_Python('alireza','moradi', 16)
print(sp1.fullname())
s1 = Student('ali', 'rezayee',20)
s2 = Student('taha', 'moradi', 17)
print(s1 + s2)
print(s1.__add__(s2))
print(s1.fullname())
print('********************')
print(len(s1))