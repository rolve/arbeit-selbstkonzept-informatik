import pandas
from scipy.stats import pearsonr


def calculate_corr_pvalues(df):
    dfcols = pandas.DataFrame(columns=df.columns)
    corr = dfcols.transpose().join(dfcols, how='outer')
    pvalues = corr.copy()
    for r in df.columns:
        for c in df.columns:
            clean = df[[r, c]].dropna()._get_numeric_data()
            if c != r and len(clean) > 0:
                corr[r][c], pvalues[r][c] = pearsonr(clean[r], clean[c])
            else:
                corr[r][c] = pvalues[r][c] = float('NaN')
    return corr, pvalues
