import numpy as np
import matplotlib.pyplot as plt
import re

ersetzungen = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

erlaubte_worte = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
]

def stringfkt(string):

    # alle wörter finden und schauen, ob sie erlaubt sind
    for wort in re.findall('[a-zA-Z_]+', string):
        if wort not in erlaubte_worte:
            raise ValueError(
                '"{}" ist verboten'.format(word)
            )

    for alt, neu in ersetzungen.items():
        string = string.replace(alt, neu)

    def func(x):
        return eval(string)

    return func

if __name__ == '__main__':

    func = stringfkt(input('Formel: f(x) = '))
    a = float(input('Bereichsgrenze links: '))
    b = float(input('Bereichsgrenze rechts: '))
    x = np.linspace(a, b, 250)

    plt.plot(x, func(x))
    plt.xlim(a, b)
    plt.show()