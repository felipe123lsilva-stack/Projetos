# Sistema de Classificação de Consumo de Água
# Projeto acadêmico - Python

print("   SISTEMA DE CLASSIFICAÇÃO DE CONSUMO")

# Solicita o tipo de imóvel
tipo = input(
    "Digite o tipo de imóvel "
    "(comercial, casa ou apartamento): "
).strip().lower()

# Solicita o consumo mensal
consumo = float(
    input("Digite o consumo mensal de água em m³: ")
)

# Classificação do consumo
if tipo == "comercial":
    print(
        "Tarifa comercial aplicada – "
        "consulte o plano corporativo."
    )

elif tipo == "apartamento" and consumo < 10:
    print(
        "Consumo econômico  "
        "excelente controle de água!"
    )
elif tipo == "apartamento" and consumo > 25:
    print(
        "Consumo excessivo: adote medidas como redução de tempo no banho "
        "e verifique vazamentos."
    )
elif (tipo == "apartamento" or tipo == "casa") and consumo <= 25:
    print(
        "Consumo moderado  "
        "dentro do padrão residencial."
    )

else:
    print(
        "Consumo excessivo  adote medidas de "
        "economia e verifique vazamentos."
    )

print("Obrigado por utilizar o sistema!")