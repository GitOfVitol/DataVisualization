import pandas as pd

# max_rows와 min_rows 주의 -> max보다 작은 값의 행을 출력하려면 min_rows로 설정
pd.set_option("display.min_rows", 50)

marathon_2017 = pd.read_csv("marathon_results_2017.csv")

marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'], axis=1)

# 비교 연산은 아래와 같이 dot expression으로 바로 사용
seniors = marathon_2017_clean.Age > 60
print(seniors)

# 특정한 조건을 만족시키는 것은 bracket expression을 사용
KEN_runner =marathon_2017_clean[marathon_2017_clean.Country == 'KEN']
print(KEN_runner)