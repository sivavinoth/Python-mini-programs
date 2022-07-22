class base :
    def __init__(self ,name ,roll,dept):

        self.name = name

        self.roll = roll
        self.dept = dept

class derived(base):

    def __init__(self ,name ,roll,dept ,dob):
        base.__init__(self,name,roll,dept)

        self.dob = dob

obj = derived(name="vinoth",dept="cse",roll=52,dob=29)

print(f"your name is : {obj.name} and your age is : {obj.dob} and your studying {obj.dept} department")