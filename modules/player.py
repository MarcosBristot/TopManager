class Jogador:
    def __init__(self, nome, idade, overall, posicao):
        self.nome = nome
        self.idade = idade
        self.overall = overall
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome} ({self.posicao}) - Overall: {self.overall}"