import pandas as pd
import numpy as np
"""
1. user defined function으로 구현 

# pandas 내부에서는 Dtype이 object로 되어 있어서 record.str 같은 방식으로 string 형식으로 변환
# pandas split함수 -> :를 기준으로 2번째 :까지 나눔, expand가 true이면 별개의 column false이면 1개의 column
# pandas astype -> dataframe을 특정한 data type으로 변경
def to_seconds(record):
    hms = record.str.split(':', n=2, expand =True)
    return hms[0].astype(int) * 3600 + hms[1].astype(int) * 60 + hms[2].astype(int)
    
marathon_2017 = pd.read_csv("marathon_results_2017.csv")
marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'], axis=1)

marathon_2017_clean['Senior'] = marathon_2017_clean.Age > 60
marathon_2017_clean['Year'] = '2017'

marathon_2017_clean['Official Time Sec'] = to_seconds(marathon_2017_clean['Official Time'])
print(marathon_2017_clean.head())
"""
marathon_2017 = pd.read_csv("marathon_results_2017.csv")
marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'], axis=1)

marathon_2017_clean['Senior'] = marathon_2017_clean.Age > 60
marathon_2017_clean['Year'] = '2017'

# timedelta 형으로 변환
marathon_2017_clean['Official Time Sec'] = pd.to_timedelta(marathon_2017_clean['Official Time'])

# 초단위 형태로 변환, numpy를 이용해서 int64로 변환
marathon_2017_clean['Official Time New'] = marathon_2017_clean['Official Time Sec'].astype('m8[s]').astype(np.int64)

print(marathon_2017_clean.info())
print(marathon_2017_clean.head())

