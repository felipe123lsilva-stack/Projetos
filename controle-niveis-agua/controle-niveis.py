from colorama import Fore, Style, init

init()

# Lista dos níveis mais baixo (1) ao máximo (5)
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)",
]


def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    else:
        return Fore.BLUE


# Simulação com valores definidos no código
leituras = [1, 2, 3, 4, 5]

for nivel in leituras:
    print(definir_cor(nivel) + niveis[nivel - 1])

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL, end="")