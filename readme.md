Aqui será descrito o passo a passo de cala linha da programação solicitada de acordo com a agenda 6 de DS TI_I

# float+input
    valor_compra = float(input("Digite o valor total da compra (R$): "))
    usamos valor_compra como variável e o float para dizer que o valor a ser digitado deve ser um numeral e input significa que é um comando a ser dado pelo usuário

# Determina o percentual de desconto com base nas regras
    Aqui, queremos dizer que: "se" o valor da compra for inferior a R$200,00 o percentual de desconto aplicado será de 5%, caso sim, ele apenas ignora as outras linhas a seguir.
    if valor_compra < 200.00:
    percentual_desconto = 0.05  # 5%

    No elif, é uma condição intermediária, se o valor for superior a R$200,00 mas abaixo de R$300,00 a condição de 10% irá se aplicar.
    elif valor_compra < 300.00:
    percentual_desconto = 0.10  # 10%

    No else, aplica a condição que, caso diferente das anteriores, aplicar 15% de desconto, ou seja, superior a R$300,00.
    else:
    percentual_desconto = 0.15  # 15%

# Calcula o valor do desconto e o total a pagar

Aqui temos os calculos das variáveis do desconto.

valor_desconto = valor_compra * percentual_desconto

valor_final = valor_compra - valor_desconto


# Exibe os resultados formatados
    Ao término do imput, os calculos são feitos baseados no if, elif e else, apresentando os resultados através do print "f" strings formata e exibir textos e variáveis juntos de forma legivel, \ uma linha de espaço, primeira informação.

    print(f"\nResumo da Compra:")


    print(f"Valor original: R$ {valor_compra:.2f}")

    A letra f antes das aspas avisa o Python que tudo o que estiver dentro de chaves { } deve ser calculado ou substituído pelo valor da variável correspondente, em vez de ser exibido como texto puro.


    print(f"Desconto aplicado: {int(percentual_desconto * 100)}% (R$ {valor_desconto:.2f})")
    print(f"Valor total a pagar: R$ {valor_final:.2f}")