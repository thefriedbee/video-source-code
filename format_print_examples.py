# examples of print methods


# Tom, born in 2000, is a freshman student with GPA 3.1415926
# Bob, born in 1995, is a graduate student with GPA 4
p1 = ['Tom', 'freshman', {'gpa': 3.1415926, 'dob': 2000}]
p2 = ['Bob', 'graduate', {'gpa': 4, 'dob': 1995}]



# bad example 1
my_str = p1[0] + ', born in ' + str(p1[2]['dob']) + ', is a ' + p1[1] + ' student with GPA ' + str(p1[2]['gpa'])
print(my_str)

# bad example 2
print(p1[0], ', born in ', p1[2]['dob'], ', is a ', p1[1], ' student with GPA ', p1[2]['gpa'], sep="")




# format string
my_str = '{}, born in {}, is a {} student with GPA {}'.format(p1[0], p1[2]['dob'], p1[1], p1[2]['gpa'])
print(my_str)

my_str = '{0}, born in {2[dob]}, is a {1} student with GPA {2[gpa]}'.format(p1[0], p1[1], p1[2])
print(my_str)

my_str = '{0[0]}, born in {0[2][dob]}, is a {0[1]} student with GPA {0[2][gpa]}'.format(p1)
print(my_str)





# can also access attributes in this way
class Person():
    def __init__(self, name, role, dob, gpa):
        self.name = name
        self.role = role
        self.dob  = dob
        self.gpa  = gpa

p1 = Person('Tom', 'freshman', '2000', '3.1415936')
print('{0.name}, born in {0.dob}, is a {0.role} student with GPA {0.gpa}'.format(p1))



# locate by keyword arguments
print('{name} is born in {dob}'.format(name='Tom', dob='2000'))

# usage: unload a dictionary or list
mini_p1 = {'name': 'Tom', 'dob':'2000', 'useless':'blablabla' }
print('{name} is born in {dob}'.format(**mini_p1))

mini_p1 = ['Tom', 'freshman', {'gpa':3.1415926, 'dob': 2000}]
print('{0} is born in {2[dob]}'.format(*mini_p1))





# old-school format
# s: str;
# d: decimal integer;
# f: float
print('%s is born in %d' % ('Tom', 2000.2))
print('%s is born in %f' % ('Tom', 2000))
print('%s is born in %.2f' % ('Tom', 2000))






# formatting using colon symbol
mini_p1 = ['Tom', 'freshman', {'gpa':3.1415926, 'dob': 2000}]
mini_p2 = ['Bob', 'graduate', {'gpa':4, 'dob': 1995}]
print('{0} is born in {2[dob]:05}'.format(*mini_p1))
print('{0} is born in {2[dob]:05.2f}'.format(*mini_p1))

print('{0} is born in {2[dob]:.2f}'.format(*mini_p1))
print('{0} is born in {2[dob]:.2f}'.format(*mini_p2))

mini_p1 = ['Tom', 'freshman', {'gpa':3.1415926, 'dob': 2000, 'salary': 12345678}]
mini_p2 = ['Bob', 'graduate', {'gpa':4, 'dob': 1995, 'salary': 12345}]
print('{0} has salary ${2[salary]:>20,.2f}/year'.format(*mini_p1))
print('{0} has salary ${2[salary]:>20,.2f}/year'.format(*mini_p2))

# format-specification-language
# https://docs.python.org/3/library/string.html#format-specification-mini-language





# format also works for datetime, like functions strftime(), strptime()
from datetime import datetime
mini_p1 = ['Tom', 'freshman', {'gpa':3.1415926, 'dob': '2000-01-01', 'salary': 12345678}]
mini_p1[2]['dob'] = datetime.strptime(mini_p1[2]['dob'], '%Y-%m-%d')

print('{0} was born in {2[dob]:%B, %d, %Y}, on a quiet {2[dob]: %A}'.format(*mini_p1))







# last but not the least. duck typing
from datetime import datetime

class Person():
    def __init__(self, name, role, dob, gpa, salary):
        self.name = name
        self.role = role
        self.dob  = datetime.strptime(dob, '%Y-%m-%d')
        self.gpa  = gpa
        self.salary = salary
    def __str__(self):
        # summary sentense
        return '{0.name}, born in {0.dob}, is a {0.role} student with GPA {0.gpa}'.format(self)

    def __format__(self, format_settings='summary'):
        if format_settings == 'salary':
            return '{0.name} is has salary ${0.salary:>20,.2f}/year'.format(self)
        else:
            return self.__str__()


p1 = Person('Tom', 'freshman', '2000-01-01', 3.1415926, 12345678)
p2 = Person('Bob', 'graduate', '1995-12-31', 4, 12345)
print(p1)
print('{:salary}'.format(p2))
print('{:summary}'.format(p2))




