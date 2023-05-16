import numpy as np
import matplotlib.pyplot as plt

class CurvaEmpuxo:

    def __init__(self, file, min, prop_massa):
        self.file = np.loadtxt(file, dtype=float)  # Arquivo de dados
        self.min_empuxo = min  # Empuxo mínimo para definir o início e fim da curva (N)
        self.prop_massa = prop_massa  # Massa de propelente (kg)
        self.x = np.round(self.file[:, 0], decimals=4)
        self.y = np.round(self.file[:, 1], decimals=4)
        self.GRAVIDADE = 9.80665
        self.table = []

    def refina_dados(self):
        tam = len(self.x)-1
        for i in range(tam, -1, -1):
            if self.y[i] < self.min_empuxo:
                self.x = np.delete(self.x, i)
                self.y = np.delete(self.y, i)
        print(self.x[0], self.x[-1])

    def impulso_total(self):

        self.refina_dados()

        while (len(self.x)-1) % 3 != 0:
            self.x = np.delete(self.x, -1)
            self.y = np.delete(self.y, -1)

        h = (self.x[-1] - self.x[0]) / (len(self.x)-1)
        n = 0
        soma = 0

        while n < len(self.x)-3:
            soma1 = 3*h/8 * (self.y[n] + 3*self.y[n+1] + 3*self.y[n+2] + self.y[n+3])
            soma = soma + soma1
            n = n + 3

        return self.table.append(['Impulso Total', np.round(soma, decimals=3), 'N*s'])

    def grafico(self):

        plt.plot(self.x, self.y)

        plt.xlabel('Tempo (s)')
        plt.ylabel('Eixo Y')
        plt.title('Curva')

        plt.savefig('grafico.png')

    def empuxo_max(self):
        return self.table.append(['Empuxo Máximo', np.round(max(self.y), decimals=3), 'N'])

    def empuxo_min(self):
        return self.table.append(['Empuxo Máximo', np.round(min(self.y), decimals=3), 'N'])

    def empuxo_med(self):
        return self.table.append(['Empuxo Médio',
                                  np.round(self.table[0][1] / (self.x[-1]-self.x[0]), decimals=3),
                                  'N'])

    def tempo_max_empuxo(self):
        max_value = np.max(self.y)
        return self.table.append(['Tempo Original de Empuxo Máximo',
                                  np.round(self.x[np.where(self.y == max_value)[0]][0], decimals=3),
                                  's'])

    def tempo_max_empuxo_corrigido(self):
        max_value = np.max(self.y)
        self.table.append(['Tempo Original de Empuxo Máximo Corrigido',
                           np.round(self.x[np.where(self.y == max_value)[0]][0] - min(self.x), decimals=3),
                           's'])

    def tempo_init(self):
        return self.table.append(['Tempo Original Inicial', np.round(min(self.x), decimals=3), 's'])

    def tempo_fim(self):
        return self.table.append(['Tempo Original Final', np.round(max(self.x), decimals=3), 's'])

    def tempo_queima(self):
        return self.table.append(['Tempo de Queima',
                                  np.round(max(self.x)-min(self.x), decimals=3),
                                  's'])

    def velociadade_media_gases(self):
        return self.table.append(['Velocidade Média de Ejeção dos Gases',
                                  np.round(self.table[0][1]/self.prop_massa, decimals=3),
                                  'm/s'])

    def impulso_especifico_med(self):
        return self.table.append(['Impulso Específico Média',
                                  np.round(self.table[0][1] / (self.prop_massa * self.GRAVIDADE), decimals=3),
                                  's'])

    def fluxo_massa_med(self):
        return self.table.append(['Fluxo de Massa Média',
                                  np.round(self.prop_massa / (self.x[-1]-self.x[0]), decimals=3),
                                  'Kg/s'])

    def relacao_maxemp_empumed(self):
        return self.table.append(['Razão Empuxo Máximo e Empuxo Médio',
                                  np.round((max(self.y) / (self.table[0][1] / (self.x[-1]-self.x[0])))*100, decimals=3),
                                  '%'])

    def relacao_empmin_empmax(self):
        return self.table.append(['Razão Empuxo Mínimo e Empuxo Máximo',
                                  np.round((min(self.y) / max(self.y))*100, decimals=3),
                                  '%'])

    def all(self):
        self.impulso_total()
        self.empuxo_max()
        self.empuxo_min()
        self.empuxo_med()
        self.tempo_max_empuxo()
        self.tempo_max_empuxo_corrigido()
        self.tempo_init()
        self.tempo_fim()
        self.tempo_queima()
        self.velociadade_media_gases()
        self.impulso_especifico_med()
        self.fluxo_massa_med()
        self.relacao_maxemp_empumed()
        self.relacao_empmin_empmax()
        self.grafico()
