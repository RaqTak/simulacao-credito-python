# Simulador de Crédito Simples

print("=== Simulador de Análise de Crédito ===")

renda = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite o valor do empréstimo: "))
historico = input("Seu histórico de crédito é bom? (sim/nao): ").lower()
tempo_emprego = int(input("Tempo de emprego (em anos): "))

score = 0

# Regra 1: relação empréstimo/renda
if emprestimo <= renda * 5:
    score += 2
else:
    score -= 1

# Regra 2: histórico
if historico == "sim":
    score += 2
else:
    score -= 2

# Regra 3: estabilidade no emprego
if tempo_emprego >= 2:
    score += 1
else:
    score -= 1

# Decisão final
if score >= 3:
    print("Crédito APROVADO ✅")
elif score >= 1:
    print("Crédito EM ANÁLISE ⚠️")
else:
    print("Crédito NEGADO ❌")

print(f"Score final: {score}")
