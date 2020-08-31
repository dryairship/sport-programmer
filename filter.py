import pandas as pd

df = pd.read_csv('input.csv')
ans = df[['Roll Number','Codeforces Username']]
ans.to_csv('./codeforces/input.csv',index=False,header=False)
ans = df[['Roll Number','AtCoder Username']]
ans.to_csv('./atcoder/input.csv',index=False,header=False)