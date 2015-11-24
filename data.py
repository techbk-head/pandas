import pandas as pd 
import json
path = {
	'nova':('b','a')
}

def read_log(log_name): #Doc log cua cac file sau do roi convert ve dang dataframe  
    cols = ['dates', 'pid', 'level', 'prog', 'infor'] #Set columns for DataFrame
    log = pd.DataFrame()
    for log_path in path[log_name]:
    	rl = pd.read_csv(log_path, sep=',', names=cols) #Read file log and display to dataframe's format
    	log.append(rl,ignore_index=True) #Ghep log cua ac file
    sort = log.sort(['dates']) #sort time    
    return (sort)

def filter(log_name, date_start, date_finish): #Filte Log theo thoi gian 
	log = read_log(log_name)
	abc = df[(df['dates'] >= date_start) & (df['dates'] <= date_finish)]
	print (abc)

def print_dict(log_name):# Convert log tu dataframe ve dang format dictionary
    myJSON = df.to_json(path_or_buf = None, orient = 'records', date_format = 'iso', double_precision = 10, force_ascii = True, date_unit = 'ms', default_handler = None) # Attempt 1
    print (myJSON)


def proc_to_statis(log_name): #Nhom log theo cot 
    print (df.groupby(["dates", "level"]).count(numeric_only=True))
    

def statistic(log_name): #Giong ham proc_to_statis nhung nhom roi count tong so value cua moi level vi du error:4 , infor =5 
	gr = pd.DataFrame({'count' : df.groupby( [ "dates", "level"] ).size()}).reset_index()
	return (gr.to_json(orient='index')) 

if __name__ == '__main__':
	grap_log('nova')
    #read_log('nova')
	#df = read_log('b')
	#print_dict(df)
#	filter('nova', '2015-11-23', '2015-11-24 07:52:53')

