import pandas as pd 
import json
path = {
	'nova':('b','a')
}

def read_log(log_name):
    cols = ['dates', 'pid', 'level', 'prog', 'infor'] #Set columns for DataFrame
    log = pd.DataFrame()
    for log_path in path[log_name]:
    	rl = pd.read_csv(log_path, sep=',', names=cols) #Read file log and display to dataframe's format
    	log.append(rl,ignore_index=True)
    sort = log.sort(['dates']) #sort time    
    return (sort)

def filter(log_name, date_start, date_finish):
	log = read_log(log_name)
	abc = df[(df['dates'] >= date_start) & (df['dates'] <= date_finish)]
	print (abc)

def proc_to_statis(log_name):
    print (df.groupby(["dates", "level"]).count(numeric_only=True))
    

def print_dict(log_name):
    myJSON = df.to_json(path_or_buf = None, orient = 'records', date_format = 'iso', double_precision = 10, force_ascii = True, date_unit = 'ms', default_handler = None) # Attempt 1
    print (myJSON)


def statistic(log_name):
	gr = pd.DataFrame({'count' : df.groupby( [ "dates", "level"] ).size()}).reset_index()
	return (gr.to_json(orient='index')) 

if __name__ == '__main__':
	grap_log('nova')
    #read_log('nova')
	#df = read_log('b')
	#print_dict(df)
#	filter('nova', '2015-11-23', '2015-11-24 07:52:53')

