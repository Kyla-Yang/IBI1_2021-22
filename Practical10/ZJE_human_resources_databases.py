class staff():
#set up a class named staff
    def __init__(self, first_name, last_name, location, role):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.role = role
#give four varibles attributes respectively
    def f(self):
        w = self.first_name + ' ' + self.last_name + ' ' + self.location + ' ' + self.role
        return w
        print(w)
#collect the information into one line
#take an example:
Robot_Young = staff('Robot', 'Young', 'Edinburge', 'Faculty')
print(staff.f(Robot_Young))

