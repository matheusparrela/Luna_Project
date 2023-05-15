import CurvaEmpuxo as ce
import GerarPDF as gp

file = 'teste.txt'  # Arquivo de dados
min = 0.05          # Empuxo mínimo para definir o início e fim da curva (N)
massa = 0.002542    # Massa de propelente (kg)

empuxo = ce.CurvaEmpuxo(file, min, massa)

print('Impulso Total:', empuxo.impulso_total(), 'N*s')
print('Empuxo Máximo:', empuxo.empuxo_max(), 'N')
print('Empuxo Médio:', empuxo.empuxo_med(), 'N')
print('Velocidade Média de ejeção dos gases:', empuxo.velociadade_media_gases(), 'm/s')
print('Impulso Específico Médio:', empuxo.impulso_especifico_med())
print('Fluxo de Massa Médio:', empuxo.fluxo_massa_med())


PDF = gp.GerarPDF(0)
PDF.file_pdf()