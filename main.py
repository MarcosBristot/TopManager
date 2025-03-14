from modules.database import carregar_dados
from modules.team import Time
from modules.player import Jogador
from modules.match import Partida
from interface import menu_principal, tela_listar_clubes, tela_simular_partida

# Função para carregar os dados iniciais
def carregar_times(dados):
    times = []
    for clube_data in dados["clubes"]:
        time = Time(clube_data["id"], clube_data["nome"])
        for jogador_data in clube_data["jogadores"]:
            jogador = Jogador(
                jogador_data["id"],
                jogador_data["nome"],
                jogador_data["idade"],
                jogador_data["overall"],
                jogador_data["posicao"]
            )
            time.adicionar_jogador(jogador)
        times.append(time)
    return times

# Função principal
def main():
    dados = carregar_dados("data/data.json")
    times = carregar_times(dados)

    while True:
        opcao = menu_principal()
        if opcao == "listar_clubes":
            tela_listar_clubes(times)
        elif opcao == "simular_partida":
            tela_simular_partida(times)
        elif opcao == "sair":
            break

if __name__ == "__main__":
    main()