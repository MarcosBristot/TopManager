class Jogador:
    def __init__(self, id, nome, idade, overall, posicao):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.overall = overall
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome} ({self.posicao}) - Overall: {self.overall}"