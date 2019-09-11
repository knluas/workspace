import pandas as pd
import seaborn as sns
import numpy as np

#df = 표
df = pd.read_csv("해쉬태그.csv", encoding='utf-8')
#print(df.count())
#dfFiltered = df[df['0'] == '#예술강사']
#print(dfFiltered.count())
#print(dfFiltered.head(5))  #상위 5개 뽑기
nan=float('NaN')
clean = df.replace('', nan)
print(clean['0']).value_counts()  #컬럼의 데이터 카운트
#print(len(df)) #데이터의 길이
#print(df['0'].unique()) #유니크한 값만 뽑기
#print(df.describe(include='np.object'))
#print(pd.melt(df, value_vars=['0','1']).rename(columns={'variable':'var','value':'val'}))
#df.iloc.str(kind='bar')
