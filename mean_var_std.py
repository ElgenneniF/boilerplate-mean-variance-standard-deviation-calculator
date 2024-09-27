import numpy as np

def calculate(list):

    # ve se tem 9 elementos
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # faz um array 3x3
    matrix = np.array(input_list).reshape(3, 3)
    
    # Calcula as estatisticas
    calculations = {
        'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()],
        'variance': [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()],
        'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()],
        'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()],
        'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()],
        'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]
    }

    return calculations