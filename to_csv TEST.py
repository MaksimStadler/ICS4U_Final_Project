from pandas import *

parkData = read_csv('parkinsons_updrs.data')

parkData.to_csv('parkinsons_data.csv')
