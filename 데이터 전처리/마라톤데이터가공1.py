import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

marathon_2015 = pd.read_csv("../data/marathon_results_2015.csv")
marathon_2016 = pd.read_csv("../data/marathon_results_2016.csv")
marathon_2017 = pd.read_csv("../data/marathon_results_2017.csv")

marathon_2015['Year'] = '2015'
marathon_2016['Year'] = '2016'
marathon_2017['Year'] = '2017'

marathon_2015to2017_final = pd.concat([marathon_2015, marathon_2016, marathon_2017], ignore_index=True, sort=False)

marathon_2015to2017_final = marathon_2015to2017_final.drop(['Unnamed: 0', 'Bib', 'Citizen', 'Unnamed: 9', 'Proj Time', 'Unnamed: 8'], axis='columns')

marathon_2015to2017_final['5K'] = pd.to_timedelta(marathon_2015to2017_final['5K'])
marathon_2015to2017_final['10K'] = pd.to_timedelta(marathon_2015to2017_final['10K'])
marathon_2015to2017_final['15K'] = pd.to_timedelta(marathon_2015to2017_final['15K'])
marathon_2015to2017_final['20K'] = pd.to_timedelta(marathon_2015to2017_final['20K'])
marathon_2015to2017_final['Half'] = pd.to_timedelta(marathon_2015to2017_final['Half'])
marathon_2015to2017_final['25K'] = pd.to_timedelta(marathon_2015to2017_final['25K'])
marathon_2015to2017_final['30K'] = pd.to_timedelta(marathon_2015to2017_final['30K'])
marathon_2015to2017_final['35K'] = pd.to_timedelta(marathon_2015to2017_final['35K'])
marathon_2015to2017_final['40K'] = pd.to_timedelta(marathon_2015to2017_final['40K'])
marathon_2015to2017_final['Pace'] = pd.to_timedelta(marathon_2015to2017_final['Pace'])
marathon_2015to2017_final['Official Time'] = pd.to_timedelta(marathon_2015to2017_final['Official Time'])

marathon_2015to2017_final['5K'] = marathon_2015to2017_final['5K'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['10K'] = marathon_2015to2017_final['10K'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['15K'] = marathon_2015to2017_final['15K'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['20K'] = marathon_2015to2017_final['20K'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['Half'] = marathon_2015to2017_final['Half'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['25K'] = marathon_2015to2017_final['25K'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['30K'] = marathon_2015to2017_final['30K'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['35K'] = marathon_2015to2017_final['35K'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['40K'] = marathon_2015to2017_final['40K'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['Pace'] = marathon_2015to2017_final['Pace'].astype('m8[s]').astype(np.int64)
marathon_2015to2017_final['Official Time'] = marathon_2015to2017_final['Official Time'].astype('m8[s]').astype(np.int64)

marathon_2015to2017_final.to_csv('marathon_2015to2017_final.csv', index=None, header=True)