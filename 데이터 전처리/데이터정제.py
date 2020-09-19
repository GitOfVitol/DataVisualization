import pandas as pd

# 모든 column출력
pd.set_option('display.max_columns', None)
# column을 same line으로 fit
pd.set_option('display.width', None)

marathon_2017 = pd.read_csv("../data/marathon_results_2017.csv")

# 상위 5개 행 가져오기
print(marathon_2017.head())

# dataframe 구조
print(marathon_2017.info())

# axis=0이면 null값의 column합 1이면 row합
print(marathon_2017.isnull().sum(axis=0))

print(marathon_2017.columns)

# axis가 1이면 column, default는 0이며 row
marathon_2017_clean=marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'], axis='columns')
print(marathon_2017_clean.head())