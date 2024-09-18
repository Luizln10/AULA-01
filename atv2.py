ganho = float(input("Quanto você ganha por hora: "))
horasTrabalhadas = int(input("Quantas horas você trabalha por mês(20 dias): "))

salarioTotal = ganho * horasTrabalhadas
print(f"O salário será {salarioTotal:, .2f}.")