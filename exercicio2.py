import abc

class Atletas:
    def __init__(self,nome,idade,pontuacao,categoria):
        self.nome = nome
        self.idade = idade
        self.pontuacao = pontuacao
        self.categoria = categoria

class Campeonato(abc.ABC):
    def __init__(self,nome,local,premiacao,patrocinadores,lista_de_inscritos):
        self.nome = nome
        self.local = local
        self.premiacao = premiacao
        self.patrocinadores = patrocinadores
        self.lista_de_inscritos = []
    
    @abc.abstractmethod
    def pontuacao(self):
        pass
    
    @abc.abstractmethod
    def inscrever(self,atleta):
        self.lista_de_inscritos.append(atleta)
    
class Amador(Campeonato):
    def __init__(self, nome, local, premiacao,patrocinadores):
        super().__init__(nome, local, premiacao, patrocinadores)
        self.categoria = 'amador'
    
    def pontuacao(self,pontuacao):
        self.pontuacao = pontuacao + 10
    
    def inscrever(self,atleta):
        return super().inscrever(atleta)
        
        
class Profissional(Campeonato):
    def __init__(self, nome, local, premiacao, patrocinadores):
        super().__init__(nome, local, premiacao, patrocinadores)
        self.categoria = "profissional"
        
    def pontuacao(self,pontuacao):
        self.pontuacao = pontuacao + 50
        
    def inscrever(self,atleta):
        if atleta.categoria == 'profissional' or atleta.categoria == 'lenda':
            return super().inscrever(atleta)

class Lenda(Campeonato):
    def __init__(self, nome, local, premiacao, patrocinadores):
        super().__init__(nome, local, premiacao, patrocinadores)
        self.categoria = "lenda"

    def pontuacao(self,pontuacao):
        self.pontuacao = pontuacao + 100
        
    def inscrever(self,atleta):
        if atleta.categoria == 'lenda':
            return super().inscrever(atleta)