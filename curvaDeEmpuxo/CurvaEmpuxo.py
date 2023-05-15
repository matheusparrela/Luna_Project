import numpy as np
import matplotlib.pyplot as plt

class CurvaEmpuxo:

    def __init__(self, file, min):
        self.file = np.loadtxt(file, dtype=float)
        self.min_empuxo = min  # Empuxo mínimo para definir o início e fim da curva (N)


    def refina_dados(self, x, y):
        tam = len(x)-1
        for i in range(tam, -1, -1):
            if y[i] < 0.05:
                x = np.delete(x, i)
                y = np.delete(y, i)
        return x, y


    def impulso_total(self):

        x = np.round(self.file[:, 0], decimals=4)
        y = np.round(self.file[:, 1], decimals=4)

        x, y = self.refina_dados(x, y)

        while (len(x)-1) % 3 != 0:
            x = np.delete(x, -1)
            y = np.delete(y, -1)

        h = (x[-1] - x[0]) / (len(x)-1)
        n = 0
        soma = 0

        while n < len(x)-3:
            soma1 = 3*h/8 * (y[n] + 3*y[n+1] + 3*y[n+2] + y[n+3])
            soma = soma + soma1
            n = n + 3

        self.grafico(x, y)
        return soma


    def grafico(self, x, y):

        plt.plot(x, y)

        plt.xlabel('Tempo (s)')
        plt.ylabel('Eixo Y')
        plt.title('Curva')

        plt.savefig('grafico.png')


    '''
    def empuxo_max(self):
        return 0

    def empuxo_med(self):
        return 0

    def velociadade_media_gases(self):
        return 0

    def impulso_especifico_med(self):
        return 0

    def fluxo_massa_med(self):
        return 0
    '''
