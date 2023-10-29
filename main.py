import random


def rand_bool():
    Value = random.randint(0, 1)
    if Value == 0:
        return False
    elif Value == 1:
        return True
    else:
        print("error")


class car:

    def __init__(self, model, color, engine_type, servo_type):
        self.Model = model
        self.Color = color
        self.EngineType = engine_type
        self.ServoType = servo_type

    def Break(self):
        Value = random.randint(1, 2)
        if Value == 1:
            print(f"{self.Model} has broken its {self.EngineType} Engine")
        elif Value == 2:
            print(f"{self.Model} has broken its {self.ServoType} Servo")

    def Drive(self):
        print(f"{self.Model} started driving")
        if rand_bool():
            self.Break()


    def StopDriving(self):
        print(f"{self.Model} stopped driving")


Car = car("Audi", "Black", "Quadro", "Full")
Car.Drive()
Car.StopDriving()




