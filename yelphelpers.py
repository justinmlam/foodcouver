import pandas as pd
import numpy as np

def expand_list(df,lst_col):
    """
    This function was taken from Heidi Jiang's "New Porkers" project
    See: https://github.com/heidijiang/new-porkers/
    
    """
    df = pd.DataFrame({
      col:np.repeat(df[col].values, df[lst_col].str.len())
      for col in df.columns.drop(lst_col)}
    ).assign(**{lst_col:np.concatenate(df[lst_col].values)})[df.columns]
    return df


def bayes_avg(df,cond,col):
    """
    This function was taken from Heidi Jiang's "New Porkers" project
    See: https://github.com/heidijiang/new-porkers/
    
    """
    v = df.groupby(cond)[col].size()
    m = df[cond].value_counts().mean()
    w = v/(v+m)
    S = w*df.groupby(cond)[col].mean() + (1-w)*df[col].mean()
    return S