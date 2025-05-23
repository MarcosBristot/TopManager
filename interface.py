import pygame
import sys
from modules.match import Partida

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("TopManager")

# Fonte
fonte = pygame.font.Font(None, 36)
fonte_eventos = pygame.font.Font(None, 24) # Fonte menor para a lista de eventos


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


def tela_exibir_resultado(time_casa, time_visitante, resultado_partida):
    """
    Exibe o resultado da partida, incluindo o placar e uma lista de eventos.
    
    resultado_partida é um dicionário: {"casa": gols_casa, "visitante": gols_visitante, "eventos": lista_de_eventos}
    """
    rodando = True
    scroll_y = 0 # Para permitir rolar a lista de eventos se for muito longa
    altura_linha_evento = 25 # Altura aproximada de cada linha de evento

    while rodando:
        tela.fill(BRANCO)
        
        # Título
        titulo_surface = fonte.render("Resultado da Partida", True, PRETO)
        titulo_rect = titulo_surface.get_rect(center=(LARGURA / 2, ALTURA * 0.05))
        tela.blit(titulo_surface, titulo_rect)

        # Placar
        placar_texto = f"{time_casa.nome} {resultado_partida['casa']} - {resultado_partida['visitante']} {time_visitante.nome}"
        placar_surface = fonte.render(placar_texto, True, PRETO)
        placar_rect = placar_surface.get_rect(center=(LARGURA / 2, ALTURA * 0.12))
        tela.blit(placar_surface, placar_rect)

        # Área para os eventos da partida
        y_eventos_inicio = ALTURA * 0.20
        altura_max_eventos = ALTURA * 0.60 # Define uma área para os eventos
        x_eventos = LARGURA * 0.05
        largura_eventos = LARGURA * 0.9

        # Desenha uma borda para a área de eventos (opcional)
        # pygame.draw.rect(tela, PRETO, (x_eventos - 2, y_eventos_inicio - 2, largura_eventos + 4, altura_max_eventos + 4), 1)

        # Exibe os eventos da partida
        y_atual = y_eventos_inicio - scroll_y
        for evento_texto in resultado_partida["eventos"]:
            if y_atual >= y_eventos_inicio and y_atual < y_eventos_inicio + altura_max_eventos - altura_linha_evento:
                evento_surface = fonte_eventos.render(evento_texto, True, PRETO)
                tela.blit(evento_surface, (x_eventos, y_atual))
            y_atual += altura_linha_evento
        
        # Botão Voltar
        largura_botao_voltar = LARGURA * 0.15
        altura_botao_voltar = ALTURA * 0.08
        x_botao_voltar = (LARGURA - largura_botao_voltar) / 2 # Centralizado
        y_botao_voltar = ALTURA * 0.85
        desenhar_botao("Voltar", x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar, AZUL)

        for evento_pygame in pygame.event.get():
            if evento_pygame.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento_pygame.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if botao_clicado(x_botao_voltar, y_botao_voltar, largura_botao_voltar, altura_botao_voltar, mouse_pos):
                    rodando = False # Volta para a tela anterior (menu de simulação ou principal)
                    return # Sai da função tela_exibir_resultado
                
                # Scroll com o mouse (rodinha)
                if evento_pygame.button == 4: # Roda para cima
                    scroll_y = max(0, scroll_y - altura_linha_evento)
                elif evento_pygame.button == 5: # Roda para baixo
                    # Calcula o scroll máximo para não rolar além do conteúdo
                    altura_total_eventos = len(resultado_partida["eventos"]) * altura_linha_evento
                    max_scroll = max(0, altura_total_eventos - altura_max_eventos)
                    scroll_y = min(max_scroll, scroll_y + altura_linha_evento)


        pygame.display.flip()

# Não se esqueça de que a função tela_simular_partida() em interface.py agora vai chamar:
# resultado = Partida(time_casa, time_visitante, "Estádio Central").simular() # 'resultado' agora é o dicionário
# tela_exibir_resultado(time_casa, time_visitante, resultado)
