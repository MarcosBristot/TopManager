import random

class Partida:
    def __init__(self, time_casa, time_visitante, estadio):
        self.time_casa = time_casa
        self.time_visitante = time_visitante
        self.estadio = estadio

    def calcular_forca(self, time):
        if not time.jogadores:
            return 0
        
        soma_overall = 0
        for jogador in time.jogadores:
            soma_overall += jogador.overall

        media_overall = soma_overall / len(time.jogadores)

        return media_overall

    def simular(self):
        forca_casa = self.calcular_forca(self.time_casa)
        forca_visitante = self.calcular_forca(self.time_visitante)

        print(f"Simulando partida entre {self.time_casa.nome} e {self.time_visitante.nome}")

        print("\nTime da Casa:", self.time_casa.nome)
        for jogador in self.time_casa.jogadores:
            print(f" - {jogador.nome}")

        print("\nTime Visitante:", self.time_visitante.nome)
        for jogador in self.time_visitante.jogadores:
            print(f" - {jogador.nome}")
            
        print(f"\n{self.time_casa.nome} ({forca_casa: }) vs {self.time_visitante.nome} ({forca_visitante: })")
        print(f"Local: {self.estadio}")

        gols_casa = random.randint(0, int(forca_casa / 10))  # Exemplo: converte força em gols
        gols_visitante = random.randint(0, int(forca_visitante / 10))

        print(f"Resultado Final: {self.time_casa.nome} {gols_casa} - {gols_visitante} {self.time_visitante.nome}")

        return {"casa": gols_casa, "visitante": gols_visitante}
    
    def gerar_gols(self, forca):
        chance_base = forca / 20

        gols = 0
        for _ in range(3):
            if random.random() < chance_base:
                gols += 1
            
        return gols