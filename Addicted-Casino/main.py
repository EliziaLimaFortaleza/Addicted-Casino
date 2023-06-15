num_fichas = int(input("Quantas fichas você possui?: "))


while num_fichas > 0:

    def ganho_do_jogo(jogada, k, n):
        if jogada % k == 0:
            return n
        else:
            return 0

    def numero_de_fichas(num_fichas, aposta, jogada, k, n):
        ganho = ganho_do_jogo(jogada, k, n)

        if ganho > 0:
            num_fichas += aposta * ganho
        else:
            num_fichas -= aposta

        return num_fichas

    aposta = int(input("Quanto deseja apostar?: "))
    num_apostas = int(input("Quantas apostas deseja fazer?: "))
    k = int(input("Em quantas jogadas acha que teria a chance de ganhar fichas?: "))
    n = int(
        input(
            f"Quantas fichas gostaria de receber, caso ganhe, após o múltiplo de {k} jogadas?: "
        )
    )

    for jogada in range(1, num_apostas + 1):
        num_fichas = numero_de_fichas(num_fichas, aposta, jogada, k, n)
        print("Saldo após a jogada", jogada, ":", num_fichas)

        if num_fichas <= 0:
            print("Fim do jogo.")
            break

        delta = int(input("Quanto gostaria de somar+ ou subtrair- da sua aposta?:"))
        aposta += delta

    if num_fichas <= 0:
        break

    continuar = input("Deseja continuar jogando? (S/N): ")
    if continuar.upper() != "S":
        break
