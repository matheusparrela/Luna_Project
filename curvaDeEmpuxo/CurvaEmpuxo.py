import pandas as pd
import numpy as np

class CurvaEmpuxo:

    def __init__(self, file):
        self.file1 = pd.read_table(file)
        self.file = np.loadtxt(file, dtype=float)

    '''
    def refina_dados(self):
        return 0
    '''

    def impulso_total(self):

        x = np.round(self.file[0:-1, 0], decimals=4)
        y = np.round(self.file[0:-1, 1], decimals=4)
        h = (x[-1] - x[0])/len(x)
        print(np.round(h, decimals=4))

        n = 0
        soma = 0
        lim = int(len(y)/3)*3

        while n < lim:
            soma1 = 3*h/8 * (y[n] + 3 * y[n+1] + 3 * y[n + 3] + y[n + 4])
            soma = soma + soma1
            n = n + 3
        return soma

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
