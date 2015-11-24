import pandas as pd 
import time
path = {
	'nova':('b','a')
#	'nova': ['opt/stack/']
#	'keystone': '',
#	'neutron': '',
}

def read_log(log_name):
	cols = ['dates', 'pid', 'level', 'prog', 'info'] #Set columns for DataFrame
	log = pd.DataFrame()
	for log_path in path[log_name]:
		abc = pd.read_csv(log_path, sep=',', names=cols)
    	#Read file log and display to dataframe's format
		# print (abc)
		log = log.append(abc,ignore_index=True)
	sort = log.sort(['dates']) #sort time
	#print (log.to_json(orient="records"))
	abc = log[(log['dates'] >= '2015-11-23') & (log['dates'] <= '2015-11-24 07:52:53')]
	print (abc)
#def filter(log_name, date_start, date_finish):
#	rl = read_log(log_name)
#	return (rl[(rl['dates'] >= date_start) & (rl['dates'] <= date_finish)].to_json(orient='records'))
    

if __name__ == '__main__':
	read_log('nova')
 #   filter('nova', '2015-11-21' , '2015-11-22')