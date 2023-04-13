import pandas as pd
import numpy as np


chat_id = 368780632 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p = ttest_ind(x,y).pvalue
    if(p<0.09):
      return True
    else:
      return False
