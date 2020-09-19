import pandas as pd

marathon_2017 = pd.read_csv("../data/marathon_results_2017.csv")

marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'], axis=1)
print(marathon_2017_clean.info())

#space나 특수문자가 없는 경우 사용 가능 방식
names = marathon_2017_clean.Name
print(names)

#space나 특수문자가 있는 경우 string 방식으로 가져와야 함
officalTime = marathon_2017_clean['Official Time']
print(officalTime)