import pandas as pd

marathon_2017 = pd.read_csv("../data/marathon_results_2017.csv")
marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'], axis=1)

print(marathon_2017_clean.info())

# 새로운 column이름을 정하고 bolean값을 넣음
marathon_2017_clean['Senior'] = marathon_2017_clean.Age > 60

# string 형식으로 넣는 것 유의
marathon_2017_clean['Year'] = '2017'

print(marathon_2017_clean.head())
print(marathon_2017_clean.info())