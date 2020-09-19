import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

marathon_2015_2017 = pd.read_csv('../data/marathon_2015to2017_final.csv')

#18~59세까지
runner_1860 = marathon_2015_2017[marathon_2015_2017.Age.isin(range(18, 60))]
#Age 값별로 counting
runner_1860_counting = runner_1860['Age'].value_counts()

x = runner_1860_counting.index

#이걸 안하면 x값이 int형이라 자동으로 오름차순으로 sorting 됨, str로 변환해야 유지
x = [str(i) for i in x]
y = runner_1860_counting.values
ratio = y / y.sum()

#비율을 누적 합계로 표현
ratio_sum = ratio.cumsum()

fig, barChart = plt.subplots(figsize=(20, 10))
barChart.bar(x, y)

#barChart와 같은 x값을 가짐
lineChart = barChart.twinx()

#-는 solid, r은 red, o는 circle을 의미 -> line의 구성 성분, alpha는 투명도
lineChart.plot(x, ratio_sum, '-ro', alpha=0.5)

#lineChart의 오른쪽 y의 label을 위한 값을 가져온 다음에 %형식으로 formating
ranges = lineChart.get_yticks()
lineChart.set_yticklabels(['{:.1%}'.format(x) for x in ranges])

#annotation을 위한 범위값 설정
ratio_sum_percentages = ['{0:.0%}'.format(x) for x in ratio_sum]
#enumerate는 list안의 값에 대해 index를 매김, i가 index이고 txt가 %값
for i, txt in enumerate(ratio_sum_percentages):
    lineChart.annotate(txt, (x[i], ratio_sum[i]), fontsize=10)

barChart.set_xlabel('Age', fontdict= {'size': 16})
barChart.set_ylabel('Number of runner', fontdict= {'size':16})
plt.title('Pareto Chart - Number of runner by Age', fontsize = 18)

plt.show()
