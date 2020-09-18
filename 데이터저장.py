import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

marathon_2015 = pd.read_csv("marathon_results_2015.csv")
marathon_2016 = pd.read_csv("marathon_results_2016.csv")
marathon_2017 = pd.read_csv("marathon_results_2017.csv")

#concat은 기준 열 사용 없이 단순히 데이터를 연결, 기본적으로 위/아래로 데이터 행을 연결하며 단순히 연결해서 인덱스 값이 중복될 수 있음
#이때 ignore_index=True로 하면 기존 index를 무시하고 index를 매길 수 있음
#office time을 index로 두고 정리
marathon_2015_to_2017 = pd.concat([marathon_2015, marathon_2016, marathon_2017], ignore_index=True, sort=False).set_index('Official Time')

#각종 정보(mean, std, max, min 등등)
#print(marathon_2015_to_2017.describe())

#age에 대해 오름차순으로 정렬
#print(marathon_2015_to_2017.sort_values(by=['Age']))

#age에 대해 내림차순으로 정렬
#print(marathon_2015_to_2017.sort_values(by='Age', ascending=False))

#header=true이면 첫번째 줄을 column이름으로 사용
marathon_2015_to_2017.to_csv("marathon_2015_to_2017.csv", index=None, header=True)
