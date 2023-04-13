import pandas as pd
import numpy as np
import scipy.stats as st


chat_id = 368780632 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    t_statistic, p_value = st.ttest_1samp(x, 500, alternative="two-sided")
    return p_value < 2*0.09 and x.mean() > 500
