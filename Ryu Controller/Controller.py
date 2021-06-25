from operator import attrgetter
from ryu.app import simple_switch_13
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, DEAD_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib import hub
import main
from classifier import Classifier as c1
import sys
from datetime import datetime
import numpy as np
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ipv4
from ryu.lib.packet import tcp
from ryu.lib.packet import ether_types
import os

stored_seconds = 100
current_stats = list()
count_of_flow_entries = 0
no_of_src_packets_in_flow = list()
byte_size_in_flow = list()
src_ips = list()
src_ports = list()
src_macs = list()
# features
sfe = 0
ssip = 0
ssp = 0
SDFP = 0
SDFB = 0

class SimpleMonitor13(main.SimpleSwitch13):
	def __init__(self, *args, **kwargs):
		super(SimpleMonitor13, self).__init__(*args, **kwargs)
		 self.datapaths = {}
		 self.monitor_thread = hub.spawn(self._monitor)

		 # c1().predict_attack([897, 101, 0, 326, 897])
	@set_ev_cls(ofp_event.EventOFPStateChange,[MAIN_DISPATCHER, DEAD_DISPATCHER])
 	def _state_change_handler(self, ev):
 		datapath = ev.datapath
 		if ev.state == MAIN_DISPATCHER:
 			if datapath.id not in self.datapaths:
 				self.logger.debug('register datapath: %016x', datapath.id)
 				self.datapaths[datapath.id] = datapath
 			elif ev.state == DEAD_DISPATCHER:
 				if datapath.id in self.datapaths:
 					self.logger.debug('unregister datapath: %016x', datapath.id)
				 	del self.datapaths[datapath.id]
	def _monitor(self):
		while True:
 			for dp in self.datapaths.values():
 				self._request_stats(dp)
 			hub.sleep(3)
 	def _request_stats(self, datapath):

 		# print(datapath)
		  ofproto = datapath.ofproto
		  parser = datapath.ofproto_parser
		  req = parser.OFPFlowStatsRequest(datapath)
		  datapath.send_msg(req)
		  # req = parser.OFPPortStatsRequest(datapath, 0, ofproto.OFPP_ANY)
		  # datapath.send_msg(req)
		  
	@set_ev_cls(ofp_event.EventOFPFlowStatsReply, MAIN_DISPATCHER)
 	def _flow_stats_reply_handler(self, ev):
 		body = ev.msg.body
 		datapath = ev.msg.datapath
 		global current_stats
 		global stored_seconds
 		global count_of_flow_entries
 		dt = datetime.now()
 		flow_seconds = dt.strftime("%S")
 		
 		if(stored_seconds != flow_seconds):
 			self.calculate_features(datapath)
 			# start a new flow stats entrey for next time interval
 			stored_seconds = flow_seconds
 			current_stats = body
 		# it is same flow stats reply's other message
 		else:
 			current_stats.extend(body)
 	def calculate_features(self, datapath):
 		global byte_size_in_flow
 		global no_of_src_packets_in_flow
 		global SDFP
 		global SDFB
 		no_of_flows_in_interval = 0
 		
 		for x in current_stats:
 			duration_of_flow = (float(x.duration_nsec) / 1000000000) + x.duration_sec
 			# take only last 5 seconds flow entries from dump-flows stats
 			if(duration_of_flow <= 5):
 				no_of_flows_in_interval +=1
 				# add soucre ip of flow in a list of soucre ip's for current interval
 				if('ipv4_src' in x.match):
 					src_ips.append(x.match['ipv4_src'])
 					
 				# add byte_count of flow in a list of byte count's for current interval
 				byte_size_in_flow.append(x.byte_count)
 				# add packet_count of flow in a list of packet count's for current interval
 				no_of_src_packets_in_flow.append(x.packet_count)
 				
 				# increment flow count for interval
 				# add soucre mac of flow in a list of soucre mac's for current interval
 				if('eth_src' in x.match):
 					src_macs.append(x.match['eth_src'])
			# features
 		SSIP = float(len(src_ips)) / 5
 		if(byte_size_in_flow):
 			SDFP = np.std(no_of_src_packets_in_flow)
 		# to remove nan values for empty list for standard deviation
 		else:
 			no_of_src_packets_in_flow = [0]
 		if(byte_size_in_flow):
 			SDFB = np.std(byte_size_in_flow)
 		else:
 			byte_size_in_flow = [0]
 		SFE = float(no_of_flows_in_interval) / 5
 		features = [SSIP, SSIP, SDFP, SDFB, SFE]
 		print(features)
 		c1().predict_attack(features)
 		# c1().myfunc2()
 		# c1().myfunc2()
		 # if(SSIP > 300):
		 # ofproto = datapath.ofproto
		 # parser = datapath.ofproto_parser
		 # priority = 5000
		 # # delete all flows of attack src
		 # command=ofproto.OFPFC_DELETE
		 # match=parser.OFPMatch(in_port=1)
		 # mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
		 # match=match, command=command, out_port=ofproto.OFPP_ANY,
		out_group=ofproto.OFPG_ANY)
		 # datapath.send_msg(mod)
		 # # send drop mod
		 # match = parser.OFPMatch(in_port=1)
		 # # actions = [ofp_parser.OFPActionOutput(ofp.OFPP_NORMAL,)]
		 # inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,[])]
		 # mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
		 # match=match, instructions=inst)
		 # datapath.send_msg(mod)
		 # # c1().predict_attack([895.0,108.0,0.0,326.6476184922625,891.0])
		 # print("sent drop to s1")
		 print("-----------------------------------------------------")
		 # call classifier funtion value
		del byte_size_in_flow[:]
 		del no_of_src_packets_in_flow[:]
 		del src_ips[:]
 		del src_macs[:]
 		
 		return
 				 
