import pandas as pd
import time
import json
path = {
	'nova':('b','a')
}

def detect_log_file(service_name):
    list_file = []
    #code tiep ...
    return list_file

def convert_time(log,time_unit):
    if time_unit = 'second':
        log['dates'] = pd.to_datetime(log['dates'], format='%Y-%m-%d %H:%M:%S')
        time = time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        if time_unit = 'minute':
            time = time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            if:
            else:
    return time


def read_log_file(service_name): #Doc log cua cac file sau do roi convert ve dang dataframe  
    cols = ['dates', 'pid', 'level', 'prog', 'infor'] #Set columns for DataFrame
    log = pd.DataFrame()
    for log_file in path[service_name]:
    	read_file = pd.read_csv(log_path, sep=',', names=cols) #Read file log and display to dataframe's format
    	log.append(read_file,ignore_index=True) #Ghep log cua ac file
    log = log.sort(['dates'],ascending=False) #sort time    
    return log

def filter_log(service_name, date_start, date_finish): #Filte Log theo thoi gian 
	log = read_log_file(service_name)
	filtered_log = log[(log['dates'] >= date_start) & (log['dates'] <= date_finish)]
	return filtered_log.to_json(orient="index")

def statistic_log(service_name, date_start, date_finish, time_unit): #Giong ham proc_to_statis nhung nhom roi count tong so value cua moi level vi du error:4 , infor =5 
	log = filter_log(service_name, date_start, date_finish)
    convert_time_log = convert_time(log,time_unit)

    count_per_level = pd.DataFrame({'count' : sort.groupby( [ "dates", "level"] ).size()}).reset_index()
    sum_each = pd.DataFrame({'sum' : gr.groupby(["level"])["count"].sum()}).reset_index()
    total = gr['count'].sum()
    summary = {}
    summary['Total'] = total
    for index, col in sum_each.iterrows():
        summary[col['level']] = col['sum']
    abc = {}
    abc['summary'] = summary
    print (abc)

if __name__ == '__main__':
	grap_log('nova')
    #read_log('nova')
	#df = read_log('b')
	#print_dict(df)
#	filter('nova', '2015-11-23', '2015-11-24 07:52:53')

