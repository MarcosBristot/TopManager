class Partida:
    def __init__(self, time_casa, time_visitante):
        self.time_casa = time_casa
        self.time_visitante = time_visitante

    def simular(self):
        print(f"{self.time_casa.nome} vs {self.time_visitante.nome}")
        print("Resultado: 1-0")  # Exemplo fixo