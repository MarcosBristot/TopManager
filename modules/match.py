import random

class Partida:
    def __init__(self, time_casa, time_visitante, estadio):
        self.time_casa = time_casa
        self.time_visitante = time_visitante
        self.estadio = estadio
        self.placar_casa = 0
        self.placar_visitante = 0
        self.eventos_partida = [] # Lista para armazenar os lances da partida

    def calcular_forca(self, time):
        if not time.jogadores:
            return 0
        
        soma_overall = 0
        for jogador in time.jogadores:
            soma_overall += jogador.overall

        media_overall = soma_overall / len(time.jogadores)
        return media_overall

    def _selecionar_jogador_para_evento(self, time, tipo_evento="qualquer"):
        """Seleciona um jogador aleatório do time para um evento.
        Pode ser expandido para dar preferência a posições específicas
        para certos eventos (ex: atacantes para gols).
        """
        if not time.jogadores:
            return None
        
        # Simplesmente seleciona um jogador aleatório por enquanto
        return random.choice(time.jogadores)

    def simular(self):
        self.placar_casa = 0
        self.placar_visitante = 0
        self.eventos_partida = []

        forca_casa = self.calcular_forca(self.time_casa)
        forca_visitante = self.calcular_forca(self.time_visitante)

        self.eventos_partida.append(f"Começa a partida entre {self.time_casa.nome} e {self.time_visitante.nome} no estádio {self.estadio}!")
        self.eventos_partida.append(f"Força {self.time_casa.nome}: {forca_casa:.2f} | Força {self.time_visitante.nome}: {forca_visitante:.2f}")

        for minuto in range(1, 91):
            # Chance base de um evento "importante" acontecer no minuto
            if random.random() < 0.1: # 10% de chance de algo relevante no minuto

                # Probabilidade de Gol
                # Ajustar os multiplicadores para tornar mais ou menos provável
                chance_gol_casa = (forca_casa / (forca_casa + forca_visitante)) * 0.2 # Chance relativa de gol para casa
                chance_gol_visitante = (forca_visitante / (forca_casa + forca_visitante)) * 0.2 # Chance relativa de gol para visitante

                rand_val = random.random()

                if rand_val < chance_gol_casa:
                    self.placar_casa += 1
                    marcador = self._selecionar_jogador_para_evento(self.time_casa, "gol")
                    nome_marcador = marcador.nome if marcador else "Jogador Desconhecido"
                    self.eventos_partida.append(f"{minuto}' - GOL! {self.time_casa.nome}! Marcado por {nome_marcador}. ({self.placar_casa} - {self.placar_visitante})")
                
                elif rand_val < chance_gol_casa + chance_gol_visitante:
                    self.placar_visitante += 1
                    marcador = self._selecionar_jogador_para_evento(self.time_visitante, "gol")
                    nome_marcador = marcador.nome if marcador else "Jogador Desconhecido"
                    self.eventos_partida.append(f"{minuto}' - GOL! {self.time_visitante.nome}! Marcado por {nome_marcador}. ({self.placar_casa} - {self.placar_visitante})")
                
                else: # Se não foi gol, pode ser cartão ou lesão
                    # Chance de Cartão (menor que gol)
                    if random.random() < 0.03: # 3% de chance de cartão, se houve um "evento importante"
                        time_evento = random.choice([self.time_casa, self.time_visitante])
                        jogador_evento = self._selecionar_jogador_para_evento(time_evento)
                        if jogador_evento:
                            tipo_cartao = "Amarelo" if random.random() < 0.8 else "Vermelho" # 80% amarelo, 20% vermelho
                            self.eventos_partida.append(f"{minuto}' - Cartão {tipo_cartao} para {jogador_evento.nome} ({time_evento.nome}).")
                    
                    # Chance de Lesão (ainda menor)
                    elif random.random() < 0.01: # 1% de chance de lesão, se houve um "evento importante" e não foi cartão
                        time_evento = random.choice([self.time_casa, self.time_visitante])
                        jogador_evento = self._selecionar_jogador_para_evento(time_evento)
                        if jogador_evento:
                            self.eventos_partida.append(f"{minuto}' - Lesão! {jogador_evento.nome} ({time_evento.nome}) parece ter se machucado.")
            
            if minuto == 45:
                self.eventos_partida.append(f"Fim do primeiro tempo: {self.time_casa.nome} {self.placar_casa} - {self.placar_visitante} {self.time_visitante.nome}")

        self.eventos_partida.append(f"Fim de jogo! Resultado final: {self.time_casa.nome} {self.placar_casa} - {self.placar_visitante} {self.time_visitante.nome}")
        
        print("\n--- LOG DA PARTIDA ---")
        for evento in self.eventos_partida:
            print(evento)
        print("----------------------")

        return {
            "casa": self.placar_casa,
            "visitante": self.placar_visitante,
            "eventos": self.eventos_partida
        }