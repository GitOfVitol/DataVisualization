#Age 별로 정렬
import pandas as pd
import matplotlib.pyplot as plt

marathon_2015_2017 = pd.read_csv('../data/marathon_2015to2017_final.csv')

runner_1860 = marathon_2015_2017[marathon_2015_2017.Age.isin(range(18, 60))]
runner_1860_counting = runner_1860['Age'].value_counts()

# age도 column으로 만들기 위해 새로운 dataframe 만듦
runner_age = pd.DataFrame({
    'Age' : runner_1860_counting.index,
    'Count' : runner_1860_counting
})
runner_age_sort = runner_age.sort_values(by=['Age'])

x = runner_age_sort.index
x = [str(i) for i in x]
#y는 dataframe 형태라 에러가 발생할 수 있음, sum과 cumsum은 dataframe에서 사용할 수 있음
y = runner_age_sort['Count']
ratio = y / y.sum()
ratio_sum = ratio.cumsum()
#dataframe 형태로 에러가 발생하니 리스트 형태로 변환
y_ratio = [i for i in ratio_sum]

fig, barChart = plt.subplots(figsize=(20, 10))
barChart.bar(x, y)

lineChart = barChart.twinx()
lineChart.plot(x, ratio_sum, '-ro', alpha=0.5)
ranges = lineChart.get_yticks()
lineChart.set_yticklabels(['{:.1%}'.format(x) for x in ranges])

ratio_sum_percentages = ['{0:.0%}'.format(x) for x in ratio_sum]
for i, txt in enumerate(ratio_sum_percentages):
    lineChart.annotate(txt, (x[i], y_ratio[i]), fontsize=10)

barChart.set_xlabel('Age', fontdict={'size': 16})
barChart.set_ylabel('Number of runner', fontdict= {'size':16})
plt.title('Dual Axis Chart - Number of runner by Age', fontsize = 18)

plt.show()
