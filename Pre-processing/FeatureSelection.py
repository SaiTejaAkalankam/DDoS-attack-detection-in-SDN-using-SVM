no_of_flows_per_round = 0
round_no = 1
x = 0
SFE = 0
SSIP = 0
SSP = 0
SDFP = 0
SDFB = 0
no_of_src_packets_in_flow = list()
packet_size_in_flow = list()
src_ips = set()
src_ports = set()

# new dataframe for features
features_df = pd.DataFrame(columns=['SSIP', 'SSP', 'SDFP', 'SDFB', 'SFE', 'is_Attack'])

for index, row in traffic_df.iterrows():
# if the row is round number row then calculate and get the features
	if((row['cookie'] == 'round_no' or x == len(traffic_df) - 1) and row['duration'] != '1'):
 
		 x +=1

		# SFE
		 SFE = no_of_flows_per_round / 3

		# SSIP
		 SSIP = len(src_ips) / 3

		# SSP
		 SSP = len(src_ports) / 3

		# SDFP
		 SDFP = np.std(no_of_src_packets_in_flow)

		# SDFB
		 SDFB = np.std(packet_size_in_flow)

		# create a series of features and add that to features dataframe
		 series = pd.Series([SSIP, SSP, SDFP, SDFB, SFE, '0'], index=features_df.columns)
		 features_df = features_df.append(series, ignore_index=True)

		# clear sets and lists for new round
		 no_of_src_packets_in_flow.clear()
		 packet_size_in_flow.clear()
		 src_ips.clear()
		 src_ports.clear()

		# increment number of rounds variable
		 round_no+=1
		# clear number of flows in current round
		 no_of_flows_per_round = 0

 else:
# first row has round number only and no value for n_bytes and n_packets, therefore we skip it
	if(row['duration'] == '1' and row['cookie'] == 'round_no'):
	 	x+=1
	 	pass
 	else:
		# if it is a normal row, siply add the flows or source ips, etc
		 x += 1
		 no_of_flows_per_round += 1

		# add ip adress to set
		 src_ips.add(row['nw_src'])
		# add port number to set
		 src_ports.add(row['tp_src'])

		# add packet size
		 packet_size_in_flow.append(int(row['n_bytes'].strip("n_bytes=")))

		# add number of packets
		 no_of_src_packets_in_flow.append(int(row['n_packets'].strip("n_packets=")))
features_df.head()

# Add the column values of is_Attack column
for i in range(0, 300):
 features_df.iat[i,5] = 0
 
for i in range(300, 700):
 features_df.iat[i,5] = 1

for i in range(700, 1000):
 features_df.iat[i,5] = 0
 
features_df.head()
