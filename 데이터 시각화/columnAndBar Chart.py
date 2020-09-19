import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
marathon_2015_2017 = pd.read_csv("../data/marathon_2015to2017_final.csv")

USA_runner = marathon_2015_2017[marathon_2015_2017.Country == 'USA']

#figure 가로세로 size결정
plt.figure(figsize=(15,10))
runner_state = sns.countplot('State', data=USA_runner)
runner_state.set_title('Number of Runner by State - USA', fontsize=18)
runner_state.set_xlabel('State', fontdict= {'size':8})
runner_state.set_ylabel('Number of Runner', fontdict= {'size':16})
plt.show()

plt.figure(figsize=(15,10))
#data는 대상이 되는 dataframe을 지정, 앞에는 dataframe의 열 이름 문자열
#hue는 category가 섞여 있는것을 색을 다르게 할 수 있음
runner_state = sns.countplot('State', data=USA_runner, hue='M/F', palette={'F':'r', 'M':'b'})
runner_state.set_title('Number of Runner by State, Gender - USA', fontsize=18)
runner_state.set_xlabel('State', fontdict= {'size':8})
runner_state.set_ylabel('Number of Runner', fontdict= {'size':16})
plt.show()

plt.figure(figsize=(15,10))
runner_state = sns.countplot('State', data=USA_runner, hue='Year')
runner_state.set_title('Number of Runner by State, Year - USA', fontsize=18)
runner_state.set_xlabel('State', fontdict= {'size':8})
runner_state.set_ylabel('Number of Runner', fontdict= {'size':16})
plt.show()
