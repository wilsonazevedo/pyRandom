import pandas as pd
import numpy as np

def minimization(x1, x2, x3):
  return 10 * ((x1 - 1)**2 + 2 * (x2 - 2)**2 + 3 * (x3 - 3)**2)

def convert_to_range(value, lower_limit, upper_limit):
  return lower_limit + (upper_limit - lower_limit) * value

random_population = [[0.55, 0.85,   0.23], [0.13,   0.93,   0.45], [0.23,   0.34,   0.65]]
df_random_population = pd.DataFrame(random_population, columns=['x1', 'x2', 'x3'])

df_random_population