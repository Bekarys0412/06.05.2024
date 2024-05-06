class Person:

    def __init__(self,name,age,famila=""):
        self.name =name
        self.age=age
        self.famila=famila
    def my_method(self):
        if self.famila:
            print("менін аты-жөнім "+ self.name,self.famila,"жасым " + str(self.age))
        else:
            P2
P1 =Person("Dauren",18,"Erbol")
P2 =Person(name="Dauren",age=18,)
P1.my_method()
P2.my_method()