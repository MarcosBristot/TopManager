from modules.team import Time
from modules.player import Jogador
from modules.match import Partida
from modules.database import carregar_dados, salvar_dados
from interface import menu_principal, tela_simular_partida

# Função para carregar times do arquivo JSON
def carregar_times():
    dados = carregar_dados("data/teams.json")
    times = []
    for time_data in dados["times"]:
        time = Time(time_data["nome"])
        for jogador_data in time_data["jogadores"]:
            jogador = Jogador(
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
    times = carregar_times()  # Carrega os times do arquivo JSON

    while True:
        opcao = menu_principal()
        if opcao == "gerenciar_times":
            print("Gerenciar times...")  # Implemente essa funcionalidade
        elif opcao == "simular_partida":
            tela_simular_partida(times)
        elif opcao == "sair":
            break
        else:
            print("Opção Inválida!")


if __name__ == "__main__":
    main()