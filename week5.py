#Defining a class
class Smartphone: 
    def __init__(self, model):
        self.model = model

    def differance(self):
        print(f"{self.model} Smartphone") 
    
         

Smartphone1 = Smartphone("model")
print(Smartphone1.model)   

#Polymorphism

class iPhone(Smartphone): 
    def differance(self):
        print(f"{self.model} This is an iPhone") 

class Samsung(Smartphone): 
    def differance(self):
        print(f"{self.model} This is a Samsung")

def Smartphone_OS(display):
    display.differance()

iPhone2 = iPhone("iPhone 16  takes better photos")
Samsung2 = Samsung("Samsung Galaxy S21 Ultra takes even better photos")

Smartphone_OS(iPhone2)
Smartphone_OS(Samsung2)



