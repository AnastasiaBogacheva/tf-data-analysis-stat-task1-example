import pandas as pd
import numpy as np

chat_id = 694882183 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    s = 0
    for i in range(len(x)):
      s = s + np.log(x[i]-247)
    s = s/len(x)
    return s # Ваш ответ
