import CurvaEmpuxo as ce

file = 'teste.txt'  # Arquivo de dados
min = 0.05          # Empuxo mínimo para definir o início e fim da curva (N)

empuxo = ce.CurvaEmpuxo(file, min)
print('Impulso Total:', empuxo.impulso_total())
