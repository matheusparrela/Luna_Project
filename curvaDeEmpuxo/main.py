import CurvaEmpuxo as ce
import GerarPDF as gp


file = 'teste.txt'  # Arquivo de dados
min = 0.25          # Empuxo mínimo para definir o início e fim da curva (N)
massa = 0.002542    # Massa de propelente (kg)


empuxo = ce.CurvaEmpuxo(file, min, massa)
empuxo.all()
print(empuxo.table)


gerador = gp.GerarPDF(0, 0, empuxo.table)  # Substitua 'a' pelo valor que você precisa
gerador.cabecalho()  # Gera o documento PDF com o cabeçalho centralizado
