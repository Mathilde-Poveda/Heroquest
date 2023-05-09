import pandas as pd

def bagging(df, iterations=1, samples=9):
    result = []
    for i in range(iterations+1):
        result.append(df.sample(n=samples))
    return result