from modules.team import Time
from modules.player import Jogador
from modules.match import Partida
from modules.database import carregar_dados, salvar_dados

def menu_principal():
    print("Bem-vindo ao TopManager!")
    print("1. Gerenciar times")
    print("2. Simular partida")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    while True:
        opcao = menu_principal()
        if opcao == "1":
            print("Gerenciar times...")
        elif opcao == "2":
            print("Simular partida...")
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()