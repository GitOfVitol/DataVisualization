import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

marathon_2015_2017 = pd.read_csv("../data/marathon_2015to2017_final.csv")

#pie chart에 줄 label
labels = 'Male', 'Female'
#특정 슬라이스를 강조 - 0.1이 두번째 슬라이스를 조금 더 강조한다는 뜻
explode = (0, 0.1)

plt.figure(figsize=(7,7))
plt.pie(marathon_2015_2017['M/F'].value_counts(), explode=explode, labels=labels, startangle=90, shadow=True, autopct='%.1f')
plt.title("Male vs. Female", fontsize=18)

plt.show()