import pygame
import sys

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

# Função para desenhar botões
def desenhar_botao(texto, x, y, largura, altura, cor):
    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    texto_surface = fonte.render(texto, True, PRETO)
    texto_rect = texto_surface.get_rect(center=(x + largura / 2, y + altura / 2))
    tela.blit(texto_surface, texto_rect)

# Função para verificar se o botão foi clicado
def botao_clicado(x, y, largura, altura, mouse_pos):
    if x <= mouse_pos[0] <= x + largura and y <= mouse_pos[1] <= y + altura:
        return True
    return False

# Função para exibir o menu principal
def menu_principal():
    while True:
        tela.fill(BRANCO)

        # Calcula as posições dos botões com base em porcentagens da tela
        largura_botao = LARGURA * 0.25  # 25% da largura da tela
        altura_botao = ALTURA * 0.1     # 10% da altura da tela
        espacamento = ALTURA * 0.05     # 5% da altura da tela

        # Posiciona os botões no centro da tela
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

# Função para exibir a lista de clubes e jogadores
def tela_listar_clubes(times):
    while True:
        tela.fill(BRANCO)

        # Exibe os clubes e jogadores
        y = ALTURA * 0.05  # 5% da altura da tela
        for time in times:
            texto = f"Clube: {time.nome}"
            texto_surface = fonte.render(texto, True, PRETO)
            tela.blit(texto_surface, (LARGURA * 0.05, y))  # 5% da largura da tela
            y += ALTURA * 0.05  # 5% da altura da tela
            for jogador in time.jogadores:
                texto = f"  Jogador: {jogador}"
                texto_surface = fonte.render(texto, True, PRETO)
                tela.blit(texto_surface, (LARGURA * 0.1, y))  # 10% da largura da tela
                y += ALTURA * 0.04  # 4% da altura da tela

        # Botão de voltar
        largura_botao = LARGURA * 0.15  # 15% da largura da tela
        altura_botao = ALTURA * 0.08    # 8% da altura da tela
        x_botao = LARGURA * 0.05        # 5% da largura da tela
        y_botao = ALTURA * 0.85         # 85% da altura da tela
        desenhar_botao("Voltar", x_botao, y_botao, largura_botao, altura_botao, AZUL)

        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verifica se o botão "Voltar" foi clicado
                if botao_clicado(x_botao, y_botao, largura_botao, altura_botao, (x, y)):
                    return

        pygame.display.flip()

# Função para exibir a tela de simulação de partida
def tela_simular_partida(times):
    while True:
        tela.fill(BRANCO)

        # Exibe os times disponíveis
        y = ALTURA * 0.1  # 10% da altura da tela
        for i, time in enumerate(times):
            texto = f"{i + 1}. {time.nome}"
            texto_surface = fonte.render(texto, True, PRETO)
            tela.blit(texto_surface, (LARGURA * 0.1, y))  # 10% da largura da tela
            y += ALTURA * 0.08  # 8% da altura da tela

        # Botão de voltar
        largura_botao = LARGURA * 0.15  # 15% da largura da tela
        altura_botao = ALTURA * 0.08    # 8% da altura da tela
        x_botao = LARGURA * 0.05        # 5% da largura da tela
        y_botao = ALTURA * 0.85         # 85% da altura da tela
        desenhar_botao("Voltar", x_botao, y_botao, largura_botao, altura_botao, AZUL)

        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verifica se o botão "Voltar" foi clicado
                if botao_clicado(x_botao, y_botao, largura_botao, altura_botao, (x, y)):
                    return

        pygame.display.flip()