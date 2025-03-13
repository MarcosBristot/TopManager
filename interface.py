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

        # Desenha os botões
        desenhar_botao("Gerenciar Times", 300, 200, 200, 50, VERDE)
        desenhar_botao("Simular Partida", 300, 300, 200, 50, VERDE)
        desenhar_botao("Sair", 300, 400, 200, 50, VERMELHO)

        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verifica se o botão "Gerenciar Times" foi clicado
                if botao_clicado(300, 200, 200, 50, (x, y)):
                    return "gerenciar_times"
                # Verifica se o botão "Simular Partida" foi clicado
                if botao_clicado(300, 300, 200, 50, (x, y)):
                    return "simular_partida"
                # Verifica se o botão "Sair" foi clicado
                if botao_clicado(300, 400, 200, 50, (x, y)):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

# Função para exibir a tela de simulação de partida
def tela_simular_partida(times):
    while True:
        tela.fill(BRANCO)

        # Exibe os times disponíveis
        y = 50
        for i, time in enumerate(times):
            texto = f"{i + 1}. {time.nome}"
            texto_surface = fonte.render(texto, True, PRETO)
            tela.blit(texto_surface, (50, y))
            y += 50

        # Botão de voltar
        desenhar_botao("Voltar", 50, 500, 100, 50, AZUL)

        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verifica se o botão "Voltar" foi clicado
                if botao_clicado(50, 500, 100, 50, (x, y)):
                    return  # Retorna ao menu principal

        pygame.display.flip()