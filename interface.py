import pygame
import sys
import random 
from modules.match import Partida 

# Cores e Fontes (mantenha as que você já tem)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0) 
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

pygame.init() 

LARGURA = 800 
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA)) 
# pygame.display.set_caption("TopManager") 

fonte = pygame.font.Font(None, 36) 
fonte_eventos = pygame.font.Font(None, 24) 
clock = pygame.time.Clock()


# Função para desenhar botões
def desenhar_botao(texto, x, y, largura, altura, cor):
    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    texto_surface = fonte.render(texto, True, PRETO)
    texto_rect = texto_surface.get_rect(center=(x + largura / 2, y + altura / 2))
    tela.blit(texto_surface, texto_rect)

# Função para verificar se o botão foi clicado
def botao_clicado(x, y, largura, altura, mouse_pos):
    return x <= mouse_pos[0] <= x + largura and y <= mouse_pos[1] <= y + altura

# Função para exibir o menu principal
def menu_principal():
    while True:
        tela.fill(BRANCO)

        largura_botao = LARGURA * 0.25
        altura_botao = ALTURA * 0.1
        espacamento = ALTURA * 0.05
        x_botao = (LARGURA - largura_botao) / 2
        y_botao1 = (ALTURA - (3 * altura_botao + 2 * espacamento)) / 2
        y_botao2 = y_botao1 + altura_botao + espacamento
        y_botao3 = y_botao2 + altura_botao + espacamento

        # Desenha os botões
        desenhar_botao("Listar Clubes", x_botao, y_botao1, largura_botao, altura_botao, VERDE)
        desenhar_botao("Simular Partida", x_botao, y_botao2, largura_botao, altura_botao, VERDE)
        desenhar_botao("Sair", x_botao, y_botao3, largura_botao, altura_botao, VERMELHO)

        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verifica se o botão "Listar Clubes" foi clicado
                if botao_clicado(x_botao, y_botao1, largura_botao, altura_botao, (x, y)):
                    return "listar_clubes"
                # Verifica se o botão "Simular Partida" foi clicado
                if botao_clicado(x_botao, y_botao2, largura_botao, altura_botao, (x, y)):
                    return "simular_partida"
                # Verifica se o botão "Sair" foi clicado
                if botao_clicado(x_botao, y_botao3, largura_botao, altura_botao, (x, y)):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

# Função para listar clubes
def tela_listar_clubes(times):
    while True:
        tela.fill(BRANCO)
        y = ALTURA * 0.05
        for time in times:
            texto_surface = fonte.render(f"Clube: {time.nome}", True, PRETO)
            tela.blit(texto_surface, (LARGURA * 0.05, y))
            y += ALTURA * 0.05
            for jogador in time.jogadores:
                texto_surface = fonte.render(f"  Jogador: {jogador}", True, PRETO)
                tela.blit(texto_surface, (LARGURA * 0.1, y))
                y += ALTURA * 0.04

        desenhar_botao("Voltar", LARGURA * 0.05, ALTURA * 0.85, LARGURA * 0.15, ALTURA * 0.08, AZUL)

        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if botao_clicado(LARGURA * 0.05, ALTURA * 0.85, LARGURA * 0.15, ALTURA * 0.08, (x, y)):
                    return

        pygame.display.flip()

# Função para simular partida
def tela_simular_partida(times):
    print("Entrando na tela de simulação de partida")
    selecionando = True
    time_casa = None
    time_visitante = None
    
    while selecionando:
        tela.fill(BRANCO)
        y = ALTURA * 0.1
        
        for i, time in enumerate(times):
            texto_surface = fonte.render(f"{i + 1}. {time.nome}", True, PRETO)
            tela.blit(texto_surface, (LARGURA * 0.1, y))
            y += ALTURA * 0.08

        desenhar_botao("Voltar", LARGURA * 0.05, ALTURA * 0.85, LARGURA * 0.15, ALTURA * 0.08, AZUL)

        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(f"Clique detectado em: {x}, {y}")  # Teste para ver se o clique está sendo reconhecido
                
                if botao_clicado(LARGURA * 0.05, ALTURA * 0.85, LARGURA * 0.15, ALTURA * 0.08, (x, y)):
                    print("Botão voltar pressionado")  # Teste para ver se o botão está sendo acionado
                    return
                
                for i in range(len(times)):
                    if botao_clicado(LARGURA * 0.1, ALTURA * 0.1 + i * ALTURA * 0.08, 200, 40, (x, y)):
                        if not time_casa:
                            time_casa = times[i]
                        elif not time_visitante:
                            time_visitante = times[i]
                            print(f"Times selecionados: {time_casa.nome} vs {time_visitante.nome}")  # Teste
                            selecionando = False
                            break  # Garante que o loop de eventos pare após a seleção
        
        pygame.display.flip()  # Atualiza a tela a cada iteração
    
    print("Simulando partida...")
    resultado = Partida(time_casa, time_visitante, "Estádio Central").simular()
    print(f"Resultado gerado: {resultado}")
    
    tela_exibir_resultado(time_casa, time_visitante, resultado)

