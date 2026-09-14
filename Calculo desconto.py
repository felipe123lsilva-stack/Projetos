# Solicita o valor total da compra ao usuário
valor_compra = float(input("Digite o valor total da compra (R$): "))

# Determina o percentual de desconto com base nas informações fornecidas
if valor_compra < 200.00:
    percentual_desconto = 0.05  # 5% (corrigido para 5% conforme a regra de desconto)
elif valor_compra < 300.00:
    percentual_desconto = 0.10  # 10% (corrigido para 10% conforme a regra de desconto)
else:
    percentual_desconto = 0.15  # 15% (corrigido para 15% conforme a regra de desconto)

# Calcula o valor do desconto e o total a pagar
valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto

# Exibe os resultados formatados
print(f"\nResumo da Compra:")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {int(percentual_desconto * 100)}% (R$ {valor_desconto:.2f})")
print(f"Valor total a pagar: R$ {valor_final:.2f}")