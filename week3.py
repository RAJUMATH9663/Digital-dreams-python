class phone:
    def make_call(self):
        print("make the call")
    def play_game(self):
        print("play game")
p1=phone()
p1.make_call()
p1.play_game()


class emp:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def emp_det(self):
        print("name of emp",self.name)
        print("age of emp",self.age)
        print("salary of emp",self.salary)
        print("gender of emp",self.gender)
e1=emp("raju",21,8500,"male")        
e1.emp_det()    


class vehicle:
    def __init__(self,milage,cost):
        self.milage=milage
        self.cost=cost
    def show_det(self):
        print("i am a vechile")
        print("milage of the car",self.milage)
        print("cost of car",self.cost)
r1=vehicle(20,10000000)
r1.show_det()

class Car(vehicle):
    def show_Car(self):
        print("i am not car")
c1=Car(200,200)
c1.show_det()
c1.show_Car()




class Car(vehicle):
    def __init__(self,milage,cost,tyre,hp):
        super().__init__(milage,cost)
        self.tyre=tyre
        self.hp=hp
    def show_Car_det(self):
        print("i am car")
        print("tyre",self.tyre)
        print("hp is ",self.hp)
c1=Car(20,200,1,300)
c1.show_det()
c1.show_Car_det()


# Parent class 1
class parents1:
    def assign_str_one(self, str1):
        self.str1 = str1

    def show_str_one(self):
        return self.str1


# Parent class 2
class parents2:
    def assign_str_two(self, str2):
        self.str2 = str2

    def show_str_two(self):
        return self.str2


# Derived class (Multiple Inheritance)
class derived(parents1, parents2):
    def assign_str_three(self, str3):
        self.str3 = str3

    def show_str_three(self):
        return self.str3


# Object creation
d1 = derived()

# Assign values
d1.assign_str_one("one")
d1.assign_str_two("two")
d1.assign_str_three("three")

# Display values
print(d1.show_str_one())
print(d1.show_str_two())
print(d1.show_str_three())


























