import pandas as pd 
import time
path = {
	'nova':('b','a')
}

def read_log(log_name):
	cols = ['dates', 'pid', 'level', 'prog', 'info'] #Set columns for DataFrame
	log = pd.DataFrame()
	for log_path in path[log_name]:
		abc = pd.read_csv(log_path, sep=',', names=cols)
		log = log.append(abc,ignore_index=True)
	sort = log.sort(['dates'])
	return sort

def filter(log_name, dates_from, dates_finish):
	log = read_log('nova')
	abc = log[(log['dates'] >= dates_from) & (log['dates'] <= dates_finish)]
	print (abc)    

if __name__ == '__main__':
#	read_log('nova')
   filter('nova', '2015-11-1' , '2015-11-24')