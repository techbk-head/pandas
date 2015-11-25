import pandas as pd 
import json
path = {
	'nova':('b','a')
}

def read_log(log_name):
	cols = ['dates', 'pid', 'level', 'prog', 'info'] #Set columns for DataFrame
	log = pd.DataFrame()
	for log_path in path[log_name]:
		rl = pd.read_csv(log_path, sep='---', names=cols)
		log = log.append(rl,ignore_index=True)
	sort = log.sort(['dates']) #sort time

	return (sort)


def statistic_log(log_name):
	logs = read_log('nova')
	 = pd.DataFrame({'count' : sort.groupby( [ "dates", "level"] ).size()}).reset_index()
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