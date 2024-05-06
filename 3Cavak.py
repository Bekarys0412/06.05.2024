class Car:

    def __init__(self, mark, model, age):
        self.mark=mark
        self.model=model
        self.age=age

    def information(self):
        print("Көліктін аты "+ self.mark, self.model, "жылы " + str(self.age))

P1 =Car("Tayoto", "Camry", 2024)
P1.information()
P1 =Car("Tayoto", "Camry", 2023)
P1.information()