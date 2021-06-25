# normal traffic dataset
	normal_df1 = pd.read_csv('normaltraffic1.csv', sep=',', engine ='python')
	normal_df2 = pd.read_csv('normaltraffic2.csv', sep=',', engine ='python')
	normal_df1.head()
	# normal_df[normal_df['cookie'] == 'round_no']
	# attack traffic dataset
	attack_df = pd.read_csv('part1.csv', sep=',', engine ='python')
	attack_df.head()
	# deleting columns which are not required
	del new_df['dl_dst']
	del new_df['dl_src']
	del new_df['idle_age']
	del new_df['idle_timeout']
	del new_df['in_port']
	del new_df['actions']
	# import combined csv
	traffic_df = pd.read_csv('combined_traffic.csv', sep=',', engine ='python')
	traffic_df.head()
	#Cleaning the data
	traffic_df['cookie'] = traffic_df['cookie'].str.replace(r'cookie=', '')
	traffic_df['duration'] = traffic_df['duration'].str.replace(r'duration=', '')
	traffic_df['duration'] = traffic_df['duration'].str.replace(r's$', '')
	traffic_df['n_packets'] = traffic_df['n_packets'].str.replace(r'n_packets=', '')
	traffic_df['n_bytes'] = traffic_df['n_bytes'].str.replace(r'n_bytes=', '')
	traffic_df['nw_src'] = traffic_df['nw_src'].str.replace(r'nw_src=', '')
	traffic_df['nw_src'] = traffic_df['nw_src'].str.replace(r'arp_spa=', '')
	traffic_df['tp_src'] = traffic_df['tp_src'].str.replace(r'tp_src=', '')
	traffic_df['tp_src'] = traffic_df['tp_src'].str.replace(r'icmp_type=', '')
	traffic_df.head()
