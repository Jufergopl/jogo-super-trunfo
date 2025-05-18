
import random

class Carta:
    def __init__(self, nome, velocidade, forca, inteligencia):
        self.nome = nome
        self.velocidade = velocidade
        self.forca = forca
        self.inteligencia = inteligencia

    def mostrar_atributos(self):
        return f"{self.nome} - Velocidade: {self.velocidade}, Força: {self.forca}, Inteligência: {self.inteligencia}"

def criar_baralho():
    return [
        Carta("Dragão", 7, 9, 6),
        Carta("Fênix", 9, 6, 8),
        Carta("Troll", 4, 10, 3),
        Carta("Elfo", 8, 5, 9),
        Carta("Gigante", 5, 8, 4),
        Carta("Unicórnio", 7, 7, 7),
    ]

def escolher_atributo():
    print("Escolha o atributo para jogar:")
    print("1 - Velocidade")
    print("2 - Força")
    print("3 - Inteligência")
    while True:
        escolha = input("Digite o número do atributo: ")
        if escolha in ["1", "2", "3"]:
            return int(escolha)
        else:
            print("Escolha inválida. Tente de novo.")

def comparar_cartas(carta_jogador, carta_computador, atributo):
    if atributo == 1:
        return carta_jogador.velocidade - carta_computador.velocidade
    elif atributo == 2:
        return carta_jogador.forca - carta_computador.forca
    else:
        return carta_jogador.inteligencia - carta_computador.inteligencia

def main():
    baralho = criar_baralho()
    random.shuffle(baralho)

    # Dividir cartas para jogador e computador
    jogador_cartas = baralho[:len(baralho)//2]
    computador_cartas = baralho[len(baralho)//2:]

    pontos_jogador = 0
    pontos_computador = 0

    rodada = 1
    while jogador_cartas and computador_cartas:
        print(f"\nRodada {rodada}")
        carta_jogador = jogador_cartas.pop(0)
        carta_computador = computador_cartas.pop(0)

        print("Sua carta:")
        print(carta_jogador.mostrar_atributos())

        atributo = escolher_atributo()

        resultado = comparar_cartas(carta_jogador, carta_computador, atributo)

        print("Carta do computador:")
        print(carta_computador.mostrar_atributos())

        if resultado > 0:
            print("Você ganhou essa rodada!")
            pontos_jogador += 1
            # Ganha a carta do computador também
            jogador_cartas.append(carta_jogador)
            jogador_cartas.append(carta_computador)
        elif resultado < 0:
            print("Computador ganhou essa rodada!")
            pontos_computador += 1
            computador_cartas.append(carta_jogador)
            computador_cartas.append(carta_computador)
        else:
            print("Empate! Cada um fica com sua carta.")
            jogador_cartas.append(carta_jogador)
            computador_cartas.append(carta_computador)

        rodada += 1

    print("\nFim do jogo!")
    print(f"Pontuação final - Você: {pontos_jogador} | Computador: {pontos_computador}")

    if pontos_jogador > pontos_computador:
        print("Parabéns! Você venceu o jogo!")
    elif pontos_computador > pontos_jogador:
        print("O computador venceu. Tente novamente!")
    else:
        print("Empate no jogo!")

if __name__ == "__main__":
    main()
