class Animal:
    def __init__(self, peso,patas,porte,):
        self.peso = peso
        self.patas = patas
        self.porte = porte
    
    def locomover (self):
        print("Locomovendo")

class Humano(Animal):
    def __init__(self, peso, patas, porte, inteligencia):
        super().__init__(peso, patas, porte)
        self.inteligencia = inteligencia
    
    def locomover (self):
        print("Caminhando")

class Cobra(Animal):
    def __init__(self, peso, patas, porte, veneno):
        super().__init__(peso, 0, porte)
        self.veneno = veneno
        
    def locomover (self):
        print("Rastejando")
        
gente = Humano(125,2,"Alto","10QI")
gente.locomover()
print(gente.inteligencia)
