import sys
sys.path.append('..')
from sampling import sample
from saeaprg import SAEAPRG

problems = ['madelon', 'isolet', 'CNAE-9', 'ORL', 'COIL20', 'warpPIE10P', 'lung', 'lymphoma', 'relathe', 'DLBCL', 'leukemia', 'Gutenberg', 'arcene']
#
#
for pro in problems:
    for i in range(1):
        A = sample(pro)
        data = A[:, :-1]
        fitness = A[:, -1]
        algorithm = SAEAPRG(data, fitness, pro)
        algorithm.optimize()
print('Terminated!')