def desenhar_botao(texto, x, y, largura, altura, cor_fundo, cor_texto=PRETO):
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
    texto_surface = fonte.render(texto, True, cor_texto)
    texto_rect = texto_surface.get_rect(center=(x + largura / 2, y + altura / 2))
    tela.blit(texto_surface, texto_rect)

def botao_clicado(x, y, largura, altura, mouse_pos):
    return x <= mouse_pos[0] <= x + largura and y <= mouse_pos[1] <= y + altura

def extrair_minuto_do_evento(evento_str):
    try:
        if "' - " in evento_str:
            return int(evento_str.split("' - ")[0])
    except ValueError:
        pass
    return -1

ESTADO_PRIMEIRO_TEMPO = "PRIMEIRO_TEMPO"
ESTADO_ACRESCIMOS_PRIMEIRO_TEMPO = "ACRESCIMOS_PRIMEIRO_TEMPO"
ESTADO_INTERVALO = "INTERVALO"
ESTADO_SEGUNDO_TEMPO = "SEGUNDO_TEMPO"
ESTADO_ACRESCIMOS_SEGUNDO_TEMPO = "ACRESCIMOS_SEGUNDO_TEMPO"
ESTADO_FIM_DE_JOGO = "FIM_DE_JOGO"


def tela_exibir_resultado(time_casa, time_visitante, resultado_partida):
    rodando = True
    scroll_y = 0
    altura_linha_evento = 25

    estado_partida_atual = ESTADO_PRIMEIRO_TEMPO
    minuto_atual_jogo_simulado = 0 
    minuto_display = 0 
    tempo_no_periodo_atual = 0 

    velocidade_simulacao_ms = 150 # Mais rápido
    tempo_ultimo_incremento_minuto = pygame.time.get_ticks()

    acrescimos_1t = random.randint(1, 3) 
    acrescimos_2t = random.randint(2, 5) 
    
    eventos_todos = resultado_partida["eventos"]
    eventos_exibidos_na_tela = []
    indice_proximo_evento_na_lista_original = 0

    placar_casa_atual = 0
    placar_visitante_atual = 0

    botao_continuar_visivel = False
    texto_botao_continuar = "Continuar para 2º Tempo"

    # Processar eventos iniciais (sem minuto, como "Começa a partida", "Força")
    temp_indice = 0
    for i, evento_str in enumerate(eventos_todos):
        if extrair_minuto_do_evento(evento_str) == -1 and ("Começa a partida" in evento_str or "Força" in evento_str):
            if evento_str not in eventos_exibidos_na_tela:
                 eventos_exibidos_na_tela.append(evento_str)
            temp_indice = i + 1
        else: # Para no primeiro evento com minuto ou não inicial
            break
    indice_proximo_evento_na_lista_original = temp_indice


    while rodando:
        tempo_real_agora = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()

        for evento_pygame in pygame.event.get():
            if evento_pygame.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento_pygame.type == pygame.MOUSEBUTTONDOWN:
                largura_botao_voltar = LARGURA * 0.20
                altura_botao_voltar = ALTURA * 0.07
                x_botao_voltar = LARGURA * 0.05 
                y_botao_voltar = ALTURA * 0.90
                if botao_clicado(x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar, mouse_pos):
                    rodando = False
                    return # Sai da tela de resultado

                if botao_continuar_visivel:
                    largura_botao_cont = LARGURA * 0.40
                    altura_botao_cont = ALTURA * 0.07
                    x_botao_cont = (LARGURA - largura_botao_cont) / 2
                    y_botao_cont = ALTURA * 0.80 
                    if botao_clicado(x_botao_cont, y_botao_cont, largura_botao_cont, altura_botao_cont, mouse_pos):
                        if estado_partida_atual == ESTADO_INTERVALO:
                            estado_partida_atual = ESTADO_SEGUNDO_TEMPO
                            minuto_atual_jogo_simulado = 45 
                            tempo_no_periodo_atual = 0
                            botao_continuar_visivel = False
                            if "Começa o segundo tempo!" not in eventos_exibidos_na_tela:
                                eventos_exibidos_na_tela.append("Começa o segundo tempo!")
                            tempo_ultimo_incremento_minuto = pygame.time.get_ticks() 

                if evento_pygame.button == 4: scroll_y = max(0, scroll_y - altura_linha_evento)
                elif evento_pygame.button == 5:
                    altura_total_eventos_visiveis = len(eventos_exibidos_na_tela) * altura_linha_evento
                    altura_area_eventos = ALTURA * 0.60 
                    max_scroll = max(0, altura_total_eventos_visiveis - altura_area_eventos)
                    scroll_y = min(max_scroll, scroll_y + altura_linha_evento)

        simulacao_ativa = estado_partida_atual not in [ESTADO_INTERVALO, ESTADO_FIM_DE_JOGO]

        if simulacao_ativa and tempo_real_agora - tempo_ultimo_incremento_minuto > velocidade_simulacao_ms:
            tempo_no_periodo_atual += 1
            minuto_atual_jogo_simulado +=1 
            tempo_ultimo_incremento_minuto = tempo_real_agora

            if estado_partida_atual == ESTADO_PRIMEIRO_TEMPO:
                minuto_display = tempo_no_periodo_atual
                if tempo_no_periodo_atual >= 45:
                    estado_partida_atual = ESTADO_ACRESCIMOS_PRIMEIRO_TEMPO
                    msg_acrescimo = f"Intervalo: {acrescimos_1t} minuto(s) de acréscimo no 1º tempo."
                    if msg_acrescimo not in eventos_exibidos_na_tela:
                        eventos_exibidos_na_tela.append(msg_acrescimo)
                    tempo_no_periodo_atual = 0 

            elif estado_partida_atual == ESTADO_ACRESCIMOS_PRIMEIRO_TEMPO:
                minuto_display = 45 
                if tempo_no_periodo_atual >= acrescimos_1t:
                    estado_partida_atual = ESTADO_INTERVALO
                    botao_continuar_visivel = True
                    # O evento "Fim do primeiro tempo..." de match.py será pego pelo loop de eventos abaixo

            elif estado_partida_atual == ESTADO_SEGUNDO_TEMPO:
                minuto_display = 45 + tempo_no_periodo_atual
                if tempo_no_periodo_atual >= 45: 
                    estado_partida_atual = ESTADO_ACRESCIMOS_SEGUNDO_TEMPO
                    msg_acrescimo_2t = f"Fim do Tempo Regulamentar: {acrescimos_2t} minuto(s) de acréscimo no 2º tempo."
                    if msg_acrescimo_2t not in eventos_exibidos_na_tela:
                        eventos_exibidos_na_tela.append(msg_acrescimo_2t)
                    tempo_no_periodo_atual = 0 
            
            elif estado_partida_atual == ESTADO_ACRESCIMOS_SEGUNDO_TEMPO:
                minuto_display = 90
                if tempo_no_periodo_atual >= acrescimos_2t:
                    estado_partida_atual = ESTADO_FIM_DE_JOGO
                    # O evento "Fim de jogo!..." de match.py será pego pelo loop de eventos abaixo
                    # e o placar final será garantido na seção de desenho.

        # Processar eventos do match.py
        while indice_proximo_evento_na_lista_original < len(eventos_todos):
            evento_str = eventos_todos[indice_proximo_evento_na_lista_original]
            minuto_do_evento_atual = extrair_minuto_do_evento(evento_str) # ex: 45, 90, ou -1

            processar_este_evento = False

            if minuto_do_evento_atual != -1: # Evento COM minuto (inclui agora Fim do 1T e Fim de Jogo)
                if minuto_do_evento_atual <= minuto_atual_jogo_simulado:
                    processar_este_evento = True
                else: # Evento futuro, não processar agora e não avançar o índice sobre ele
                    break 
            else: # Evento SEM minuto (ex: "Começa a partida", "Força", ou outros logs)
                  # Adicionar apenas uma vez se não for uma mensagem de acréscimo da interface 
                  # ou outras mensagens geradas pela interface.
                if evento_str not in eventos_exibidos_na_tela and \
                   not ("Acréscimo no" in evento_str or \
                        "Fim do Tempo Regulamentar:" in evento_str or \
                        "Começa o segundo tempo!" in evento_str):
                    # As mensagens "Começa a partida" e "Força" já são tratadas no início.
                    # Este 'else' pegaria outros logs sem minuto, se houver.
                    if not ("Começa a partida" in evento_str or "Força" in evento_str):
                        processar_este_evento = True

            if processar_este_evento:
                if evento_str not in eventos_exibidos_na_tela: # Evita duplicatas
                     eventos_exibidos_na_tela.append(evento_str)
                
                if "GOL!" in evento_str: 
                    try:
                        placar_str = evento_str[evento_str.rfind("(")+1:evento_str.rfind(")")]
                        p_casa, p_vis = map(int, placar_str.split(" - "))
                        placar_casa_atual = p_casa
                        placar_visitante_atual = p_vis
                    except: pass # Ignora erro de parse
                indice_proximo_evento_na_lista_original += 1
            else:
                # Se não processou (ex: evento futuro já deu break, ou evento sem minuto já exibido)
                # Se for um evento SEM MINUTO que JÁ FOI EXIBIDO, precisamos avançar o índice.
                if minuto_do_evento_atual == -1 and evento_str in eventos_exibidos_na_tela:
                    indice_proximo_evento_na_lista_original += 1
                else:
                    # Se foi um evento futuro, o break anterior já tratou.
                    # Se foi um evento sem minuto que não deve ser processado, e não está na tela,
                    # e não é para pular, então damos break para segurança.
                    break 

        tela.fill(BRANCO)
        
        sufixo_cronometro = "'"
        if estado_partida_atual == ESTADO_ACRESCIMOS_PRIMEIRO_TEMPO:
            minuto_base_display = 45
            minuto_extra_display = tempo_no_periodo_atual
            texto_cronometro = f"Tempo: {minuto_base_display} + {minuto_extra_display}'"
        elif estado_partida_atual == ESTADO_ACRESCIMOS_SEGUNDO_TEMPO:
            minuto_base_display = 90
            minuto_extra_display = tempo_no_periodo_atual
            texto_cronometro = f"Tempo: {minuto_base_display} + {minuto_extra_display}'"
        elif estado_partida_atual == ESTADO_INTERVALO:
            texto_cronometro = "Intervalo"
        elif estado_partida_atual == ESTADO_FIM_DE_JOGO:
            texto_cronometro = "Fim de Jogo"
            placar_casa_atual = resultado_partida['casa'] 
            placar_visitante_atual = resultado_partida['visitante']
        else: 
            texto_cronometro = f"Tempo: {minuto_display}'"

        tempo_surface = fonte.render(texto_cronometro, True, PRETO)
        tempo_rect = tempo_surface.get_rect(center=(LARGURA / 2, ALTURA * 0.05))
        tela.blit(tempo_surface, tempo_rect)

        placar_texto_atualizado = f"{time_casa.nome} {placar_casa_atual} - {placar_visitante_atual} {time_visitante.nome}"
        placar_surface = fonte.render(placar_texto_atualizado, True, PRETO)
        placar_rect = placar_surface.get_rect(center=(LARGURA / 2, ALTURA * 0.12))
        tela.blit(placar_surface, placar_rect)

        y_eventos_inicio = ALTURA * 0.20
        altura_area_eventos = ALTURA * 0.58 
        x_eventos = LARGURA * 0.05
        
        y_atual_desenho = y_eventos_inicio - scroll_y
        for i, evento_texto_para_desenhar in enumerate(eventos_exibidos_na_tela):
            # Otimização para não tentar renderizar tudo se a lista for enorme
            if i > scroll_y / altura_linha_evento + (altura_area_eventos / altura_linha_evento) + 5 and y_atual_desenho > ALTURA :
                break 
            if y_atual_desenho >= y_eventos_inicio - altura_linha_evento and y_atual_desenho < y_eventos_inicio + altura_area_eventos:
                evento_surface_render = fonte_eventos.render(evento_texto_para_desenhar, True, PRETO)
                tela.blit(evento_surface_render, (x_eventos, y_atual_desenho))
            y_atual_desenho += altura_linha_evento
        
        largura_botao_voltar = LARGURA * 0.20
        altura_botao_voltar = ALTURA * 0.07
        x_botao_voltar = LARGURA * 0.05 
        y_botao_voltar = ALTURA * 0.90
        desenhar_botao("Voltar", x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar, AZUL, BRANCO)

        if botao_continuar_visivel:
            largura_botao_cont = LARGURA * 0.40
            altura_botao_cont = ALTURA * 0.07
            x_botao_cont = (LARGURA - largura_botao_cont) / 2
            y_botao_cont = ALTURA * 0.80 
            desenhar_botao(texto_botao_continuar, x_botao_cont, y_botao_cont, largura_botao_cont, altura_botao_cont, VERDE, BRANCO)

        pygame.display.flip()
        clock.tick(30)