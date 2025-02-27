
def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

import numpy as np
dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteira', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casada', 'feminino']
    ]
)

var = dados[0::2, :2]
print(var)


dados = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

result_2 = []
for lista in dados:
    result_2 += lista
print(result_2)


fatorial = 1
for var in range(1,6):
  fatorial *= var

print(fatorial)


