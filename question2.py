class Dog:
    def __init__(self, name, age,coatcolor):
        self.name =name
        self.age =age
        self.coatcolar =coatcolor
    def __str__(self):
        return f"Name:{self.name} \n Age: {self.age} "  
    def get_info(self):
        return self.coatcolar
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coatcolor):
        super().__init__(name, age, coatcolor) 
    def country_origin(self,country):
        self.country =country
    def vaccin(self,vaccinated):
        self.vaccinated =vaccinated
    def get_country_origin(self):
        return self.country
    def get_vaccin(self):
        return self.vaccinated          
class Bulldog(Dog):
    def __init__(self, name, age, coatcolor):
        super().__init__(name, age, coatcolor)
    def country_origin(self,country):
        self.country =country
    def vaccin(self,vaccinated):
        self.vaccinated =vaccinated 
    def get_country_origin(self):
        return self.country
    def get_vaccin(self):
        return self.vaccinated          
obj1 =JackRussellTerrier("Binny","5","black") 
obj1.country_origin("india")
obj1.vaccin("yes")
print(obj1.__str__())
print("coatcolor:",obj1.get_info())
print("Country of origin: ",obj1.get_country_origin())
print("vacinated: ",obj1.get_vaccin())
obj2=Bulldog("jimmy","4","white")      
obj2.country_origin("Germany")
obj2.vaccin("No")
print(obj2.__str__())
print("coatcolor:",obj2.get_info())
print("Country of origin: ",obj2.get_country_origin())
print("vacinated: ",obj2.get_vaccin())