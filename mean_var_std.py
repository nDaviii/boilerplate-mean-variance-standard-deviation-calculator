import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
    
  # faz a conversão pra uma array de 3x3
  array = np.array(list).reshape(3, 3)
    
  # faz o cálculo de cada estatística pedida
  calculations = {
        'mean': [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean().tolist()],
        'variance': [array.var(axis=0).tolist(), array.var(axis=1).tolist(), array.var().tolist()],
        'standard deviation': [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std().tolist()],
        'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max().tolist()],
        'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min().tolist()],
        'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum().tolist()]
    }

  return calculations