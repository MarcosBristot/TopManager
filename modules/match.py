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

# Dentro de modules/match.py

# ... (código anterior da classe Partida) ...

    def simular(self):
        self.placar_casa = 0
        self.placar_visitante = 0
        self.eventos_partida = []

        forca_casa = self.calcular_forca(self.time_casa)
        forca_visitante = self.calcular_forca(self.time_visitante)

        # Adiciona eventos iniciais que não têm minuto
        self.eventos_partida.append(f"Começa a partida entre {self.time_casa.nome} e {self.time_visitante.nome} no estádio {self.estadio}!")
        self.eventos_partida.append(f"Força {self.time_casa.nome}: {forca_casa:.2f} | Força {self.time_visitante.nome}: {forca_visitante:.2f}")

        for minuto in range(1, 91):
            # Chance base de um evento "importante" acontecer no minuto
            if random.random() < 0.1: # 10% de chance de algo relevante no minuto

                # ... (lógica de gols, cartões, lesões permanece a mesma) ...
                # Exemplo de como um gol é adicionado (mantenha sua lógica atual aqui)
                # rand_val = random.random()
                # if rand_val < chance_gol_casa:
                #     self.placar_casa += 1
                #     marcador = self._selecionar_jogador_para_evento(self.time_casa, "gol")
                #     nome_marcador = marcador.nome if marcador else "Jogador Desconhecido"
                #     self.eventos_partida.append(f"{minuto}' - GOL! {self.time_casa.nome}! Marcado por {nome_marcador}. ({self.placar_casa} - {self.placar_visitante})")
                # (etc. para gol do visitante, cartões, lesões)
                # COPIE SUA LÓGICA DE GOLS, CARTÕES E LESÕES EXISTENTE AQUI DENTRO DO LOOP DO MINUTO

                # A lógica de gols, cartões e lesões (que você já tem e estava funcionando) deve ser mantida aqui.
                # A alteração principal é nas mensagens de Fim do Primeiro Tempo e Fim de Jogo.
                
                # Chance de Gol (mantenha sua lógica)
                chance_gol_casa = (forca_casa / (forca_casa + forca_visitante)) * 0.2 
                chance_gol_visitante = (forca_visitante / (forca_casa + forca_visitante)) * 0.2

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
                
                else: 
                    if random.random() < 0.03: 
                        time_evento = random.choice([self.time_casa, self.time_visitante])
                        jogador_evento = self._selecionar_jogador_para_evento(time_evento)
                        if jogador_evento:
                            tipo_cartao = "Amarelo" if random.random() < 0.8 else "Vermelho" 
                            self.eventos_partida.append(f"{minuto}' - Cartão {tipo_cartao} para {jogador_evento.nome} ({time_evento.nome}).")
                    
                    elif random.random() < 0.01: 
                        time_evento = random.choice([self.time_casa, self.time_visitante])
                        jogador_evento = self._selecionar_jogador_para_evento(time_evento)
                        if jogador_evento:
                            self.eventos_partida.append(f"{minuto}' - Lesão! {jogador_evento.nome} ({time_evento.nome}) parece ter se machucado.")

            # AJUSTE AQUI: Adicionar minuto à mensagem de Fim do primeiro tempo
            if minuto == 45:
                self.eventos_partida.append(f"45' - Fim do primeiro tempo: {self.time_casa.nome} {self.placar_casa} - {self.placar_visitante} {self.time_visitante.nome}")

        # AJUSTE AQUI: Adicionar minuto à mensagem de Fim de jogo
        self.eventos_partida.append(f"90' - Fim de jogo! Resultado final: {self.time_casa.nome} {self.placar_casa} - {self.placar_visitante} {self.time_visitante.nome}")
        
        # Log no console (opcional, pode remover se não precisar)
        # print("\n--- LOG DA PARTIDA (match.py) ---")
        # for evento in self.eventos_partida:
        #     print(evento)
        # print("----------------------")

        return {
            "casa": self.placar_casa,
            "visitante": self.placar_visitante,
            "eventos": self.eventos_partida
        }

# ... (resto da classe Partida, como _selecionar_jogador_para_evento e calcular_forca) ...
# Certifique-se que o método _selecionar_jogador_para_evento está presente na sua classe Partida
    def _selecionar_jogador_para_evento(self, time, tipo_evento="qualquer"):
        if not time.jogadores:
            return None
        return random.choice(time.jogadores)

    def calcular_forca(self, time): # Mantenha este método
        if not time.jogadores:
            return 0
        soma_overall = sum(jogador.overall for jogador in time.jogadores)
        media_overall = soma_overall / len(time.jogadores)
        return media_overall