import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

marathon_2015_2017 = pd.read_csv("../data/marathon_2015to2017_final.csv")

plt.figure(figsize=(20,10))

#histogram을 위한 chart를 만들어줌
#FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
age_count = sns.distplot(marathon_2015_2017.Age)
age_count.set_xlabel('Ages', fontdict= {'size':16})
age_count.set_ylabel('Distribution Rate', fontdict= {'size':16})
age_count.set_title('Distribution Rate by Ages', fontsize=18)
plt.show()

"""
y축이 비율이 아닌 명 수 

age_count = sns.countplot('Age', data=marathon_2015_2017)
age_count.set_xlabel('Ages', fontdict= {'size':16})
age_count.set_ylabel('Distribution Rate', fontdict= {'size':16})
age_count.set_title('Distribution Rate by Ages', fontsize=18)
plt.show()
"""

"""
sorting

age_count = sns.countplot('Age', data=marathon_2015_2017, order=marathon_2015_2017['Age'].value_counts().index)
age_count.set_xlabel('Ages', fontdict= {'size':16})
age_count.set_ylabel('Distribution Rate', fontdict= {'size':16})
age_count.set_title('Distribution Rate by Ages', fontsize=18)
plt.show()

"""