class Time:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def __str__(self):
        return f"{self.nome} ({len(self.jogadores)} jogadores)"